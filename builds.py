import requests
from bs4 import BeautifulSoup


def build_search(search):
    beginner_builds = {}
    pvp_builds = {}
    pve_builds = {}
    search = search.lower()
    baseurl = "https://alcasthq.com/eso-"
    if search == "necromancer":
        uri = baseurl + search + "-class-list/"
    else:
        uri = baseurl + search + "/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    result = requests.get(uri, headers=headers)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, 'html.parser')
        content = soup.find(class_="post-content")
        for a in content.find_all('a', href=True, text=True):
            if "beginner" in a['href']:
                beginner_builds[a['href']] = a.string
            elif "pve" in a['href']:
                pve_builds[a['href']] = a.string
            elif "pvp" in a['href']:
                pvp_builds[a['href']] = a.string
        return beginner_builds, pvp_builds, pve_builds
    else: 
        print("No Response")
