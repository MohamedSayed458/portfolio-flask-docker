from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mohamed Newish | Junior DevOps Engineer</title>
        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
        <!-- Font Awesome -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --primary: #3b82f6;
                --secondary: #10b981;
                --dark: #0f172a;
                --light: #f8fafc;
                --gray: #64748b;
                --card-bg: #1e293b;
            }
            
            * { margin: 0; padding: 0; box-sizing: border-box; }
            
            body {
                font-family: 'Inter', sans-serif;
                background-color: var(--dark);
                color: var(--light);
                line-height: 1.6;
            }
            
            .container {
                max-width: 1100px;
                margin: 0 auto;
                padding: 0 20px;
            }
            
            /* Header */
            header {
                padding: 20px 0;
                border-bottom: 1px solid #334155;
            }
            
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-family: 'Fira Code', monospace;
                font-size: 1.5rem;
                font-weight: 700;
                color: var(--primary);
            }
            
            .nav-links a {
                color: var(--light);
                text-decoration: none;
                margin-left: 20px;
                font-size: 0.9rem;
                transition: color 0.3s;
            }
            
            .nav-links a:hover { color: var(--primary); }
            
            /* Hero Section */
            .hero {
                padding: 100px 0;
                text-align: center;
            }
            
            .hero h1 {
                font-size: 3.5rem;
                margin-bottom: 20px;
                background: linear-gradient(to right, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .hero p {
                font-size: 1.2rem;
                color: var(--gray);
                max-width: 600px;
                margin: 0 auto 30px;
            }
            
            .btn {
                display: inline-block;
                padding: 12px 30px;
                background: var(--primary);
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 600;
                transition: transform 0.2s;
            }
            
            .btn:hover { transform: translateY(-2px); }
            .btn-outline {
                background: transparent;
                border: 2px solid var(--primary);
                margin-left: 10px;
            }
            
            /* Sections */
            section { padding: 80px 0; }
            
            .section-title {
                font-size: 2rem;
                margin-bottom: 40px;
                text-align: center;
                font-family: 'Fira Code', monospace;
            }
            
            .section-title::before {
                content: "# ";
                color: var(--secondary);
            }
            
            /* Skills Grid */
            .skills-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }
            
            .skill-card {
                background: var(--card-bg);
                padding: 25px;
                border-radius: 10px;
                border: 1px solid #334155;
                transition: transform 0.3s;
            }
            
            .skill-card:hover { transform: translateY(-5px); border-color: var(--primary); }
            
            .skill-card h3 {
                margin-bottom: 15px;
                color: var(--primary);
                font-family: 'Fira Code', monospace;
            }
            
            .skill-tags {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            
            .tag {
                background: #334155;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 0.85rem;
            }
            
            /* Projects */
            .projects-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
            }
            
            .project-card {
                background: var(--card-bg);
                border-radius: 10px;
                overflow: hidden;
                border: 1px solid #334155;
            }
            
            .project-content { padding: 25px; }
            
            .project-card h3 {
                margin-bottom: 10px;
                color: var(--secondary);
            }
            
            .project-card p {
                color: var(--gray);
                margin-bottom: 20px;
                font-size: 0.95rem;
            }
            
            .project-links a {
                color: var(--primary);
                text-decoration: none;
                font-weight: 600;
                margin-right: 15px;
            }
            
            .project-links a:hover { text-decoration: underline; }
            
            /* Footer */
            footer {
                background: #020617;
                padding: 40px 0;
                text-align: center;
                color: var(--gray);
                border-top: 1px solid #334155;
            }
            
            .social-links {
                margin-bottom: 20px;
            }
            
            .social-links a {
                color: var(--light);
                font-size: 1.5rem;
                margin: 0 10px;
                transition: color 0.3s;
            }
            
            .social-links a:hover { color: var(--primary); }
            
            /* Terminal Badge */
            .terminal-badge {
                background: #000;
                color: #10b981;
                padding: 5px 10px;
                border-radius: 5px;
                font-family: 'Fira Code', monospace;
                font-size: 0.8rem;
                display: inline-block;
                margin-bottom: 20px;
                border: 1px solid #333;
            }
            
            @media (max-width: 768px) {
                .hero h1 { font-size: 2.5rem; }
                .nav-links { display: none; }
            }
        </style>
    </head>
    <body>
        <!-- Header -->
        <header>
            <div class="container">
                <nav>
                    <div class="logo">&lt;Mohamed /&gt;</div>
                    <div class="nav-links">
                        <a href="#about">About</a>
                        <a href="#skills">Skills</a>
                        <a href="#projects">Projects</a>
                        <a href="#contact">Contact</a>
                    </div>
                </nav>
            </div>
        </header>

        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <div class="terminal-badge">root@aws-ec2:~# ./deploy_portfolio.sh</div>
                <h1>Junior DevOps Engineer</h1>
                <p>Bridging the gap between Development, Operations, and Security. Specialized in automating infrastructure, containerizing applications, and building secure CI/CD pipelines.</p>
                <div>
                    <a href="#projects" class="btn">View Projects</a>
                    <a href="https://github.com/MohamedSayed458" target="_blank" class="btn btn-outline"><i class="fab fa-github"></i> GitHub</a>
                </div>
            </div>
        </section>

        <!-- Skills Section -->
        <section id="skills">
            <div class="container">
                <h2 class="section-title">Technical Skills</h2>
                <div class="skills-grid">
                    <!-- DevOps -->
                    <div class="skill-card">
                        <h3><i class="fas fa-cloud"></i> DevOps & Cloud</h3>
                        <div class="skill-tags">
                            <span class="tag">Docker</span>
                            <span class="tag">Docker Compose</span>
                            <span class="tag">CI/CD</span>
                            <span class="tag">GitHub Actions</span>
                            <span class="tag">AWS EC2</span>
                            <span class="tag">Linux Admin</span>
                        </div>
                    </div>
                    
                    <!-- Programming -->
                    <div class="skill-card">
                        <h3><i class="fas fa-code"></i> Programming</h3>
                        <div class="skill-tags">
                            <span class="tag">Python</span>
                            <span class="tag">JavaScript</span>
                            <span class="tag">Bash Scripting</span>
                            <span class="tag">HTML5/CSS3</span>
                        </div>
                    </div>
                    
                    <!-- Web & DB -->
                    <div class="skill-card">
                        <h3><i class="fas fa-database"></i> Web & Database</h3>
                        <div class="skill-tags">
                            <span class="tag">Flask</span>
                            <span class="tag">Node.js</span>
                            <span class="tag">RESTful APIs</span>
                            <span class="tag">PostgreSQL</span>
                            <span class="tag">SQL</span>
                        </div>
                    </div>
                    
                    <!-- Security -->
                    <div class="skill-card">
                        <h3><i class="fas fa-shield-alt"></i> Security</h3>
                        <div class="skill-tags">
                            <span class="tag">OWASP Top 10</span>
                            <span class="tag">Input Validation</span>
                            <span class="tag">Auth Concepts</span>
                            <span class="tag">Security Testing</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects">
            <div class="container">
                <h2 class="section-title">Featured Projects</h2>
                <div class="projects-grid">
                    <!-- Project 1 -->
                    <div class="project-card">
                        <div class="project-content">
                            <h3>DevOps Portfolio Pipeline</h3>
                            <p>Containerized Flask application deployed on AWS EC2. Automated CI/CD pipelines using GitHub Actions with integrated health checks and Docker orchestration.</p>
                            <div class="skill-tags" style="margin-bottom: 15px;">
                                <span class="tag">Flask</span>
                                <span class="tag">Docker</span>
                                <span class="tag">AWS</span>
                                <span class="tag">GitHub Actions</span>
                            </div>
                            <div class="project-links">
                                <a href="https://github.com/MohamedSayed458/portfolio-flask-docker" target="_blank"><i class="fab fa-github"></i> View Code</a>
                                <a href="/health" target="_blank"><i class="fas fa-heartbeat"></i> Health Check</a>
                            </div>
                        </div>
                    </div>

                    <!-- Project 2 -->
                    <div class="project-card">
                        <div class="project-content">
                            <h3>Sharingan</h3>
                            <p>Bash automation tool that streamlines the reconnaissance process. Reduces manual information gathering time significantly during security assessments.</p>
                            <div class="skill-tags" style="margin-bottom: 15px;">
                                <span class="tag">Bash</span>
                                <span class="tag">Automation</span>
                                <span class="tag">Security</span>
                            </div>
                            <div class="project-links">
                                <a href="https://github.com/MohamedSayed458/Sharingan" target="_blank"><i class="fab fa-github"></i> View Code</a>
                            </div>
                        </div>
                    </div>

                    <!-- Project 3 -->
                    <div class="project-card">
                        <div class="project-content">
                            <h3>LFler</h3>
                            <p>Python-based utility for automated identification and testing of Local File Inclusion (LFI) vulnerabilities. Demonstrates deep understanding of web security flaws.</p>
                            <div class="skill-tags" style="margin-bottom: 15px;">
                                <span class="tag">Python</span>
                                <span class="tag">Security</span>
                                <span class="tag">OWASP</span>
                            </div>
                            <div class="project-links">
                                <a href="https://github.com/MohamedSayed458/LFler" target="_blank"><i class="fab fa-github"></i> View Code</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact/Footer -->
        <footer id="contact">
            <div class="container">
                <div class="social-links">
                    <a href="https://github.com/MohamedSayed458" target="_blank"><i class="fab fa-github"></i></a>
                    <a href="mailto:mohamedsayed2646@gmail.com"><i class="fas fa-envelope"></i></a>
                    <a href="https://www.linkedin.com/in/mohamed-newish-8470a5395/"><i class="fab fa-linkedin"></i></a>
                </div>
                <p>&copy; 2026 Mohamed Newish. Built with Flask & Docker on AWS.</p>
                <p style="font-size: 0.8rem; margin-top: 10px; color: #475569;">
                    Languages: English (Fluent), German (Good Knowledge), Arabic (Native)
                </p>
            </div>
        </footer>

        <!-- Smooth Scroll Script -->
        <script>
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        </script>
    </body>
    </html>
    ''')

@app.route('/api')
def api():
    # Return JSON for API clients
    return jsonify({
        "message": "Hello from Mohamed!",
        "role": "Junior DevOps Engineer",
        "status": "active",
        "projects": ["portfolio-flask-docker", "Sharingan", "LFler"]
    })

@app.route('/health')
def health():
    # Health check endpoint for monitoring demos
    return jsonify({
        "status": "healthy", 
        "service": "portfolio",
        "uptime": "running",
        "version": "1.0.0"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
