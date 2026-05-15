import os, json, urllib.request, base64
from .confluence_normalizer import html_to_markdownish

class ConfluenceProvider:
    def __init__(self, env=None):
        self.env=env or os.environ

    def _cloud_headers(self):
        email=self.env.get("CONFLUENCE_CLOUD_EMAIL","")
        token=self.env.get("CONFLUENCE_CLOUD_API_TOKEN") or self.env.get("CONFLUENCE_CLOUD_SCOPED_TOKEN","")
        h={"Accept":"application/json"}
        if email and token:
            raw=base64.b64encode(f"{email}:{token}".encode()).decode()
            h["Authorization"]=f"Basic {raw}"
        elif token:
            h["Authorization"]=f"Bearer {token}"
        return h

    def _dc_headers(self):
        token=self.env.get("CONFLUENCE_DATA_CENTER_PAT","")
        h={"Accept":"application/json"}
        if token: h["Authorization"]=f"Bearer {token}"
        return h

    def fetch_page_cloud(self, base_url, page_id):
        url=f"{base_url.rstrip('/')}/wiki/api/v2/pages/{page_id}?body-format=storage"
        req=urllib.request.Request(url,headers=self._cloud_headers())
        with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())

    def fetch_page_dc(self, base_url, page_id):
        url=f"{base_url.rstrip('/')}/rest/api/content/{page_id}?expand=body.storage,version,metadata.labels"
        req=urllib.request.Request(url,headers=self._dc_headers())
        with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())

    def normalize_page(self, data):
        title=data.get("title","untitled")
        body=""
        if "body" in data:
            body = data.get("body",{}).get("storage",{}).get("value","")
        labels = []
        md = f"# {title}\n\n" + html_to_markdownish(body) + "\n"
        return {"title": title, "markdown": md, "labels": labels, "raw": data}
