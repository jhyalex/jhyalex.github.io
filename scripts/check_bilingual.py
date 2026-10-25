from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote,urljoin
import json,re,hashlib,xml.etree.ElementTree as ET
import sys
SRC=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else SRC/'_site')
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=[];self.lang=None;self.data=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a':self.links.append(a)
 def handle_data(self,d):self.data.append(d)
keys=json.loads((SRC/'_data/translation_keys.json').read_text())
assert len(keys)==len(list((SRC/'_posts').glob('*.md')))
assert len(set(keys.values()))==len(keys)
for p,k in keys.items():
 d=json.loads((SRC/'_data/en'/f'{k}.json').read_text());assert all(d[v].strip() for v in ['title','subtitle','body'])
 en=ROOT/f'en/posts/{k}/index.html';assert en.exists(),en
 page=Page(en.read_text());assert page.lang=='en'
 assert d['title'] in ''.join(page.data)
 assert len(d['body'])>80
 zhlink=next(a['href'] for a in page.links if a.get('data-language')=='zh')
 zh=ROOT/unquote(urlsplit(zhlink).path).strip('/')/'index.html';assert zh.exists(),zh
 z=Page(zh.read_text());assert z.lang=='zh-CN'
 assert next(a['href'] for a in z.links if a.get('data-language')=='en')==f'/en/posts/{k}/'
 assert not [i for i in page.ids if page.ids.count(i)>1],en
assert 'loafing' in (ROOT/'en/posts/2025-08-30/index.html').read_text()
assert 'swinging my arms' not in (ROOT/'en/posts/2025-08-30/index.html').read_text()
broken=[]
for p in ROOT.rglob('*.html'):
 rel='/'+p.relative_to(ROOT).as_posix().removesuffix('index.html')
 for a in Page(p.read_text()).links:
  href=a.get('href','');u=urlsplit(urljoin(rel,href))
  if u.scheme or u.netloc or not href:continue
  target=ROOT/unquote(u.path).lstrip('/')
  if u.path.endswith('/'):target=target/'index.html'
  elif not target.exists() and not target.suffix:target=target/'index.html'
  if not target.exists():broken.append((str(p.relative_to(ROOT)),href))
for p in ['feed.xml','en/feed.xml']:ET.parse(ROOT/p)
print(json.dumps({'translated_articles':len(keys),'reciprocal_language_links':True,'rss_valid':True,'broken_internal_links':broken},ensure_ascii=False,indent=2))
assert not broken
