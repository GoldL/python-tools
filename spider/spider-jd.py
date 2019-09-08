import requests
from lxml import html

def spider(sn):
  """ 京东数据 """
  url = 'https://search.jd.com/Search'
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
    'Referer': 'https://www.jd.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
    }

  params = (
    ('keyword', sn),
    ('enc', 'utf-8'),
    ('wq', '1000x'),
    ('pvid', '70b2126fcf3246ce9f32710d41799ede'),
  )
  # 获取html内容
  resp = requests.get(url, headers=headers, params=params)
  resp.encoding = 'utf-8'
  html_doc = resp.text
  # xpath对象
  selector = html.fromstring(html_doc)
  
  ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')

  for li in ul_list:
    
    # 标题
    title = li.xpath('div/div[@class="p-name"]/a/em/text()')
    print(title[0])

    # 链接
    link = li.xpath('div/div[@class="p-img"]/a/@href')

  # 价格
    price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
    print(price[0])

    # 商家
    store = li.xpath('div/div[@class="p-shopnum"]/a/@title')
    print(store[0])
  
if __name__ == "__main__":
  sn = '9787115428028'
  spider(sn)