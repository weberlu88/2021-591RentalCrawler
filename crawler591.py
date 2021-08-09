from bs4 import BeautifulSoup
import requests

def writefile(url):
    '''write into md like format'''
    f = open("591房屋資訊.txt", "w+")
    f.write(title + "\n")
    f.write("\t* " + price + "\n")
    f.write("\t* " + explain + "\n")
    for a in attrlist:
        f.write("\t* " + a + "\n")
    f.close()

if __name__ == "__main__":
    url = input("Please enter 591 rental's URL: ") 
    
    # url = "https://rent.591.com.tw/rent-detail-10218171.html"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    # print(soup)

    housetitle = soup.select('span.houseInfoTitle')[0].text

    print(housetitle)

    detailinfo = soup.select('div.detailInfo.clearfix')[0]
    price = detailinfo.select('div.price.clearfix')[0].text.strip()
    explain = detailinfo.select('div.explain')[0].text.strip()
    attr = detailinfo.select('li')
    attrlist = [i.text.replace('\xa0', '') for i in attr]
    # print(detailinfo, price, explain, attrlist)

    title = f"[{housetitle}]({url})"
    # print(title)

    writefile(url) # write into md like format
