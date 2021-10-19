import urllib.request
import shutil

def download(url, path):
  with urllib.request.urlopen(url) as response, open(path, "wb") as dest:
    shutil.copyfileobj(response, dest)
