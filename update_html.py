import re

with open('index.html', 'r') as f:
    content = f.read()

# Add image data to work items and enhance HTML structure for hover images
html_replacements = [
    (r'<a href="#" class="work-item">', r'<a href="#" class="work-item" data-img="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1000&auto=format&fit=crop">'),
    (r'<a href="#" class="work-item">\s*<div class="work-item-left">\s*<span class="work-idx">02</span>', r'<a href="#" class="work-item" data-img="https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?q=80&w=1000&auto=format&fit=crop">\n        <div class="work-item-left">\n          <span class="work-idx">02</span>'),
    (r'<a href="#" class="work-item">\s*<div class="work-item-left">\s*<span class="work-idx">03</span>', r'<a href="#" class="work-item" data-img="https://images.unsplash.com/photo-1614729939124-03290b56c9ce?q=80&w=1000&auto=format&fit=crop">\n        <div class="work-item-left">\n          <span class="work-idx">03</span>'),
    (r'<a href="#" class="work-item">\s*<div class="work-item-left">\s*<span class="work-idx">04</span>', r'<a href="#" class="work-item" data-img="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop">\n        <div class="work-item-left">\n          <span class="work-idx">04</span>'),
    (r'<a href="#" class="work-item">\s*<div class="work-item-left">\s*<span class="work-idx">05</span>', r'<a href="#" class="work-item" data-img="https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1000&auto=format&fit=crop">\n        <div class="work-item-left">\n          <span class="work-idx">05</span>')
]

for old, new in html_replacements:
    content = re.sub(old, new, content)

# Add hover image container
content = content.replace('</main>', '<div class="hover-image-reveal" id="hover-image"></div>\n</main>')


# CSS Updates
css_additions = """
  /* --- Enhancements --- */
  :root {
    --accent: #ff4d00;
  }

  /* Cursor */
  .cursor {
    width: 12px; height: 12px;
    background: var(--text-dark);
    mix-blend-mode: difference;
    transition: width 0.3s ease, height 0.3s ease, background 0.3s ease, transform 0.1s linear;
    z-index: 9999;
  }
  .cursor.hover {
    width: 60px; height: 60px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255,255,255,0.5);
    mix-blend-mode: normal;
  }
  .light-mode .cursor { background: var(--text-light); }
  .light-mode .cursor.hover { background: rgba(0,0,0,0.1); border-color: rgba(0,0,0,0.5); }

  /* Background transition */
  body {
    transition: background-color 1s cubic-bezier(0.77, 0, 0.175, 1), color 0.8s ease;
  }

  /* Text Highlights & Accents */
  em {
    color: var(--accent) !important;
    font-style: italic;
    position: relative;
    display: inline-block;
  }

  .btn-primary {
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }
  .btn-primary:hover {
    background: #fff;
    color: var(--bg-dark);
    border-color: #fff;
  }
  .light-mode .btn-primary:hover {
    background: var(--bg-dark);
    color: #fff;
  }

  /* Work Item Hover Effects */
  .work-item {
    position: relative;
    transition: padding 0.5s cubic-bezier(0.19,1,0.22,1), opacity 0.5s ease;
    overflow: hidden;
  }
  .work-item::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: var(--text-dark);
    transform: scaleY(0);
    transform-origin: bottom;
    transition: transform 0.6s cubic-bezier(0.19,1,0.22,1);
    z-index: -1;
  }
  .light-mode .work-item::before { background: var(--text-light); }

  .work-item:hover {
    padding-left: 30px;
    padding-right: 30px;
    opacity: 1 !important;
  }
  .work-list:hover .work-item:not(:hover) {
    opacity: 0.3 !important;
  }
  .work-item:hover::before {
    transform: scaleY(1);
    transform-origin: top;
  }
  .work-item:hover .work-idx,
  .work-item:hover .work-name,
  .work-item:hover .work-cat {
    color: var(--bg-dark);
  }
  .light-mode .work-item:hover .work-idx,
  .light-mode .work-item:hover .work-name,
  .light-mode .work-item:hover .work-cat {
    color: var(--bg-light);
  }

  .work-name {
    transition: color 0.3s ease, transform 0.5s cubic-bezier(0.19,1,0.22,1);
  }
  .work-item:hover .work-name {
    transform: translateX(20px) skewX(-2deg);
  }

  /* Hover Image Reveal */
  .hover-image-reveal {
    position: fixed;
    top: 50%; left: 50%;
    width: 350px; height: 450px;
    transform: translate(-50%, -50%) scale(0.8) rotate(-5deg);
    pointer-events: none;
    opacity: 0;
    z-index: 0;
    background-size: cover;
    background-position: center;
    transition: opacity 0.4s ease, transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
    border-radius: 4px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
  }
  .hover-image-reveal.active {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1) rotate(0deg);
  }

  /* Initial state for SplitText words to add rotation */
  .split-line {
    overflow: hidden;
    padding-bottom: 0.1em;
  }
  .word {
    transform-origin: bottom center;
  }
"""

content = content.replace('</style>', css_additions + '\n</style>')

# JS Updates
js_additions = """
  // Work items image reveal
  const hoverImage = document.getElementById('hover-image');
  const workItems = document.querySelectorAll('.work-item');
  let revealX = window.innerWidth/2, revealY = window.innerHeight/2;

  if (window.matchMedia('(pointer: fine)').matches) {
      document.addEventListener('mousemove', (e) => {
          revealX = e.clientX;
          revealY = e.clientY;
          if(hoverImage.classList.contains('active')) {
             gsap.to(hoverImage, {
                 x: revealX - hoverImage.offsetWidth/2,
                 y: revealY - hoverImage.offsetHeight/2,
                 duration: 0.8,
                 ease: 'power3.out'
             });
          }
      });

      workItems.forEach(item => {
          item.addEventListener('mouseenter', (e) => {
              const imgUrl = item.getAttribute('data-img');
              if(imgUrl) {
                  hoverImage.style.backgroundImage = `url(${imgUrl})`;
                  hoverImage.classList.add('active');
                  // Set initial position immediately
                  gsap.set(hoverImage, {
                      x: e.clientX - hoverImage.offsetWidth/2,
                      y: e.clientY - hoverImage.offsetHeight/2,
                      rotation: Math.random() * 10 - 5
                  });
              }
          });
          item.addEventListener('mouseleave', () => {
              hoverImage.classList.remove('active');
          });
      });
  }

  // Enhanced initial animation with rotation and opacity
  function initHeroAnimations() {
    const tl = gsap.timeline();
    // Words come up from bottom with a slight rotation and opacity fade
    tl.fromTo('#s1 .word',
        { y: 100, rotationZ: 10, opacity: 0 },
        { y: 0, rotationZ: 0, opacity: 1, duration: 1.4, stagger: 0.04, ease: 'power4.out' }
      )
      .fromTo('#s1 .anim-up',
        { y: 40, opacity: 0 },
        { y: 0, opacity: 1, duration: 1.2, stagger: 0.1, ease: 'power3.out' },
        '-=1.0'
      );
  }
"""

# Replace initHeroAnimations definition and add image logic
content = re.sub(
    r'function initHeroAnimations\(\) \{.*?\n\s*\}',
    js_additions,
    content,
    flags=re.DOTALL
)

# Update the scroll trigger content reveal to use enhanced effects
enhanced_scroll = """
    // Content Reveal (Enhanced)
    if(scene.id !== 's1') {
      const words = scene.querySelectorAll('.word');
      if(words.length) {
        gsap.fromTo(words,
          { y: 100, rotationZ: 8, opacity: 0 },
          {
            scrollTrigger: { trigger: scene, start: 'top 80%' },
            y: 0, rotationZ: 0, opacity: 1, duration: 1.2, stagger: 0.03, ease: 'power4.out'
          }
        );
      }
      const ups = scene.querySelectorAll('.anim-up, .work-item');
      if(ups.length) {
        gsap.fromTo(ups, { y: 50, opacity: 0 }, {
          scrollTrigger: { trigger: scene, start: 'top 85%' },
          y: 0, opacity: 1, duration: 1.2, stagger: 0.1, ease: 'power3.out'
        });
      }
    }
"""

content = re.sub(
    r'// Content Reveal\n.*?if\(scene\.id !== \'s1\'\) \{.*?\n\s*\}\n\s*\}',
    enhanced_scroll,
    content,
    flags=re.DOTALL
)


with open('index.html', 'w') as f:
    f.write(content)
