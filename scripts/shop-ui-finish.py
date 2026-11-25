from pathlib import Path
from bs4 import BeautifulSoup as S
R=Path(__file__).resolve().parents[1];D=R/'dist'
for p in D.glob('*.html'):
 s=S(p.read_text(),'html.parser')
 header=s.select_one('.site-header-inner')
 if not header:continue
 if not header.select_one('.site-header-actions'):
  menu=header.select_one('.site-menu')
  wrap=S('<div class="site-header-actions"><a class="site-cart-link" href="/cart.html" aria-label="View cart"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 8h16l-1 12H5L4 8Z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg><span data-cart-count>0</span></a></div>','html.parser').div
  menu.wrap(wrap);wrap.insert(0,wrap.find(class_='site-cart-link'))
 if p.name in ('shop.html','shop-list.html'):
  grid=s.select_one('#shop-grid')
  if grid and not s.select_one('#product-sort'):
   toolbar=S('<div class="shop-sort-bar"><p>Explore our 4 products</p><label for="product-sort">Sort by</label><select id="product-sort" aria-label="Sort products"><option value="default">Default sorting</option><option value="low">Price: low to high</option><option value="high">Price: high to low</option><option value="name">Name: A to Z</option></select></div>','html.parser').div
   grid.insert_before(toolbar)
 p.write_text(str(s))
