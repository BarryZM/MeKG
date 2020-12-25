from util.pg_connection import new_connection
from scrapy_cerebrovascular.scrapy_html import ScrapyHtml

engine, session = new_connection()
sh = ScrapyHtml(engine, session)
sh.translate()
print('translate succeed !')
