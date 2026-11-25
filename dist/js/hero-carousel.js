(() => {
 const gallery=document.querySelector('.spotlight-gallery');
 if(!gallery)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let last=0,paused=false,frame;
 const pause=()=>paused=true;
 const resume=()=>{paused=false;last=0};
 gallery.addEventListener('pointerenter',pause);
 gallery.addEventListener('pointerleave',resume);
 gallery.addEventListener('touchstart',pause,{passive:true});
 gallery.addEventListener('touchend',resume,{passive:true});
 gallery.addEventListener('focusin',pause);
 gallery.addEventListener('focusout',resume);
 const originals=[...gallery.children];
 originals.forEach(item=>{const clone=item.cloneNode(true);clone.setAttribute('aria-hidden','true');clone.removeAttribute('href');clone.setAttribute('tabindex','-1');gallery.append(clone)});
 function tick(now){
  const dt=last?Math.min(now-last,50):0;last=now;
  if(!paused&&!reduced.matches&&!document.hidden){
   const loop=gallery.scrollWidth/2;
   if(loop>gallery.clientWidth){gallery.scrollLeft+=dt*.045;if(gallery.scrollLeft>=loop)gallery.scrollLeft-=loop}
  }
  frame=requestAnimationFrame(tick);
 }
 frame=requestAnimationFrame(tick);
 window.addEventListener('pagehide',()=>cancelAnimationFrame(frame));
 window.addEventListener('pageshow',e=>{if(e.persisted){last=0;frame=requestAnimationFrame(tick)}});
})();
