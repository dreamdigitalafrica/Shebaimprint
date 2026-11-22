/* Complete the blog-list image reveal without requiring the theme's global smooth scroller. */
(() => {
  if (!window.gsap || !window.ScrollTrigger || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const banner = document.querySelector('.podcast-page .tp-banner-thumb');
  if (!banner) return;
  gsap.fromTo(banner.querySelector('img'), {yPercent:-4}, {yPercent:4,ease:'none',scrollTrigger:{trigger:banner,start:'top bottom',end:'bottom top',scrub:1}});
  // Fonts and responsive images can change section positions after initial parsing.
  const refresh = () => ScrollTrigger.refresh();
  if (document.fonts) document.fonts.ready.then(refresh);
  document.querySelectorAll('main img').forEach(img => {if (!img.complete) img.addEventListener('load',refresh,{once:true});});
})();
