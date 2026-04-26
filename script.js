// Navbar scroll
const navbar=document.querySelector('.navbar');
window.addEventListener('scroll',()=>{navbar.classList.toggle('scrolled',window.scrollY>50)});

// Mobile menu
const hamburger=document.querySelector('.hamburger'),navLinks=document.querySelector('.nav-links');
hamburger.addEventListener('click',()=>{
  navLinks.classList.toggle('open');
  const s=hamburger.querySelectorAll('span');
  if(navLinks.classList.contains('open')){s[0].style.transform='rotate(45deg) translate(5px,5px)';s[1].style.opacity='0';s[2].style.transform='rotate(-45deg) translate(5px,-5px)'}
  else{s[0].style.transform='';s[1].style.opacity='';s[2].style.transform=''}
});
navLinks.querySelectorAll('a').forEach(l=>l.addEventListener('click',()=>{navLinks.classList.remove('open');hamburger.querySelectorAll('span').forEach(s=>{s.style.transform='';s.style.opacity=''})}));

// Active link
const sections=document.querySelectorAll('.section[id]'),navA=document.querySelectorAll('.nav-links a');
window.addEventListener('scroll',()=>{const y=window.scrollY+120;sections.forEach(s=>{const t=s.offsetTop,h=s.offsetHeight,id=s.getAttribute('id');if(y>=t&&y<t+h){navA.forEach(a=>a.classList.remove('active'));const a=document.querySelector(`.nav-links a[href="#${id}"]`);if(a)a.classList.add('active')}})});

// Scroll reveal
const obs=new IntersectionObserver(e=>{e.forEach(en=>{if(en.isIntersecting)en.target.classList.add('visible')})},{threshold:.1,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.fade-up').forEach(el=>obs.observe(el));

// Counter
const cObs=new IntersectionObserver(e=>{e.forEach(en=>{if(en.isIntersecting){const el=en.target,t=parseInt(el.dataset.count),su=el.dataset.suffix||'';let c=0;const st=Math.max(1,Math.floor(t/60)),ti=setInterval(()=>{c+=st;if(c>=t){c=t;clearInterval(ti)}el.textContent=c+su},25);cObs.unobserve(el)}})},{threshold:.5});
document.querySelectorAll('.stat-number[data-count]').forEach(el=>cObs.observe(el));

// Domain tabs
document.querySelectorAll('.domain-tab').forEach(tab=>{
  tab.addEventListener('click',()=>{
    document.querySelectorAll('.domain-tab').forEach(t=>t.classList.remove('active'));
    document.querySelectorAll('.domain-panel').forEach(p=>p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.target).classList.add('active');
  });
});

// Scroll to top
const scrollBtn=document.querySelector('.scroll-top');
window.addEventListener('scroll',()=>{scrollBtn.classList.toggle('show',window.scrollY>400)});
scrollBtn.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));

// Contact form — calls Vercel serverless function
const form=document.getElementById('contactForm');
if(form){
  form.addEventListener('submit',async(e)=>{
    e.preventDefault();
    const btn=form.querySelector('.form-submit');
    const msg=document.getElementById('formMsg');
    btn.disabled=true;btn.textContent='Sending...';msg.textContent='';msg.className='form-msg';
    const name=form.querySelector('#fname').value+' '+form.querySelector('#lname').value;
    const email=form.querySelector('#email').value;
    const message=form.querySelector('#message').value;
    try{
      const res=await fetch('/api/contact',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({name,email,message})
      });
      const data=await res.json();
      if(res.ok){msg.textContent='Message sent successfully!';msg.className='form-msg success';form.reset()}
      else{msg.textContent=data.error||'Failed to send. Try again.';msg.className='form-msg error'}
    }catch(err){msg.textContent='Network error. Please try again.';msg.className='form-msg error'}
    btn.disabled=false;btn.textContent='Send Message';
  });
}
