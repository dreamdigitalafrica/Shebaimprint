from pathlib import Path
from bs4 import BeautifulSoup as S
R=Path(__file__).resolve().parents[1];D=R/'dist'
s=S((R/'scripts/templates/about-us.html').read_text(),'html.parser')
d=S((D/'shop.html').read_text(),'html.parser'); main=s.main
for n in list(main.find_all(recursive=False)):
 if not set(n.get('class',[])) & {'about-us-area','about-me-slider-area','tp-about-area'}:n.decompose()
t=main.select_one('.about-us-title');t.name='h1';t.string='Movement. Confidence. Community.'
for n in main.select('.about-me-slider-awards'):n.decompose()
for i,im in enumerate(main.select('.about-me-slider-thumb img')):
 im['src']='images/stock/'+['community','stretch','outdoors'][i%3]+'-1280.webp';im['alt']=['Move together','Everyday movement','Connect with your community'][i%3];im['loading']='lazy'
main.select_one('.tp-section-title').string='Make your mark. Live with purpose.'
for item,(title,copy,src) in zip(main.select('.tp-about-item'),[
 ('Sheba Imprint','Movement, wellbeing and community. Through Fit is Lit, Lit Store and Sheba Care, we create space to grow.','images/stock/community-1280.webp'),
 ('Faith Sheba Gamde','Founder of Sheba Imprint and Fit is Lit. Helping you build confidence through movement and consistent everyday habits.','images/fitislit/sheba-founder.jpg')]):
 item.h3.string=title;item.p.string=copy;item.img['src']=src;item.img['alt']=title;item.img['loading']='lazy'
main['id']='main-content';d.main.replace_with(main);d.body['class']=['sheba-theme','sheba-about-page'];d.title.string='About Us | Sheba Imprint'
d.select_one('meta[name="description"]')['content']='Meet Sheba Imprint and founder Faith Sheba Gamde. Movement, wellbeing and community.'
d.head.append(S('<link rel="stylesheet" href="cunnet-assets/css/swiper-bundle.css">','html.parser'))
for src in ['cunnet-assets/js/swiper-bundle.js','js/sheba-about.js']:d.body.append(S(f'<script src="{src}" defer></script>','html.parser'))
for name in ['about.html','about-us.html']:(D/name).write_text(str(d))
