import bs4
import requests as req
import re


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def HongshuParser(url: str) -> dict:
    try:
        html = req.get(url, headers=headers)
        soup = bs4.BeautifulSoup(html.content.decode(),features="lxml")
        images = soup.find_all("meta",attrs={'name': "og:image"})
        descriptions = soup.find_all("meta",attrs={'name': "description"})
        url = re.findall(r'content="([^"\']*)"', str(images))
        description = re.findall(r'<meta content="(.*?)" name="description"', str(descriptions))[0]
        images = []
        for s in url:
            images.append("https://sns-img-hw.xhscdn.com/"+re.findall(r'/([^!/]+)!', s)[0] +"?imageView2/2/w/1080/format/png")

        return {"images": images, "description":description}
    except:
        return {"message": "Internal Server Error"}

if __name__=="__main__":
    print(HongshuParser("http://xhslink.com/oLlKSC"))

    