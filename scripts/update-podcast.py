from pathlib import Path
from bs4 import BeautifulSoup as S
R=Path(__file__).resolve().parents[1];p=R/'dist/podcast.html';s=S(p.read_text(),'html.parser')
im=s.select_one('.tp-banner-thumb img');im['src']='images/stock/podcast-microphone-2560.webp';im['srcset']=', '.join(f'images/stock/podcast-microphone-{w}.webp {w}w' for w in [640,1280,2560]);im['sizes']='100vw';im['alt']='Podcast microphone in front of an audio waveform';im['width']='2560';im['height']='1664';im['fetchpriority']='high';im['data-speed']='0.4'
# The heading wrapper already fades; avoid applying a second fade to its child.
n=s.select_one('.tp-breadcrumb-dec-wrap');n['class']=[x for x in n['class'] if x!='tp_fade_anim']
for src,tag in [('css/podcast.css?v=2','link'),('js/podcast.js?v=2','script')]:
 if not s.find(tag,attrs={'href' if tag=='link' else 'src':src}):
  (s.head if tag=='link' else s.body).append(S(f'<link rel="stylesheet" href="{src}">' if tag=='link' else f'<script src="{src}"></script>','html.parser'))
p.write_text(str(s))
