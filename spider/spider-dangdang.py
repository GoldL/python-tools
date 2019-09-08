import requests
from lxml import html

def spider(sn):
  """ 当当网数据 """
  url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)
  # 获取html内容
  html_data = requests.get(url).text
  # xpath对象
  selector = html.fromstring(html_data)

  ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')

  for li in ul_list:
    # 标题
    title = li.xpath('a/@title')
    print(title[0])

    # 链接
    link = li.xpath('a/@href')
    print(link[0])

    # 价格
    price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
    print(price[0].replace('¥', ''))
    
    # 商家
    store = li.xpath('p[@class="search_shangjia"]/a/@title')
    store = '当当自营' if len(store) == 0 else store[0]
    print(store)

if __name__ == "__main__":
      sn = '9787115428028'
      spider(sn)