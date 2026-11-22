from pathlib import Path
from bs4 import BeautifulSoup as S
R=Path(__file__).resolve().parents[1];D=R/'dist'
for p in D.glob('*.html'):
 s=S(p.read_text(),'html.parser')
 if not s.select_one('.site-header'):continue
 for n in s.select('.spotlight-label,.spotlight-background>span,.shop-cetagory-item span'):n.decompose()
 for n in s.select('.thumbs[title]'):del n['title']
 for n in s.select('h2'):
  if 'Sheba Imprint brings fitness' in n.get_text():
   for c in list(n.contents):
    if isinstance(c,str):c.replace_with('Move with purpose. Live with confidence. ')
 if not s.select_one('link[href="css/mobile-polish.css"]'):s.head.append(S('<link rel="stylesheet" href="css/mobile-polish.css">','html.parser'))
 p.write_text(str(s))
s=S((D/'about.html').read_text(),'html.parser')
t=S((R/'scripts/templates/about-me.html').read_text(),'html.parser').select_one('.about-me-area')
t.select_one('.tp-about-subtitle').string='About me';h=t.select_one('.pp-about-title');h.name='h1';h.string='I’m Faith Sheba Gamde, founder of Sheba Imprint.'
t.select_one('.pp-about-dec').string='I bring movement, wellbeing and community together through Fit is Lit, Lit Store and Sheba Care. My focus is simple: helping you build confidence and make room for the life you want to live.'
b=t.select_one('.pp-about-btn');b.clear();b.append(S('<a class="tp-btn" href="mailto:Shebasimprint@gmail.com">Get in touch</a>','html.parser'))
s.main.clear();s.main.append(t);s.main.append(S('<div class="container pb-100"><img class="founder-landscape w-100" src="images/brand/founder-landscape.webp" alt="Faith Sheba Gamde" width="1672" height="941" decoding="async" srcset="images/brand/founder-landscape-640.webp 640w, images/brand/founder-landscape.webp 1672w" sizes="(max-width: 767px) 100vw, 1140px"></div>','html.parser'));s.title.string='About Me | Faith Sheba Gamde';s.body['class']=['sheba-theme','about-me-page'];(D/'about-me.html').write_text(str(s))
for name in ['about.html','about-us.html']:
 p=D/name;s=S(p.read_text(),'html.parser');h=s.find('h3',string='Faith Sheba Gamde')
 if h:h.string='';h.append(S('<a href="about-me.html">Faith Sheba Gamde</a>','html.parser'))
 p.write_text(str(s))
for name in ['index.html','home-preview.html']:
 p=D/name;s=S(p.read_text(),'html.parser')
 for img in s.select('.spotlight-background[data-index="0"] img,.thumbs[data-index="0"] img'):
  img.attrs.update({'src':'images/brand/founder-landscape.webp','width':'1672','height':'941','style':'object-position:50% 50%'})
  img.attrs.pop('data-src',None)
  img['srcset']='images/brand/founder-landscape-640.webp 640w, images/brand/founder-landscape.webp 1672w'
 a=s.select_one('.thumbs[data-index="0"]')
 if a:
  a['href']='about-me.html';a['aria-label']='Meet Sheba';a.img['alt']='Faith Sheba Gamde, founder of Sheba Imprint'
 p.write_text(str(s))
# Keep the supplied people untouched; extend only the presentation background.
for name in ['index.html','home-preview.html']:
 p=D/name;s=S(p.read_text(),'html.parser')
 for index,file,alt in [('0','sheba-original.png','Faith Sheba Gamde'),('2','community-original.jpg','Sheba community fitness session')]:
  for frame in s.select(f'.spotlight-background[data-index="{index}"],.thumbs[data-index="{index}"]'):
   frame['class']=list(dict.fromkeys(frame.get('class',[])+['original-photo-frame']))
   frame['style']=f"--photo-fill:url('/images/brand/{file}')"
   # Inline custom properties resolve relative to the stylesheet using them.
   img=frame.select_one('img')
   for attr in ['srcset','data-src','width','height']:img.attrs.pop(attr,None)
   img['src']=f'images/brand/{file}';img['alt']=alt;img['style']='object-fit:contain;object-position:center'
 p.write_text(str(s))
p=D/'about-me.html';s=S(p.read_text(),'html.parser');img=s.select_one('.founder-landscape')
for attr in ['srcset','width','height']:img.attrs.pop(attr,None)
img['src']='images/brand/sheba-original.png'
img['style']='object-fit:contain'
p.write_text(str(s))
# Natural landscape extensions replace the temporary blurred side fills.
for name in ['index.html','home-preview.html','about-me.html']:
 p=D/name;s=S(p.read_text(),'html.parser')
 for index,file in [('0','sheba-cafe-landscape.png'),('2','community-landscape.png')]:
  for frame in s.select(f'.spotlight-background[data-index="{index}"],.thumbs[data-index="{index}"]'):
   frame['class']=[c for c in frame.get('class',[]) if c!='original-photo-frame']+['landscape-photo-frame']
   frame.attrs.pop('style',None)
   img=frame.select_one('img');img['src']=f'images/brand/{file}';img['width']='1672';img['height']='941';img['style']='object-fit:contain;object-position:center'
 if name=='about-me.html':
  img=s.select_one('.founder-landscape');img['src']='images/brand/sheba-cafe-landscape.png';img['width']='1672';img['height']='941'
 p.write_text(str(s))
