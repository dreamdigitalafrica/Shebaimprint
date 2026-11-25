from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image,ImageChops,ImageOps
R=Path(__file__).resolve().parents[1];D=R/'dist';P=D/'images/products'
for src in P.glob('*.webp'):
 if src.stem.endswith('-display'):continue
 im=Image.open(src).convert('RGB')
 delta=ImageChops.difference(im,Image.new('RGB',im.size,'white')).convert('L').point(lambda x:255 if x>24 else 0)
 box=delta.getbbox()
 if not box:continue
 crop=im.crop(box)
 canvas=Image.new('RGB',(880,798),'#f5f5f3')
 crop.thumbnail((748,694),Image.Resampling.LANCZOS)
 canvas.paste(crop,((880-crop.width)//2,(798-crop.height)//2))
 canvas.save(P/(src.stem+'-display.webp'),quality=88,method=6)
for p in D.glob('*.html'):
 s=BeautifulSoup(p.read_text(),'html.parser')
 if not s.select_one('.site-header'):continue
 changed=False
 for img in s.select('.shop-product-thumb img,.tp-product-details-nav-main-thumb img'):
  src=img.get('src','')
  if src.startswith('images/products/') and not src.endswith('-display.webp'):
   name=Path(src).stem+'-display.webp';img['src']='images/products/'+name;img['width']='880';img['height']='798';changed=True
 if changed:p.write_text(str(s))
