import pathlib
import shutil
import http.server
import socketserver
import webbrowser

import requests

organization = "mozilla"
repo = "pdf.js"
api_url = f"https://api.github.com/repos/{organization}/{repo}/releases/latest"

infos = requests.get(api_url).json()


def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, "wb") as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


here = pathlib.Path(".").absolute()
dest = here / "viewer.zip"
sandbox = here / "sandbox"
index = here / "index.html"
pdf = here / "test.pdf"

download_url(infos["assets"][0]["browser_download_url"], dest)

shutil.unpack_archive(str(dest), str(sandbox))
shutil.copy2(str(pdf), sandbox / "web")

PORT = 8006
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    webbrowser.open(f"localhost:{PORT}")
    print("serving at port", PORT)
    httpd.serve_forever()
