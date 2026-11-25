(() => {
 const gallery=document.querySelector('.spotlight-gallery');
 if(!gallery)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let paused=false,last=0,direction=1,frame;
 const pause=()=>{paused=true;};
 const resume=()=>{paused=false;last=0;};
 gallery.addEventListener('pointerenter',pause);
 gallery.addEventListener('pointerleave',resume);
 gallery.addEventListener('touchstart',pause,{passive:true});
 gallery.addEventListener('touchend',resume,{passive:true});
 gallery.addEventListener('focusin',pause);
 gallery.addEventListener('focusout',resume);
 function tick(now){
  const dt=last?Math.min(now-last,50):0;last=now;
  if(!paused&&!reduced.matches&&!document.hidden){
   const max=gallery.scrollWidth-gallery.clientWidth;
   if(max>0){
    if(innerWidth<=767){const slide=gallery.querySelector(".thumbs");const width=slide?.getBoundingClientRect().width||gallery.clientWidth;if(now-(gallery.dataset.lastSlide||0)>3200){gallery.scrollTo({left:Math.round(gallery.scrollLeft/width+1)*width,behavior:"smooth"});gallery.dataset.lastSlide=now;if(gallery.scrollLeft>=max-width)gallery.scrollTo({left:0,behavior:"smooth"});}}else gallery.scrollLeft+=direction*dt*.025;
    if(gallery.scrollLeft>=max-1)direction=-1;
    if(gallery.scrollLeft<=0)direction=1;
   }
  }
  frame=requestAnimationFrame(tick);
 }
 frame=requestAnimationFrame(tick);
 window.addEventListener('pagehide',()=>cancelAnimationFrame(frame));
 window.addEventListener('pageshow',e=>{if(e.persisted){last=0;frame=requestAnimationFrame(tick);}});
})();
