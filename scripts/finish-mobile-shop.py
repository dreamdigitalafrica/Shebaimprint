from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image,ImageChops,ImageOps
R=Path(__file__).resolve().parents[1];D=R/'dist';P=D/'images/products'
for src in P.glob('*.webp'):
 if src.stem.endswith('-display'):continue
 im=Image.open(src).convert('RGB')
 # The supplied photos sit on near-white backgrounds. Detect the product,
 # allowing for small WebP variations in the white pixels around it.
 delta=im.convert('L').point(lambda x:255 if x<225 else 0)
 box=delta.getbbox()
 if not box:continue
 margin=max(8,round(min(im.size)*.025))
 box=(max(0,box[0]-margin),max(0,box[1]-margin),min(im.width,box[2]+margin),min(im.height,box[3]+margin))
 crop=im.crop(box)
 canvas=Image.new('RGB',(880,798),'#f5f5f3')
 crop=ImageOps.contain(crop,(792,718),Image.Resampling.LANCZOS)
 # Fade the photographed white backdrop into the card background. Product
 # colours remain intact, while no white rectangle surrounds the crop.
 alpha=ImageChops.difference(crop,Image.new('RGB',crop.size,'white')).convert('L')
 alpha=alpha.point(lambda x:0 if x<6 else 255 if x>28 else round((x-6)*255/22))
 canvas.paste(crop,((880-crop.width)//2,(798-crop.height)//2),alpha)
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
