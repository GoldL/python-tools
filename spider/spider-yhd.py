import requests
from lxml import html

def spider(sn):
  """ 一号店数据 """
  url = 'https://search.yhd.com/c0-0/k{sn}/'.format(sn=sn)
  # 获取html内容
  html_data = requests.get(url).text
  # xpath对象
  selector = html.fromstring(html_data)

  ul_list = selector.xpath('//div[@id="itemSearchList"]/div')

  for li in ul_list:
    # 标题
    title = li.xpath('div/p[@class="proName clearfix"]/a/@title')
    print(title[0])

    # 链接
    link = li.xpath('div/p[@class="proName clearfix"]/a/@href')
    print(link[0])

    # 价格
    price = li.xpath('div/p[@class="proPrice"]/em/@yhdprice')
    print(price[0])
    
    # 商家
    store = li.xpath('div/p[@class="searh_shop_storeName storeName limit_width"]/a/@title')
    print(store[0])

if __name__ == "__main__":
      sn = '9787115428028'
      spider(sn)