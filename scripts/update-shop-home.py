from pathlib import Path
from bs4 import BeautifulSoup as S
R=Path(__file__).resolve().parents[1];D=R/'dist'
T=R/'scripts/templates/shop-home.html'
s=S(T.read_text(),'html.parser');old=S((D/'shop.html').read_text(),'html.parser')
# Retain the working merchandise cards and their cart behavior.
cards=old.select('#shop-grid > [data-product-card]')
if not cards: raise RuntimeError('Shop product cards not found')
main=s.main
for selector in ['.shop-testimonial-area','.shop-related-product-area','.shop-payment-area','.shop-text-slider','.shop-ins-area']:
 for n in main.select(selector): n.decompose()
hero=[('Activewear','Made for your next move.','activewear','gym-tights.html'),('Find your rhythm','Essentials for an active day.','rope','gym-workout-top.html'),('Everyday movement','Discover Lit Store.','tennis','#shop-grid')]
for i,(item,(title,desc,photo,url)) in enumerate(zip(main.select('.shop-hero-item'),hero)):
 item.h2.name='h1' if i==0 else 'h2';item.select_one('.shop-hero-title a').string=title;item.p.string=desc
 for a in item.select('a'): a['href']=url
 for n in item.select('.text-1,.text-2'): n.string='Shop now'
 im=item.img;im['src']=f'images/stock/{photo}-2560.webp';im['alt']=title;im['width']=1856 if i==2 else 918;im['height']=750
 im['fetchpriority']='high' if i==0 else 'auto'
for item,(title,desc,url) in zip(main.select('.shop-service-item'),[('Activewear','Tights and tops for your workout wardrobe.','gym-tights.html'),('Footwear','Find your next pair.','running-shoes.html'),('Accessories','Keep your everyday essentials close.','sports-water-bottle.html')]):
 item.h3.string=title;item.p.string=desc;item.a['href']=url
 for n in item.select('a i'): n.decompose()
 for n in item.select('.text-1,.text-2'): n.string='View product'
area=main.select_one('.shop-product-area');area.clear();area.append(S('<div class="container"><h2 class="tp-section-title mb-50">Lit Store</h2><div class="row" id="shop-grid"></div><p class="store-note">Checkout is a preview. No payment is taken.</p></div>','html.parser'))
for card in cards: area.select_one('#shop-grid').append(card)
main.select_one('.shop-product-bigtext').string='Lit Store'
for item,(label,photo,url) in zip(main.select('.shop-cetagory-item'),[('Activewear','activewear','gym-tights.html'),('Movement','yoga','services.html'),('Community','outdoors','sheba-care.html')]):
 item.img['src']=f'images/stock/{photo}-1280.webp';item.img['alt']=label;item.img['loading']='lazy';item.span.string=label
 a=S(f'<a href="{url}"></a>','html.parser').a
 for c in list(item.contents):a.append(c.extract())
 item.append(a)
old.main.replace_with(main);old.body['class']=['sheba-theme','shop-home-page']
for name in ['shop.html','shop-list.html']:(D/name).write_text(str(old))
for p in D.glob('*.html'):
 doc=S(p.read_text(),'html.parser');nav=doc.select_one('#site-navigation')
 if not nav:continue
 if not nav.select_one('a[href="/shop.html"]'):
  a=S('<a href="/shop.html">Lit Store</a>','html.parser').a;nav.select_one('a[href="/fit-is-lit.html"]').insert_after(a)
 for n in doc.select('.tp-pd-2-categories'):n.decompose()
 p.write_text(str(doc))
