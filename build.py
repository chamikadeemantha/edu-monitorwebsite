
h = open("index.html","w",encoding="utf-8")
h.write("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>EduMonitor | Real-Time Student &amp; Teacher Performance Monitoring</title>
<link rel="stylesheet" href="styles.css"/><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/></head><body>
<nav class="navbar"><div class="container nav-inner"><a href="#" class="nav-logo">Edu<span>Monitor</span></a>
<ul class="nav-links"><li><a href="#home" class="active">Home</a></li><li><a href="#research">Research</a></li><li><a href="#domain">Domain</a></li><li><a href="#milestones">Milestones</a></li><li><a href="#downloads">Downloads</a></li><li><a href="#publications">Publications</a></li><li><a href="#team">Team</a></li><li><a href="#contact">Contact</a></li></ul>
<button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button></div></nav>

<section class="hero section" id="home"><div class="container hero-content">
<div class="hero-badge"><span class="dot"></span> SLIIT Research Project 2025</div>
<h1>Real-Time Student &amp; Teacher <span class="hl">Performance Monitoring</span> System</h1>
<p>An AI-powered educational platform combining computer vision, NLP, and machine learning to monitor engagement, predict attendance, analyze teacher behavior, and provide real-time classroom support.</p>
<div class="hero-btns"><a href="#research" class="btn-primary"><i class="fas fa-microscope"></i> Explore Research</a><a href="#contact" class="btn-outline"><i class="fas fa-envelope"></i> Contact Us</a></div>
</div></section>

<section class="section" id="overview"><div class="container">
<div class="section-label fade-up">About The Project</div><h2 class="section-title fade-up">Project <span class="hl">Overview</span></h2>
<div class="overview-grid fade-up">
<div class="overview-text">
<p>EduMonitor is a comprehensive, AI-powered educational monitoring platform developed at the Sri Lanka Institute of Information Technology (SLIIT). The system addresses a critical gap in modern education — the lack of real-time, actionable insights into classroom dynamics.</p>
<p>Our platform integrates four specialized research components into a unified system: <strong>Student Engagement Detection</strong> using pose estimation and computer vision, <strong>Teacher Behavior Classification</strong> through movement tracking and spatial analysis, <strong>Attendance Factor Analysis</strong> using a validated psychometric survey instrument with machine learning predictions, and a <strong>RAG-based Classroom Support System</strong> for real-time question answering and lecture summarisation.</p>
<p>Built on a modern tech stack — FastAPI backend, Next.js frontend, and PostgreSQL database — EduMonitor processes classroom video feeds, survey data, and lecture content to deliver real-time analytics, predictions, and personalised recommendations to educators through an intuitive dashboard.</p>
</div>
<div class="overview-image fade-up"><img src="images/hero-bg.png" alt="EduMonitor System Overview"/></div>
</div></div></section>

<section class="section" id="research"><div class="container">
<div class="section-label fade-up">Our Research</div><h2 class="section-title fade-up">What <span class="hl">EduMonitor</span> Does</h2>
<p class="section-desc fade-up">Our system integrates four AI-powered components to create a comprehensive classroom analytics platform.</p>
<div class="research-grid">
<div class="glass-card fade-up"><div class="card-icon"><i class="fas fa-eye"></i></div><h3>Student Engagement Detection</h3><p>Real-time pose-based framework using YOLOv8-Pose and Random Forest classifiers for behavioral predictions.</p></div>
<div class="glass-card fade-up"><div class="card-icon"><i class="fas fa-chalkboard-teacher"></i></div><h3>Teacher Behavior Analysis</h3><p>Pose estimation and movement tracking to classify teacher instructional behaviors and classroom dynamics.</p></div>
<div class="glass-card fade-up"><div class="card-icon"><i class="fas fa-chart-line"></i></div><h3>Attendance Factor Analysis</h3><p>Validated six-factor survey instrument with Ridge Regression to predict and explain attendance patterns.</p></div>
<div class="glass-card fade-up"><div class="card-icon"><i class="fas fa-robot"></i></div><h3>RAG Classroom Support</h3><p>Dual-source RAG system for real-time Q&amp;A, lecture summarisation, and outcome-aligned assessment.</p></div>
</div></div></section>
""")

# Domain section with tabs
tabs = [
    ("Literature Survey","lit"),("Research Gap","gap"),("Research Problem","prob"),
    ("Research Objectives","obj"),("Methodology","meth"),("Technologies Used","tech")
]
members = [
    {"name":"Kisara W.C","id":"IT22582874","topic":"Student Engagement Detection","tag":"tag-purple",
     "lit":"Recent educational computer vision studies utilize pose estimation to analyze classroom actions while minimizing reliance on appearance-based cues. Deep learning models for behavior recognition often require high-performance GPUs and typically operate offline.",
     "gap":"Most approaches analyze student engagement and teacher behavior as completely separate domains, missing joint classroom dynamics. Existing systems lack the interpretability educators need.",
     "prob":"There is a critical lack of a practical, interpretable, and real-time framework capable of jointly analyzing both student behavioral engagement and teacher instructional behavior.",
     "obj":["Design a unified, pose-based framework for jointly monitoring teacher and student behaviors","Develop an interpretable feature engineering pipeline using geometric, kinematic, and spatial descriptors","Incorporate classroom-aware contextual modeling to improve system robustness","Support real-time, low-latency deployment on standard hardware"],
     "meth":"Real-time 17-point skeletal extraction using YOLOv8-Pose. OSNet-based deep re-identification for tracking. Extraction of 9 geometric features with lightweight Random Forest classifiers and temporal smoothing windows (~30 frames).",
     "tech":"Python 3.10, OpenCV, Ultralytics YOLOv8, Scikit-learn, FastAPI, Next.js, React, Tailwind CSS. Standard CPU-based edge-computing environment (Intel Core i5, 8 GB RAM)."},
    {"name":"De Silva A.R.S","id":"IT22586834","topic":"Teacher Behavior Classification","tag":"tag-cyan",
     "lit":"Research in spatial pedagogy highlights that teacher positioning, trajectory, and proximity are crucial for interpreting instructional interactions. Deep learning models often require high-performance GPUs.",
     "gap":"Existing systems heavily rely on computationally intensive architectures, limiting live deployment on standard hardware. End-to-end black-box models lack interpretability.",
     "prob":"There is a critical lack of a practical, interpretable, and real-time framework for analyzing teacher instructional behavior within physical classroom settings.",
     "obj":["Design a pose-based framework for monitoring teacher behaviors in physical classrooms","Develop an interpretable feature engineering pipeline using geometric and kinematic descriptors","Incorporate classroom-aware contextual modeling","Support real-time deployment on standard hardware with live visualization"],
     "meth":"YOLOv8-Pose for perception. OSNet-based deep re-identification for tracking. Dynamic temporal/kinematic feature extraction. Lightweight Random Forest classifiers with majority voting for stable predictions.",
     "tech":"Python 3.10, OpenCV, Ultralytics YOLOv8, Scikit-learn, FastAPI, Next.js, React, Tailwind CSS. Standard CPU-based environment (Intel Core i5, 8 GB RAM, Windows 10)."},
    {"name":"Deemantha P.H.H.C","id":"IT22560162","topic":"Attendance Factor Analysis","tag":"tag-blue",
     "lit":"Student lecture attendance is one of the strongest predictors of academic performance. However, most universities only record absence without understanding the reasons. ML techniques have been used but rely on administrative data rather than validated survey instruments.",
     "gap":"Most studies rely on single-factor analyses and do not use a validated multidimensional survey. ML models are rarely trained on factor-analytic scores linked to real attendance records. There is also a theory-practice gap in deployment.",
     "prob":"Universities can record absence but cannot explain why students are absent. The problem is to develop a validated survey instrument, predict attendance using ML, and deliver actionable recommendations through a live dashboard.",
     "obj":["Develop a real-time attendance prediction system using a validated six-factor survey instrument","Validate the instrument using Exploratory Factor Analysis on two independent datasets","Compare four regression models and deploy the best as an ML Insights Engine","Generate per-student factor-level natural-language recommendations"],
     "meth":"A 28-item Likert-scale survey covering six factor dimensions was designed and administered via Google Forms. Responses were linked to actual attendance records (n=115). EFA achieved KMO > 0.90. Ridge Regression was selected as best model (R² = 0.8643) and integrated into EduMonitor backend.",
     "tech":"Python, Scikit-learn, factor_analyzer, Pandas, NumPy, Matplotlib, Seaborn, FastAPI, Next.js 14 with TypeScript, PostgreSQL, Google Forms, Jupyter Notebook."},
    {"name":"Pallewela S.M","id":"IT22594136","topic":"RAG Classroom Support","tag":"tag-pink",
     "lit":"Recent studies show that Retrieval-Augmented Generation (RAG) improves accuracy of educational AI systems by grounding responses in external knowledge. However, most systems rely on static datasets and lack real-time classroom integration.",
     "gap":"Current educational AI systems do not effectively combine real-time lecture content with pre-prepared materials. Most solutions lack ability to reflect what is actually taught during live sessions.",
     "prob":"Students often experience knowledge gaps during live lectures due to missed explanations or varying learning speeds. Existing tools do not provide real-time support to address these gaps.",
     "obj":["Develop a real-time classroom support system for question answering and lecture summarisation","Align assessments with learning outcomes using Bloom's taxonomy","Provide analytics to identify student performance gaps"],
     "meth":"Dual-source RAG architecture combining teacher-provided materials and live speech-to-text transcripts. Content embedded using Sentence-BERT and stored in vector database. Fine-tuned LLM generates context-aware answers, summaries, and quiz questions.",
     "tech":"Llama-based language models, Sentence-BERT, Qdrant vector database, Faster-Whisper for speech-to-text, FastAPI backend, Next.js frontend."}
]

h.write('<section class="section" id="domain" style="background:var(--bg2)"><div class="container">\n')
h.write('<div class="section-label fade-up">Domain</div><h2 class="section-title fade-up">Individual <span class="hl">Research Domains</span></h2>\n')
h.write('<p class="section-desc fade-up">Each team member contributes a specialized AI component to the unified EduMonitor platform.</p>\n')
h.write('<div class="domain-tabs fade-up">')
for i,t in enumerate(tabs):
    ac=' active' if i==0 else ''
    h.write(f'<button class="domain-tab{ac}" data-target="panel-{t[1]}">{t[0]}</button>')
h.write('</div>\n')

for ti,t in enumerate(tabs):
    ac=' active' if ti==0 else ''
    h.write(f'<div class="domain-panel{ac}" id="panel-{t[1]}"><div class="domain-cards">\n')
    for m in members:
        h.write(f'<div class="d-card fade-up"><span class="d-tag {m["tag"]}">{m["id"]}</span>')
        h.write(f'<div class="d-member">{m["name"]}</div><h3>{m["topic"]}</h3>')
        key = t[1]
        if key=="obj":
            h.write('<ul>')
            for o in m[key]: h.write(f'<li>{o}</li>')
            h.write('</ul>')
        else:
            h.write(f'<p>{m[key]}</p>')
        h.write('</div>\n')
    h.write('</div></div>\n')
h.write('</div></section>\n')

# Milestones
ms = [
    ("September 2025","Project Proposal","Initial research proposal defining research problems, objectives, and scope for all four components.",6,30,"fa-file-alt"),
    ("December 2025","Progress Presentation I","Comprehensive literature surveys, identified research gaps, and detailed the initial methodology for each system component.",12,60,"fa-chart-bar"),
    ("March 2026","Progress Presentation II","Demonstrated implementation progress, presented model training results, and showcased performance evaluation of each AI module.",12,60,"fa-code"),
    ("April 2026","Final Presentation &amp; Viva","Final dissertations, comprehensive system presentations, and viva defense with complete integrated platform demonstration.",20,100,"fa-graduation-cap")
]
h.write('<section class="section" id="milestones"><div class="container">\n')
h.write('<div class="section-label fade-up" style="text-align:center">Timeline</div><h2 class="section-title fade-up" style="text-align:center">Research <span class="hl">Milestones</span></h2>\n')
h.write('<p class="section-desc fade-up" style="text-align:center;margin:0 auto 48px">A structured timeline highlighting key assessments, deliverables, and evaluation milestones of the EduMonitor research project.</p>\n')
h.write('<div class="ms-timeline">\n')
for date,title,desc,marks,pct,icon in ms:
    h.write(f'''<div class="ms-item fade-up"><div class="ms-dot-wrap"><div class="ms-dot"></div></div>
<div class="ms-card"><div class="ms-card-header"><i class="fas fa-calendar-alt"></i> {date}</div>
<h3>{title}</h3><p>{desc}</p>
<div class="ms-footer"><div class="ms-marks-row"><span class="ms-marks-label">Marks Allocated:</span><span class="ms-marks-val">{marks}</span></div>
<div class="ms-progress"><div class="ms-progress-bar" style="width:{pct}%"></div></div><span class="ms-pct">{pct}%</span></div></div></div>
''')
h.write('</div></div></section>\n')

# Downloads
cats = [
    ("Project Charter","fa-file-contract",[("Project Charter","PDF","#")]),
    ("Proposal Documents","fa-file-alt",[
        ("Proposal — Kisara W.C","PDF","https://drive.google.com/file/d/1zoigON9K3tz5XnG5sB5bEOSHDSQ93wkD/view?usp=sharing"),
        ("Proposal — De Silva A.R.S","PDF","https://drive.google.com/file/d/1eCFB98qBPTR-aU7_iUR1phsbnIiAR0PX/view?usp=sharing"),
        ("Proposal — Deemantha P.H.H.C","PDF","https://drive.google.com/file/d/1MjSbM9GbwZbyY6dK1Cg5LIFIXrwMV6HW/view?usp=sharing"),
        ("Proposal — Pallewela S.M","PDF","https://drive.google.com/file/d/1CtByewh5yUn82ns7rlkBrjDiw9TTP8c3/view?usp=sharing")]),
    ("Check List Documents","fa-clipboard-check",[
        ("Checklist 1","PDF","https://drive.google.com/file/d/10CZtYHOeZyjU0W7-SeYY8PungCAeCWMO/view?usp=sharing"),
        ("Checklist 2","PDF","https://drive.google.com/file/d/199h5isWZ2gNaD1AlXGXIGlrSwdEj0_LH/view?usp=sharing"),
        ("Checklist 3","PDF","#"),
        ("Checklist 4","PDF","#"),
        ("Topic Assessment Form","PDF","https://drive.google.com/file/d/1PIHdjM-kY8fP5sgXGsT5zmx0-go9FQ18/view?usp=sharing")]),
    ("Final Documents","fa-book",[
        ("Final Group Report","PDF","#"),("Final Report — Kisara W.C","PDF","#"),
        ("Final Report — De Silva A.R.S","PDF","#"),("Final Report — Deemantha P.H.H.C","PDF","#"),
        ("Final Report — Pallewela S.M","PDF","#")]),
    ("Presentations","fa-file-powerpoint",[
        ("Proposal Presentation","PPTX","https://docs.google.com/presentation/d/1O9Egh_E56Qb0K_lxxRWWiL_8CkAZ8cqg/edit?usp=drive_link&ouid=106375118808152884765&rtpof=true&sd=true"),
        ("Progress Presentation 1","PPTX","https://docs.google.com/presentation/d/1kUfcPPYykvClRLFozm9yRUkSEUKkAJYw/edit?usp=drive_link&ouid=106375118808152884765&rtpof=true&sd=true"),
        ("Progress Presentation 2","PPTX","#"),("Final Presentation","PPTX","#")])
]
h.write('<section class="section" id="downloads" style="background:var(--bg2)"><div class="container">\n')
h.write('<div class="section-label fade-up">Resources</div><h2 class="section-title fade-up">Downloads &amp; <span class="hl">Documents</span></h2>\n')
h.write('<p class="section-desc fade-up">Access our research documents, presentations, and reports.</p>\n')
for cat,icon,files in cats:
    h.write(f'<div class="dl-category fade-up"><div class="dl-category-title"><i class="fas {icon}"></i> {cat}</div><div class="downloads-grid">\n')
    for name,ftype,link in files:
        ic = "pdf" if ftype=="PDF" else "ppt" if ftype=="PPTX" else "doc"
        fi = "fa-file-pdf" if ftype=="PDF" else "fa-file-powerpoint" if ftype=="PPTX" else "fa-file-alt"
        href = link if link!="#" else "#"
        tgt = ' target="_blank"' if link!="#" else ''
        h.write(f'<div class="download-card"><div class="dl-icon {ic}"><i class="fas {fi}"></i></div><div class="dl-info"><h4>{name}</h4><span class="dl-type">{ftype} Document</span></div><a class="dl-btn" href="{href}"{tgt}><i class="fas fa-external-link-alt"></i></a></div>\n')
    h.write('</div></div>\n')
h.write('</div></section>\n')

# Publications
pubs = [
    ("Multidimensional Analysis of Factors Affecting Undergraduate Lecture Attendance","Deemantha P.H.H.C","Evidence from a Sri Lankan Higher Education Context","https://drive.google.com/file/d/18BccTZqR0HdPY7PYmkl4MaW9gOkjz36b/view?usp=sharing"),
    ("A Dual-Source RAG-Based Real-Time Classroom Support System","Pallewela S.M","For Question Answering, Lecture Summarisation, and Outcome-Aligned Assessment","https://drive.google.com/file/d/1ijBnYRWrY53CFb72abhz2BhSFVAp89KR/view?usp=sharing"),
    ("A Unified Real-Time Classroom Analytics Framework","Kisara W.C &amp; De Silva A.R.S","For Student Engagement and Teacher Behavior Analysis","https://drive.google.com/file/d/1cvGi68bRY7MbRyHef3ipbV87TmDcQEy9/view?usp=sharing")
]
h.write('<section class="section" id="publications"><div class="container">\n')
h.write('<div class="section-label fade-up">Publications</div><h2 class="section-title fade-up">Research <span class="hl">Papers</span></h2>\n')
h.write('<p class="section-desc fade-up">Our research contributions accepted for academic publication.</p>\n')
for title,author,sub,link in pubs:
    h.write(f'<div class="pub-card fade-up"><h3>{title}</h3><div class="pub-authors">{author}</div><p>{sub}</p><a class="pub-link" href="{link}" target="_blank">Read Paper <i class="fas fa-arrow-right"></i></a></div>\n')
h.write('</div></section>\n')

# Team
team = [
    ("Prof. Pradeep Abeygunawardhana","Supervisor","","Prof. Pradeep Abeygunawardhana(Supervisor).jpg"),
    ("Ms. Suranjini Silva","Co-Supervisor","","Ms. Suranjini Silva(Co-supervisor).jpg"),
    ("Kisara W.C","Team Member","IT22582874","kisara w.c.jpg"),
    ("De Silva A.R.S","Team Member","IT22586834","dE SILVA a.r.s.png"),
    ("Deemantha P.H.H.C","Team Member","IT22560162","Deemantha P.H.H.C.JPG"),
    ("Pallewela S.M","Team Member","IT22594136","PALLEWELA S.M.jpg")
]
h.write('<section class="section" id="team" style="background:var(--bg2)"><div class="container">\n')
h.write('<div class="section-label fade-up">Our Team</div><h2 class="section-title fade-up">Meet the <span class="hl">Team</span></h2>\n')
h.write('<p class="section-desc fade-up">The people behind EduMonitor.</p><div class="team-grid">\n')
for name,role,tid,img in team:
    idhtml = f'<div class="team-id">{tid}</div>' if tid else ''
    h.write(f'<div class="team-card fade-up"><img class="team-avatar" src="images/{img}" alt="{name}"/><h3>{name}</h3><div class="team-role">{role}</div>{idhtml}</div>\n')
h.write('</div></div></section>\n')

# Contact + Form
contacts = [
    ("Kisara W.C","it22582874@my.sliit.lk","076 018 6270"),
    ("De Silva A.R.S","it22586834@my.sliit.lk","075 647 0579"),
    ("Deemantha P.H.H.C","it22560162@my.sliit.lk","070 308 1363"),
    ("Pallewela S.M","it22594136@my.sliit.lk","071 480 8366")
]
h.write('<section class="section" id="contact"><div class="container">\n')
h.write('<div class="section-label fade-up">Get In Touch</div><h2 class="section-title fade-up">Contact <span class="hl">Us</span></h2>\n')
h.write('<p class="section-desc fade-up">Have questions about our research? Reach out to any team member.</p>\n')
h.write('<div class="contact-wrapper fade-up"><div class="contact-info-cards">\n')
for name,email,phone in contacts:
    h.write(f'<div class="contact-card"><div class="contact-icon"><i class="fas fa-envelope"></i></div><div><h4>{name}</h4><a href="mailto:{email}">{email}</a><p>{phone}</p></div></div>\n')
h.write('<div class="contact-card"><div class="contact-icon"><i class="fas fa-map-marker-alt"></i></div><div><h4>SLIIT Malabe Campus</h4><p>New Kandy Rd, Malabe, Sri Lanka</p></div></div>\n')
h.write('</div>\n')
# Form
h.write("""<div class="contact-form"><h3>Send us a Message</h3><p class="form-sub">We'll get back to you as soon as possible.</p>
<form id="contactForm"><div class="form-row"><div class="form-group"><label for="fname">First Name</label><input type="text" id="fname" required placeholder="Your first name"/></div>
<div class="form-group"><label for="lname">Last Name</label><input type="text" id="lname" required placeholder="Your last name"/></div></div>
<div class="form-group"><label for="email">Email</label><input type="email" id="email" required placeholder="your@email.com"/></div>
<div class="form-group"><label for="message">Message</label><textarea id="message" required placeholder="How can we help you?"></textarea></div>
<button type="submit" class="form-submit">Send Message</button><div class="form-msg" id="formMsg"></div></form></div></div></div></section>
""")

# Stay Connected
h.write("""<div class="stay-connected"><div class="container">
<div class="section-label">Let's Stay Connected</div>
<h2 class="section-title" style="font-size:1.6rem">Follow Our Research Journey</h2>
<p style="color:var(--t2);margin-top:8px">Stay updated with our latest developments and publications.</p>
<div class="social-links">
<a href="#" class="social-link"><i class="fab fa-github"></i></a>
<a href="#" class="social-link"><i class="fab fa-linkedin-in"></i></a>
<a href="mailto:it22560162@my.sliit.lk" class="social-link"><i class="fas fa-envelope"></i></a>
<a href="#" class="social-link"><i class="fab fa-researchgate"></i></a>
</div></div></div>
""")

# Footer + scroll-to-top
h.write("""<footer class="footer"><div class="container">
<p style="margin-bottom:8px"><a href="#home" class="nav-logo" style="font-size:1.1rem">Edu<span>Monitor</span></a></p>
<p>&copy; 2025 EduMonitor — Sri Lanka Institute of Information Technology. All rights reserved.</p>
</div></footer>
<button class="scroll-top" aria-label="Scroll to top"><i class="fas fa-chevron-up"></i></button>
<script src="script.js"></script></body></html>""")
h.close()
print("index.html generated successfully!")
