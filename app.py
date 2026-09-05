from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mohamed Newish | DevOps Engineer</title>
    <meta name="description" content="DevOps engineer in Chemnitz, Germany. Docker, Kubernetes (AWS EKS), Helm, Jenkins, GitHub Actions and Terraform.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* dark is the default; [data-theme="light"] is the opt-in palette */
        :root {
            --primary:#3b82f6; --secondary:#10b981;
            --bg:#0f172a; --surface:#1e293b; --raised:#243449;
            --border:#334155; --text:#f8fafc; --muted:#94a3b8; --faint:#64748b;
            --tag-bg:#0b1220; --shadow:0 10px 30px rgba(0,0,0,.35);
        }
        :root[data-theme="light"] {
            --primary:#1d4ed8; --secondary:#047857;
            --bg:#f8fafc; --surface:#ffffff; --raised:#f1f5f9;
            --border:#dbe3ec; --text:#0f172a; --muted:#516072; --faint:#7b8794;
            --tag-bg:#eef3f9; --shadow:0 8px 24px rgba(15,23,42,.07);
        }
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family:'Inter',sans-serif; background:var(--bg); color:var(--text);
            line-height:1.6; transition:background .2s ease, color .2s ease;
        }
        .container { max-width:1100px; margin:0 auto; padding:0 20px; }
        a { color:inherit; }
        :focus-visible { outline:2px solid var(--primary); outline-offset:3px; }

        header { padding:18px 0; border-bottom:1px solid var(--border);
                 position:sticky; top:0; background:var(--bg); z-index:10; }
        nav { display:flex; justify-content:space-between; align-items:center; gap:16px; }
        .logo { font-family:'Fira Code',monospace; font-size:1.4rem; font-weight:700; color:var(--primary); }
        .nav-links { display:flex; align-items:center; gap:24px; }
        .nav-links a { color:var(--muted); text-decoration:none; font-size:.95rem; }
        .nav-links a:hover { color:var(--text); }
        #theme-toggle {
            font-family:'Fira Code',monospace; font-size:.82rem; cursor:pointer;
            color:var(--muted); background:var(--raised); border:1px solid var(--border);
            border-radius:6px; padding:6px 12px; display:inline-flex; align-items:center; gap:7px;
        }
        #theme-toggle:hover { color:var(--text); border-color:var(--primary); }

        section { padding:64px 0; }
        .section-title { font-size:1.55rem; font-weight:700; margin-bottom:8px; }
        .section-sub { color:var(--muted); margin-bottom:30px; font-size:.95rem; }

        .hero { padding:76px 0 60px; }
        .terminal-badge {
            display:inline-block; font-family:'Fira Code',monospace; font-size:.82rem;
            color:var(--secondary); background:var(--tag-bg); border:1px solid var(--border);
            border-radius:6px; padding:7px 13px; margin-bottom:22px;
        }
        .hero h1 { font-size:3.1rem; line-height:1.1; font-weight:700; margin-bottom:8px; }
        .hero h2 { font-size:1.15rem; font-weight:400; color:var(--primary); margin-bottom:20px; }
        .hero p { color:var(--muted); max-width:66ch; margin-bottom:26px; }
        .btn {
            display:inline-flex; align-items:center; gap:8px; text-decoration:none;
            padding:11px 20px; border-radius:8px; font-weight:600; font-size:.95rem;
            background:var(--primary); color:#fff; margin-right:12px; margin-bottom:10px;
        }
        .btn:hover { opacity:.9; }
        .btn-outline { background:transparent; color:var(--text); border:1px solid var(--border); }
        .btn-outline:hover { border-color:var(--primary); color:var(--primary); opacity:1; }
        .meta { margin-top:26px; color:var(--faint); font-size:.9rem; display:flex; flex-wrap:wrap; gap:8px 22px; }

        .grid { display:grid; gap:20px; }
        .skills-grid { grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); }
        .card {
            background:var(--surface); border:1px solid var(--border);
            border-radius:12px; padding:22px; box-shadow:var(--shadow);
        }
        .card h3 { font-size:1.02rem; margin-bottom:12px; display:flex; align-items:center; gap:9px; }
        .card h3 i { color:var(--primary); width:18px; }
        .tags { display:flex; flex-wrap:wrap; gap:7px; }
        .tag {
            font-family:'Fira Code',monospace; font-size:.76rem; color:var(--muted);
            background:var(--tag-bg); border:1px solid var(--border);
            border-radius:5px; padding:4px 9px;
        }

        .projects-grid { grid-template-columns:repeat(auto-fit,minmax(330px,1fr)); }
        .project-card h3 { font-size:1.14rem; margin-bottom:4px; display:block; }
        .project-card .stack { font-family:'Fira Code',monospace; font-size:.78rem;
                               color:var(--secondary); margin-bottom:12px; }
        .project-card p { color:var(--muted); font-size:.93rem; margin-bottom:14px; }
        .project-links { display:flex; gap:18px; font-size:.88rem; }
        .project-links a { color:var(--primary); text-decoration:none; font-weight:600; }
        .project-links a:hover { text-decoration:underline; }

        .two-col { grid-template-columns:1.6fr 1fr; }
        .edu { margin-bottom:18px; }
        .edu .deg { font-weight:600; }
        .edu .org, .edu .when { color:var(--muted); font-size:.92rem; }
        .lang { display:flex; justify-content:space-between; padding:7px 0;
                border-bottom:1px solid var(--border); font-size:.93rem; }
        .lang span { color:var(--muted); }

        footer { border-top:1px solid var(--border); padding:36px 0; text-align:center; }
        .social-links { display:flex; justify-content:center; gap:22px; margin-bottom:16px; }
        .social-links a { color:var(--muted); font-size:1.35rem; text-decoration:none; }
        .social-links a:hover { color:var(--primary); }
        footer p { color:var(--faint); font-size:.87rem; }

        @media (max-width:768px) {
            .hero h1 { font-size:2.3rem; }
            .nav-links a { display:none; }
            .two-col { grid-template-columns:1fr; }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo">&lt;Mohamed /&gt;</div>
                <div class="nav-links">
                    <a href="#skills">Skills</a>
                    <a href="#projects">Projects</a>
                    <a href="#education">Education</a>
                    <a href="#contact">Contact</a>
                    <button id="theme-toggle" type="button" aria-label="Switch colour theme">
                        <i class="fas fa-sun" id="theme-icon"></i><span id="theme-label">Light</span>
                    </button>
                </div>
            </nav>
        </div>
    </header>

    <section class="hero" id="about">
        <div class="container">
            <div class="terminal-badge">$ kubectl get pods --all-namespaces</div>
            <h1>Mohamed Newish</h1>
            <h2>DevOps Engineer — containers, CI/CD and the clusters underneath</h2>
            <p>
                I focus on container orchestration with Docker and Kubernetes (AWS EKS), release
                management with Helm, and automating deployments through CI/CD pipelines (Jenkins,
                GitHub Actions) and Infrastructure as Code (Terraform) on AWS. Confident on Linux and
                with Bash automation, plus working knowledge of Linux and Windows server administration.
            </p>
            <div>
                <a href="#projects" class="btn"><i class="fas fa-folder-open"></i> View projects</a>
                <a href="https://github.com/Mohamed-Newish" target="_blank" rel="noopener" class="btn btn-outline">
                    <i class="fab fa-github"></i> GitHub
                </a>
                <a href="mailto:mohamedsayed2646@gmail.com" class="btn btn-outline">
                    <i class="fas fa-envelope"></i> Email me
                </a>
            </div>
            <div class="meta">
                <span><i class="fas fa-location-dot"></i> Chemnitz, Germany</span>
                <span><i class="fas fa-circle-check"></i> Open to DevOps · Platform · SRE roles</span>
            </div>
        </div>
    </section>

    <section id="skills">
        <div class="container">
            <h2 class="section-title">Technical skills</h2>
            <p class="section-sub">What I work with day to day.</p>
            <div class="grid skills-grid">
                <div class="card">
                    <h3><i class="fas fa-cubes"></i> Containers &amp; orchestration</h3>
                    <div class="tags">
                        <span class="tag">Docker</span><span class="tag">Docker Compose</span>
                        <span class="tag">Kubernetes</span><span class="tag">AWS EKS</span>
                        <span class="tag">Helm</span><span class="tag">Ingress</span>
                        <span class="tag">Secrets</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-rotate"></i> CI/CD &amp; automation</h3>
                    <div class="tags">
                        <span class="tag">Jenkins</span><span class="tag">GitHub Actions</span>
                        <span class="tag">Terraform</span><span class="tag">Bash</span>
                        <span class="tag">Cron</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-cloud"></i> Cloud (AWS)</h3>
                    <div class="tags">
                        <span class="tag">EC2</span><span class="tag">EKS</span>
                        <span class="tag">VPC</span><span class="tag">Load Balancer</span>
                        <span class="tag">IAM basics</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-network-wired"></i> Networking</h3>
                    <div class="tags">
                        <span class="tag">TCP/IP</span><span class="tag">DNS</span>
                        <span class="tag">DHCP</span><span class="tag">HTTP/HTTPS</span>
                        <span class="tag">NGINX Ingress</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-server"></i> Systems &amp; administration</h3>
                    <div class="tags">
                        <span class="tag">Linux (Ubuntu/Debian)</span><span class="tag">Users &amp; permissions</span>
                        <span class="tag">Logging</span><span class="tag">Windows Server</span>
                        <span class="tag">Active Directory</span><span class="tag">GPO</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-chart-line"></i> Monitoring &amp; databases</h3>
                    <div class="tags">
                        <span class="tag">Prometheus</span><span class="tag">Grafana</span>
                        <span class="tag">PostgreSQL</span><span class="tag">SQL Server basics</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-code"></i> Programming &amp; scripting</h3>
                    <div class="tags">
                        <span class="tag">Bash</span><span class="tag">Python</span>
                        <span class="tag">Go</span><span class="tag">JavaScript</span>
                    </div>
                </div>
                <div class="card">
                    <h3><i class="fas fa-shield-halved"></i> Security &amp; tools</h3>
                    <div class="tags">
                        <span class="tag">OWASP Top 10</span><span class="tag">Input validation</span>
                        <span class="tag">Authentication</span><span class="tag">Git &amp; GitHub</span>
                        <span class="tag">Vim</span><span class="tag">Postman</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="projects">
        <div class="container">
            <h2 class="section-title">Projects</h2>
            <p class="section-sub">Infrastructure first, then the security tooling.</p>
            <div class="grid projects-grid">

                <div class="card project-card">
                    <h3>Journey App — CI/CD on AWS EKS</h3>
                    <div class="stack">Docker · Kubernetes (EKS) · Helm · Jenkins · NGINX Ingress · PostgreSQL</div>
                    <p>
                        A full-stack application (Node.js/Express, PostgreSQL, Nginx) containerized and
                        deployed to an AWS EKS cluster. A Jenkins declarative pipeline builds both images,
                        pushes them to Docker Hub and releases through Helm on every git push, with
                        zero-downtime rolling updates, path routing via NGINX Ingress and credentials in
                        Kubernetes Secrets.
                    </p>
                    <div class="project-links">
                        <a href="https://github.com/Mohamed-Newish/journey-app-devops" target="_blank" rel="noopener">
                            <i class="fab fa-github"></i> View code
                        </a>
                    </div>
                </div>

                <div class="card project-card">
                    <h3>Cloud-native DevOps Portfolio</h3>
                    <div class="stack">Flask · Docker · GitHub Actions · AWS EC2 · Gunicorn</div>
                    <p>
                        This site. A containerized Flask application with an automated CI pipeline in
                        GitHub Actions that builds the image, runs it and gates the deploy on a
                        <code>/health</code> check before anything ships.
                    </p>
                    <div class="project-links">
                        <a href="https://github.com/Mohamed-Newish/portfolio-flask-docker" target="_blank" rel="noopener">
                            <i class="fab fa-github"></i> View code
                        </a>
                        <a href="/health" target="_blank"><i class="fas fa-heart-pulse"></i> Health check</a>
                        <a href="/api" target="_blank"><i class="fas fa-code"></i> API</a>
                    </div>
                </div>

                <div class="card project-card">
                    <h3>sharingan-go — recon orchestrator</h3>
                    <div class="stack">Go · concurrency · rate limiting · tool orchestration</div>
                    <p>
                        A Go rewrite of a Bash recon pipeline for authorized security testing, built around
                        a stealth engine: an adaptive rate limiter, a circuit breaker and WAF fingerprinting
                        that tune themselves to how the target responds. Four modes behind separate scope
                        gates, each driving established tools and skipping missing ones cleanly.
                    </p>
                    <div class="project-links">
                        <a href="https://github.com/Mohamed-Newish/sharingan-go" target="_blank" rel="noopener">
                            <i class="fab fa-github"></i> View code
                        </a>
                    </div>
                </div>

                <div class="card project-card">
                    <h3>byakugan — content inspection</h3>
                    <div class="stack">Bash · concurrent phases · toolchain integration</div>
                    <p>
                        The companion to sharingan-go: seven concurrent phases covering screenshots,
                        path and parameter wordlists, SQLi/XSS candidates and secrets in page source —
                        writing into the same per-target output directory without duplicating work.
                    </p>
                    <div class="project-links">
                        <a href="https://github.com/Mohamed-Newish/byakugan" target="_blank" rel="noopener">
                            <i class="fab fa-github"></i> View code
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <section id="education">
        <div class="container">
            <h2 class="section-title">Education &amp; languages</h2>
            <div class="grid two-col">
                <div class="card">
                    <div class="edu">
                        <div class="deg">M.Sc. Embedded Systems</div>
                        <div class="org">Chemnitz University of Technology (TU Chemnitz)</div>
                        <div class="when">2025 – present · Chemnitz, Germany</div>
                    </div>
                    <div class="edu">
                        <div class="deg">B.Sc. Electrical Engineering</div>
                        <div class="org">Faculty of Engineering Shoubra, Benha University</div>
                        <div class="when">Benha, Egypt</div>
                    </div>
                </div>
                <div class="card">
                    <div class="lang"><b>English</b><span>Fluent</span></div>
                    <div class="lang"><b>Arabic</b><span>Native</span></div>
                    <div class="lang" style="border-bottom:0"><b>German</b><span>B1</span></div>
                </div>
            </div>
        </div>
    </section>

    <footer id="contact">
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Mohamed-Newish" target="_blank" rel="noopener" aria-label="GitHub"><i class="fab fa-github"></i></a>
                <a href="mailto:mohamedsayed2646@gmail.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
                <a href="https://www.linkedin.com/in/mohamed-newish-8470a5395/" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
            </div>
            <p>&copy; 2026 Mohamed Newish · Built with Flask, served by Gunicorn in a Docker container.</p>
        </div>
    </footer>

    <script>
        (function () {
            var root = document.documentElement;
            var btn = document.getElementById('theme-toggle');
            var icon = document.getElementById('theme-icon');
            var label = document.getElementById('theme-label');

            function apply(mode) {
                root.dataset.theme = mode;
                var toLight = mode !== 'light';
                icon.className = toLight ? 'fas fa-sun' : 'fas fa-moon';
                label.textContent = toLight ? 'Light' : 'Dark';
            }

            var saved = 'dark';
            try { saved = localStorage.getItem('theme') || 'dark'; } catch (e) {}
            apply(saved);

            btn.addEventListener('click', function () {
                var next = root.dataset.theme === 'light' ? 'dark' : 'light';
                apply(next);
                try { localStorage.setItem('theme', next); } catch (e) {}
            });

            document.querySelectorAll('a[href^="#"]').forEach(function (a) {
                a.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href'))
                            .scrollIntoView({ behavior: 'smooth' });
                });
            });
        })();
    </script>
</body>
</html>
'''


@app.route('/')
def home():
    return render_template_string(PAGE)


@app.route('/api')
def api():
    return jsonify({
        "message": "Hello from Mohamed!",
        "role": "DevOps Engineer",
        "location": "Chemnitz, Germany",
        "status": "active",
        "skills": ["Docker", "Kubernetes", "Helm", "Jenkins", "GitHub Actions", "Terraform", "AWS"],
        "projects": [
            "journey-app-devops",
            "portfolio-flask-docker",
            "sharingan-go",
            "byakugan"
        ]
    })


@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "portfolio",
        "uptime": "running",
        "version": "2.0.0"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
