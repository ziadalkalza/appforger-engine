from urllib.parse import urlparse

def normalize_repo_url(url: str) -> dict:
    if url.startswith("git@bitbucket.org:"):
        rest=url.split(":",1)[1].removesuffix(".git")
        workspace, repo = rest.split("/",1)
        return {"provider":"bitbucket","product":"cloud","workspace":workspace,"repo_slug":repo}
    u=urlparse(url)
    host=u.netloc
    path=[x for x in u.path.strip("/").removesuffix(".git").split("/") if x]
    if "bitbucket.org" in host and len(path)>=2:
        return {"provider":"bitbucket","product":"cloud","workspace":path[0],"repo_slug":path[1]}
    if "github.com" in host and len(path)>=2:
        return {"provider":"github","owner":path[0],"repo":path[1]}
    if "gitlab" in host and len(path)>=2:
        return {"provider":"gitlab","namespace":"/".join(path[:-1]),"repo":path[-1]}
    return {"provider":"generic_git","url":url}
