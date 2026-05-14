import os, tempfile, subprocess, urllib.request, base64, json
from pathlib import Path

class BitbucketProvider:
    def __init__(self, env=None):
        self.env = env or os.environ

    def _auth_header(self):
        user=self.env.get("BITBUCKET_CLOUD_USERNAME","")
        token=self.env.get("BITBUCKET_CLOUD_API_TOKEN","")
        if user and token:
            raw=base64.b64encode(f"{user}:{token}".encode()).decode()
            return {"Authorization": f"Basic {raw}"}
        dc=self.env.get("BITBUCKET_DATA_CENTER_TOKEN","")
        if dc:
            return {"Authorization": f"Bearer {dc}"}
        return {}

    def _request_json(self, url):
        req=urllib.request.Request(url, headers=self._auth_header())
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())

    def list_files(self, source):
        workspace=source.get("workspace") or self.env.get("BITBUCKET_CLOUD_WORKSPACE")
        repo=source.get("repo_slug")
        branch=source.get("branch","main")
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo}/src/{branch}/?pagelen=100"
        data=self._request_json(url)
        return [v["path"] for v in data.get("values",[]) if v.get("type")=="commit_file"]

    def fetch_file(self, source, path):
        workspace=source.get("workspace") or self.env.get("BITBUCKET_CLOUD_WORKSPACE")
        repo=source.get("repo_slug")
        branch=source.get("branch","main")
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo}/src/{branch}/{path}"
        req=urllib.request.Request(url, headers=self._auth_header())
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode(errors="ignore")

    def export_to_temp(self, source):
        url=source.get("repo_url")
        if not url:
            raise ValueError("repo_url required for clone fallback")
        tmp=Path(tempfile.mkdtemp(prefix="appforge_bitbucket_"))
        subprocess.check_call(["git","clone","--depth","1",url,str(tmp)])
        return tmp
