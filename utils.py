import bs4
import requests as req
import re
import random
from urllib.parse import unquote

def RandomUA():
    ua_arr = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    ]
    return random.choice(ua_arr)



def HongshuParser(url: str) -> dict:
    try:
        print(url)
        headers = {
            'User-Agent':RandomUA()
        }
        html = req.get(url, headers=headers)
        soup = bs4.BeautifulSoup(html.content.decode(),features="lxml")
        images = soup.find_all("meta",attrs={'name': "og:image"})

        descriptions = soup.find_all("meta",attrs={'name': "description"})
        urls = re.findall(r'content="([^"\']*)"', str(images))
        description = re.findall(r'<meta content="(.*?)" name="description"', str(descriptions))[0]
        images = []
        for s in urls:
            images.append(re.findall(r'/([^!/]+)!', s)[0])

        return {"images": images, "description":description}
    except:
        return {"message": "Internal Server Error","url": url}

if __name__=="__main__":
    print(HongshuParser("https%3A%2F%2Fwww.xiaohongshu.com%2Fdiscovery%2Fitem%2F66dbbda2000000001e018d43%3Fsource%3Dwebshare%26xsec_token%3DABLd9dEnabx9iqDUHccv9g0T-KQKZC-aVMXCs_jeAEZiE%3D%26xsec_source%3Dpc_share"))

    