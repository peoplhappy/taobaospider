from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from taobaoscrapy import Item
from scrapy_splash import SplashRequest
from taobaoscrapy import urlcode
from scrapy.http import Request
from selenium import webdriver
import bs4

class taobao_spider(CrawlSpider):
    name = 'taobaospider'
    items={}
    maxpage=5
    allowed_domains = ['taobao.com','detail.tmall.com']
    #start_urls = ['https://s.taobao.com/'+"search?q="+"最终幻想15"]
    #q=urlcode.encode("最终幻想15", "utf-8")
    start_urls=['https://s.taobao.com/search?q=最终幻想15']
    rules = [Rule(LinkExtractor(allow=['item.htm']), 'item_parser')]
    chrome_option = webdriver.ChromeOptions();
    chrome_option.add_argument("--headless")
    def start_requests(self):
        for i in range(self.maxpage):
            url=self.start_urls[0]+"&s="+str(44*i)
            yield Request(url=url, callback=self.parser)

    def parser(self, response):
        driverpath = "D:/Downloads/chromedriver_win32/chromedriver.exe"
        driver = webdriver.Chrome(driverpath,chrome_options=self.chrome_option)
        driver.get(response.url)
        driver.implicitly_wait(30)
        driver.refresh()
        driver.implicitly_wait(30)
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "lxml")
        shopurllist=soup.select("div.J_MouserOnverReq")
        for i in range(len(shopurllist)):
            shopurl=shopurllist[i].div.div.div.a["href"].replace(' ', '')
            #shopname=shopurllist[i].select("div.shop a span:nth-of-type(5)")[0].text

            if not shopurl.startswith("https"):
                shopurl="https:"+shopurl
                self.items[shopurl] = Item.taobaoscrapyItem()
                self.items[shopurl]["shopname"] = shopurllist[i].select_one("div.shop a span:nth-of-type(5)").string
                self.items[shopurl]["pricelist"] = shopurllist[i].select_one("div:nth-of-type(8) strong").string
                self.items[shopurl]["goodsname"] = shopurllist[i].select_one("div:nth-of-type(11) a").text
                self.items[shopurl]["totalsells"] = shopurllist[i].select_one("div:nth-of-type(9)").string.replace(
                    "人付款", "")
            else:
                self.items[shopurl] = Item.taobaoscrapyItem()
                self.items[shopurl]["shopname"] = shopurllist[i].select_one("div.shop a span:nth-of-type(5)").string
                self.items[shopurl]["pricelist"] = shopurllist[i].select_one("div:nth-of-type(7) strong").string
                self.items[shopurl]["goodsname"] = shopurllist[i].select_one("div:nth-of-type(10) a").text
                self.items[shopurl]["totalsells"] = shopurllist[i].select_one("div:nth-of-type(8)").string.replace(
                    "人付款", "")
            yield Request(url=shopurl,callback=self.item_parse)
        driver.close()

    def item_parse(self,response):
        url=response.url
        if response.url.startswith("https://item"):
            url=response.url+"#detail"
        item = self.items[url]
        driverpath = "D:/Downloads/chromedriver_win32/chromedriver.exe"
        driver = webdriver.Chrome(driverpath, chrome_options=self.chrome_option)
        driver.get(response.url)
        driver.implicitly_wait(30)
        driver.refresh()
        driver.implicitly_wait(30)
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "lxml")
        item["shopurl"]=response.url
        monthsell=soup.select_one("#J_DetailMeta > div.tm-clear > div.tb-property > div > ul > li.tm-ind-item.tm-ind-sellCount > div > span.tm-count")
        if monthsell:
            item['lastmonthsells']=monthsell.string
        else:
            item['lastmonthsells']=0
        rated1=soup.select_one("#J_ShopInfo > div > div.tb-shop-info-bd > div > dl:nth-of-type(1) > dd > a ")
        rated2=soup.select_one("#shop-info > div.main-info > div:nth-of-type(1) > div.shopdsr-score.shopdsr-score-up-ctrl > span")
        if rated1:
            item['rated']=rated1.string
        elif rated2:
            item['rated']=rated2.string
        else:
            item['rated'] =0
        driver.close()
        yield item
