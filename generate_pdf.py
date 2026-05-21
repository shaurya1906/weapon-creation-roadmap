"""
generate_pdf.py - Project Roadmap PDF Generator
Creates a premium, visually rich PDF showcasing 50+ projects
curated by Shaurya Mishra.
"""

from fpdf import FPDF
import os
import math
import re


def sanitize(text):
    """Replace non-latin1 characters so Helvetica can render them."""
    # Replace common unicode chars
    replacements = {
        '\u2014': '-',   # em dash
        '\u2013': '-',   # en dash
        '\u2018': "'",   # left single quote
        '\u2019': "'",   # right single quote
        '\u201c': '"',   # left double quote
        '\u201d': '"',   # right double quote
        '\u2026': '...',  # ellipsis
        '\u2022': '*',   # bullet
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    # Strip any remaining non-latin1 characters (emojis, etc.)
    text = text.encode('latin-1', errors='ignore').decode('latin-1')
    return text

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COLOR PALETTE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DARK_BG       = (13, 17, 23)
CARD_BG       = (22, 27, 34)
ACCENT_BLUE   = (56, 132, 244)
ACCENT_PURPLE = (139, 92, 246)
ACCENT_GREEN  = (52, 211, 153)
ACCENT_ORANGE = (251, 146, 60)
ACCENT_PINK   = (236, 72, 153)
ACCENT_CYAN   = (34, 211, 238)
ACCENT_RED    = (239, 68, 68)
ACCENT_YELLOW = (250, 204, 21)
WHITE         = (230, 237, 243)
MUTED         = (139, 148, 158)
DIM           = (48, 54, 61)

CATEGORY_COLORS = {
    "Web Development":          ACCENT_BLUE,
    "AI & Machine Learning":    ACCENT_PURPLE,
    "Data & Analytics":         ACCENT_GREEN,
    "Developer Tools & CLI":    ACCENT_ORANGE,
    "Games & Interactive":      ACCENT_PINK,
    "Cloud & DevOps":           ACCENT_CYAN,
    "Mobile & PWA":             ACCENT_RED,
    "IoT & Hardware":           ACCENT_YELLOW,
    "Security & Auth":          (168, 85, 247),
    "Creative & Media":         (244, 114, 182),
}

CATEGORY_ICONS = {
    "Web Development":          "[WEB]",
    "AI & Machine Learning":    "[AI]",
    "Data & Analytics":         "[DATA]",
    "Developer Tools & CLI":    "[DEV]",
    "Games & Interactive":      "[GAME]",
    "Cloud & DevOps":           "[CLOUD]",
    "Mobile & PWA":             "[APP]",
    "IoT & Hardware":           "[IOT]",
    "Security & Auth":          "[SEC]",
    "Creative & Media":         "[ART]",
}

DIFFICULTY_COLORS = {
    "Beginner":     ACCENT_GREEN,
    "Intermediate": ACCENT_ORANGE,
    "Advanced":     ACCENT_RED,
    "Expert":       ACCENT_PURPLE,
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROJECT DATA — 50+ Projects across 10 categories
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROJECTS = {
    "Web Development": [
        {
            
        
        },
        {
            "name": "E-Commerce Storefront",
            "desc": "Full-featured online store with product catalog, cart system, Stripe checkout, admin dashboard, and order tracking. Responsive design with skeleton loaders.",
            "tech": ["Next.js", "Stripe API", "PostgreSQL", "Prisma"],
            "difficulty": "Advanced",
            "time": "8-12 hours",
        },
        {
            "name": "Real-Time Chat Application",
            "desc": "WebSocket-powered chat with rooms, typing indicators, message reactions, file uploads, and online presence. End-to-end encrypted messaging.",
            "tech": ["React", "Socket.io", "Node.js", "MongoDB"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
        {
            "name": "Blog Platform with CMS",
            "desc": "Markdown-based blogging platform with rich text editor, SEO optimization, RSS feeds, analytics dashboard, and comment system with moderation.",
            "tech": ["Next.js", "MDX", "Supabase", "Vercel"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
        {
            "name": "Music Streaming App (Retrowave)",
            "desc": "Full music player with decade browsing, search, playlists, audio visualization, and streaming via YouTube Music API. Neon retrowave aesthetic.",
            "tech": ["HTML/CSS/JS", "Python Flask", "yt-dlp", "Web Audio API"],
            "difficulty": "Advanced",
            "time": "10-15 hours",
        },
        {
            "name": "Recipe Sharing Platform",
            "desc": "Community-driven recipe site with ingredient-based search, step-by-step instructions, nutritional info, meal planning calendar, and grocery list generator.",
            "tech": ["React", "Node.js", "PostgreSQL", "Cloudinary"],
            "difficulty": "Intermediate",
            "time": "6-8 hours",
        },
    ],
    "AI & Machine Learning": [
        {
            "name": "Synthetic AGI Orchestrator",
            "desc": "Multi-model AI synthesis engine that routes queries to GPT, Claude, and Gemini, then merges outputs for maximum accuracy. Features consensus scoring and confidence metrics.",
            "tech": ["Python", "FastAPI", "OpenAI API", "Anthropic API", "Gemini API"],
            "difficulty": "Expert",
            "time": "12-18 hours",
        },
        {
            "name": "AI-Powered Code Reviewer",
            "desc": "Automated PR review bot that analyzes code quality, security vulnerabilities, performance bottlenecks, and suggests improvements using LLM reasoning.",
            "tech": ["Python", "GitHub API", "Gemini API", "FastAPI"],
            "difficulty": "Advanced",
            "time": "6-8 hours",
        },
        {
            "name": "RAG Knowledge Base",
            "desc": "Retrieval-Augmented Generation system with document ingestion, vector embeddings, semantic search, and conversational Q&A with source citations.",
            "tech": ["Python", "LangChain", "ChromaDB", "OpenAI Embeddings"],
            "difficulty": "Advanced",
            "time": "5-7 hours",
        },
        {
            "name": "Sentiment Analysis Dashboard",
            "desc": "Real-time social media sentiment tracker with trend visualization, entity extraction, topic modeling, and alerting for brand mentions.",
            "tech": ["Python", "HuggingFace", "Streamlit", "Twitter API"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
        {
            "name": "AI Image Generator & Editor",
            "desc": "Text-to-image generation interface with inpainting, outpainting, style transfer, and prompt engineering presets. Gallery with favorites and sharing.",
            "tech": ["React", "Stable Diffusion API", "Node.js", "S3"],
            "difficulty": "Advanced",
            "time": "8-10 hours",
        },
        {
            "name": "Intelligent Resume Builder",
            "desc": "AI-powered resume creator that analyzes job descriptions, suggests bullet points, optimizes for ATS, and generates multiple format exports (PDF, DOCX).",
            "tech": ["Next.js", "OpenAI API", "Puppeteer", "PostgreSQL"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
    ],
    "Data & Analytics": [
        {
            "name": "IPL Match Predictor",
            "desc": "Data-driven sports prediction engine using historical stats, player form, venue analysis, and ensemble ML models. Live leaderboard and prediction accuracy tracking.",
            "tech": ["Python", "Pandas", "Scikit-learn", "React", "D3.js"],
            "difficulty": "Advanced",
            "time": "10-14 hours",
        },
        {
            "name": "Finance Tracker Dashboard",
            "desc": "Personal finance manager with bank sync, expense categorization, budget alerts, investment tracking, and interactive charts with drill-down capability.",
            "tech": ["React", "Chart.js", "Node.js", "Plaid API"],
            "difficulty": "Intermediate",
            "time": "6-8 hours",
        },
        {
            "name": "COVID/Health Data Visualizer",
            "desc": "Interactive choropleth maps and time-series charts for health data exploration. Supports custom dataset uploads and comparison views.",
            "tech": ["D3.js", "Mapbox", "Python Flask", "Pandas"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
        {
            "name": "GitHub Analytics Dashboard",
            "desc": "Visualize your coding activity - commit heatmaps, language breakdowns, PR metrics, contribution streaks, and repository health scores.",
            "tech": ["Next.js", "GitHub GraphQL API", "Recharts", "Vercel"],
            "difficulty": "Intermediate",
            "time": "4-5 hours",
        },
        {
            "name": "Real-Time Stock Screener",
            "desc": "Live stock data with technical indicators, candlestick charts, watchlists, alerts, and fundamental analysis filters. Paper trading simulator included.",
            "tech": ["React", "WebSocket", "Alpha Vantage API", "TradingView"],
            "difficulty": "Advanced",
            "time": "8-10 hours",
        },
    ],
    "Developer Tools & CLI": [
        {
            "name": "CLI Task Manager (Taskforge)",
            "desc": "Terminal-based project management with Kanban boards, time tracking, git integration, priority sorting, and Pomodoro timer. Syncs to cloud.",
            "tech": ["Python", "Rich", "Click", "SQLite"],
            "difficulty": "Beginner",
            "time": "3-4 hours",
        },
        {
            "name": "API Mock Server Generator",
            "desc": "Auto-generate realistic mock APIs from OpenAPI/Swagger specs with faker-powered data, latency simulation, and error scenario testing.",
            "tech": ["Node.js", "Express", "Faker.js", "YAML"],
            "difficulty": "Intermediate",
            "time": "3-5 hours",
        },
        {
            "name": "Code Snippet Manager",
            "desc": "Searchable, tagged code snippet library with syntax highlighting, multi-language support, VS Code extension integration, and team sharing.",
            "tech": ["Electron", "React", "SQLite", "Prism.js"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
        {
            "name": "Log Analyzer & Visualizer",
            "desc": "Parse, filter, and visualize application logs with pattern detection, error clustering, timeline views, and alert rule configuration.",
            "tech": ["Python", "Elasticsearch", "Kibana", "FastAPI"],
            "difficulty": "Advanced",
            "time": "6-8 hours",
        },
        {
            "name": "Database Schema Designer",
            "desc": "Visual ERD builder with drag-and-drop tables, relationship mapping, SQL/migration export, and schema versioning. Supports PostgreSQL, MySQL, SQLite.",
            "tech": ["React", "Canvas API", "Node.js", "SQL Generator"],
            "difficulty": "Advanced",
            "time": "8-10 hours",
        },
        {
            "name": "Regex Pattern Playground",
            "desc": "Interactive regex tester with real-time matching, group highlighting, cheat sheet, pattern library, and explanation mode that breaks down complex patterns.",
            "tech": ["HTML", "CSS", "JavaScript", "Web Workers"],
            "difficulty": "Beginner",
            "time": "2-3 hours",
        },
    ],
    "Games & Interactive": [
        {
            "name": "Multiplayer Trivia Game",
            "desc": "Real-time multiplayer quiz with room codes, live leaderboard, power-ups, custom question packs, and spectator mode. Smooth animations throughout.",
            "tech": ["React", "Socket.io", "Node.js", "Redis"],
            "difficulty": "Intermediate",
            "time": "6-8 hours",
        },
        {
            "name": "2D Platformer (Pixel Quest)",
            "desc": "Retro pixel-art platformer with physics engine, level editor, collectibles, enemies with AI pathfinding, and local high-score board.",
            "tech": ["HTML5 Canvas", "JavaScript", "Web Audio API"],
            "difficulty": "Intermediate",
            "time": "8-10 hours",
        },
        {
            "name": "Chess Engine with AI",
            "desc": "Fully playable chess with drag-and-drop, move validation, AI opponent (minimax + alpha-beta pruning), game history, and PGN export.",
            "tech": ["JavaScript", "Canvas/SVG", "Web Workers"],
            "difficulty": "Advanced",
            "time": "10-14 hours",
        },
        {
            "name": "Interactive Data Story",
            "desc": "Scroll-driven narrative visualization combining data journalism with interactive charts. Readers explore data by scrolling through animated story chapters.",
            "tech": ["D3.js", "ScrollTrigger", "GSAP", "HTML/CSS"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
        {
            "name": "Typing Speed Racer",
            "desc": "Competitive typing game with WPM tracking, accuracy stats, multiplayer races, difficulty levels, and progression system with achievements.",
            "tech": ["React", "WebSocket", "Node.js", "MongoDB"],
            "difficulty": "Beginner",
            "time": "3-4 hours",
        },
    ],
    "Cloud & DevOps": [
        {
            "name": "CI/CD Pipeline Dashboard",
            "desc": "Unified view of all CI/CD pipelines across GitHub Actions, GitLab CI, and Jenkins. Build status, deployment history, rollback controls, and Slack notifications.",
            "tech": ["Next.js", "GitHub API", "Docker", "WebSocket"],
            "difficulty": "Advanced",
            "time": "8-10 hours",
        },
        {
            "name": "Container Orchestration Monitor",
            "desc": "Real-time Kubernetes cluster dashboard with pod status, resource utilization, log streaming, and auto-scaling visualizations.",
            "tech": ["React", "Kubernetes API", "Grafana", "Prometheus"],
            "difficulty": "Expert",
            "time": "12-16 hours",
        },
        {
            "name": "Serverless Function Deployer",
            "desc": "One-click serverless function deployment tool with code editor, environment variables manager, cold-start metrics, and execution logs.",
            "tech": ["Next.js", "AWS Lambda", "Vercel Functions", "Monaco Editor"],
            "difficulty": "Advanced",
            "time": "6-8 hours",
        },
        {
            "name": "Infrastructure Cost Calculator",
            "desc": "Estimate and compare cloud costs across AWS, GCP, and Azure. Save configurations, forecast spend, and get optimization recommendations.",
            "tech": ["React", "Cloud Pricing APIs", "Chart.js", "Node.js"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
        {
            "name": "Uptime Monitor & Status Page",
            "desc": "Monitor website/API health with ping checks, latency tracking, incident management, and a public status page. Email/SMS alerting on downtime.",
            "tech": ["Node.js", "Cron", "PostgreSQL", "React", "Twilio"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
    ],
    "Mobile & PWA": [
        {
            "name": "Habit Tracker PWA",
            "desc": "Offline-first habit tracking app with streak counting, heatmap calendar, push notifications, weekly reports, and motivational quotes.",
            "tech": ["React", "Service Workers", "IndexedDB", "Web Push API"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
        {
            "name": "Expense Splitter (SplitEase)",
            "desc": "Group expense splitting with real-time balance calculation, payment integration, receipt scanning (OCR), and settlement suggestions.",
            "tech": ["React Native / PWA", "Node.js", "Tesseract.js", "Stripe"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
        {
            "name": "Workout & Fitness Logger",
            "desc": "Exercise tracking with custom routines, progress charts, rest timers, PR tracking, and body measurement logs. Works offline.",
            "tech": ["PWA", "IndexedDB", "Chart.js", "Service Workers"],
            "difficulty": "Beginner",
            "time": "3-5 hours",
        },
        {
            "name": "QR Code Generator & Scanner",
            "desc": "Generate styled QR codes with logos, colors, and shapes. Scan QR codes via camera with history and batch generation support.",
            "tech": ["React", "qrcode.js", "WebRTC Camera API", "Canvas"],
            "difficulty": "Beginner",
            "time": "2-3 hours",
        },
        {
            "name": "Offline Notes App (Notecraft)",
            "desc": "Rich-text note-taking with folders, tags, search, markdown support, and cloud sync when online. Dark mode and focus mode included.",
            "tech": ["PWA", "Tiptap Editor", "IndexedDB", "CRDTs"],
            "difficulty": "Intermediate",
            "time": "5-7 hours",
        },
    ],
    "IoT & Hardware": [
        {
            "name": "Smart Attendance System (RFID)",
            "desc": "IoT attendance tracker using RFID tags with ESP32, real-time cloud sync, admin dashboard, attendance reports, and late-arrival alerts.",
            "tech": ["Arduino/ESP32", "MQTT", "Node.js", "React Dashboard"],
            "difficulty": "Advanced",
            "time": "8-12 hours",
        },
        {
            "name": "Home Environment Monitor",
            "desc": "Temperature, humidity, and air quality monitoring with historical charts, threshold alerts, and smart device integration via MQTT.",
            "tech": ["ESP32", "DHT22/BME280", "InfluxDB", "Grafana"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
        {
            "name": "Plant Watering Automation",
            "desc": "Soil moisture monitoring with automated watering schedule, camera feed for plant health, and mobile notifications when plants need attention.",
            "tech": ["Raspberry Pi", "Soil Sensor", "Python", "Telegram Bot"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
        {
            "name": "Smart Door Lock System",
            "desc": "NFC/PIN-based door lock with access logs, remote unlock via app, visitor management, and emergency override. Secure BLE communication.",
            "tech": ["ESP32", "NFC Module", "React Native", "Firebase"],
            "difficulty": "Advanced",
            "time": "10-14 hours",
        },
    ],
    "Security & Auth": [
        {
            "name": "OAuth2 Authentication Service",
            "desc": "Full OAuth2/OIDC provider with Google/GitHub social login, JWT tokens, refresh rotation, RBAC, and 2FA (TOTP). Production-grade security.",
            "tech": ["Node.js", "Passport.js", "JWT", "PostgreSQL", "Redis"],
            "difficulty": "Advanced",
            "time": "6-8 hours",
        },
        {
            "name": "Password Manager (Vault)",
            "desc": "Encrypted password vault with AES-256, master password derivation (Argon2), browser extension, auto-fill, and secure sharing.",
            "tech": ["Electron", "React", "Node.js", "Crypto APIs"],
            "difficulty": "Expert",
            "time": "12-16 hours",
        },
        {
            "name": "Vulnerability Scanner",
            "desc": "Automated security scanner for web apps - checks for XSS, SQLi, CSRF, misconfigurations, and generates detailed remediation reports.",
            "tech": ["Python", "Scrapy", "Beautiful Soup", "FastAPI"],
            "difficulty": "Expert",
            "time": "10-14 hours",
        },
        {
            "name": "Rate Limiter & API Gateway",
            "desc": "Configurable API gateway with rate limiting, IP whitelisting, request logging, abuse detection, and real-time traffic analytics.",
            "tech": ["Node.js", "Redis", "Express", "React Dashboard"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
    ],
    "Creative & Media": [
        {
            "name": "Collaborative Whiteboard",
            "desc": "Real-time drawing canvas with layers, shapes, text, image upload, undo/redo, and multi-user collaboration via WebRTC.",
            "tech": ["React", "Canvas API", "WebRTC", "Socket.io"],
            "difficulty": "Advanced",
            "time": "8-10 hours",
        },
        {
            "name": "Meme Generator Studio",
            "desc": "Drag-and-drop meme editor with template library, custom text styling, image filters, GIF export, and trending meme feed.",
            "tech": ["React", "Canvas API", "Cloudinary", "Node.js"],
            "difficulty": "Beginner",
            "time": "3-4 hours",
        },
        {
            "name": "Podcast Hosting Platform",
            "desc": "Upload, host, and distribute podcasts with RSS feed generation, episode analytics, embedded player widget, and AI-generated transcripts.",
            "tech": ["Next.js", "AWS S3", "Whisper API", "PostgreSQL"],
            "difficulty": "Advanced",
            "time": "10-14 hours",
        },
        {
            "name": "Color Palette Generator",
            "desc": "AI-driven color palette generator from images or moods. Includes contrast checker, CSS/Tailwind export, palette saving, and accessibility scoring.",
            "tech": ["React", "Canvas API", "Color Theory Algorithms"],
            "difficulty": "Beginner",
            "time": "2-3 hours",
        },
        {
            "name": "Video Thumbnail Maker",
            "desc": "Template-based thumbnail designer with text overlays, background remover, batch export, and integration with YouTube to auto-suggest styles.",
            "tech": ["React", "Canvas API", "Remove.bg API", "Node.js"],
            "difficulty": "Intermediate",
            "time": "4-6 hours",
        },
    ],
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PDF CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class RoadmapPDF(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "A4")
        self.set_auto_page_break(auto=True, margin=20)

    # ── Utility ────────────────────────────────────────────────────────────
    def _dark_page(self):
        self.set_fill_color(*DARK_BG)
        self.rect(0, 0, 210, 297, "F")

    def _gradient_bar(self, y, h, color_left, color_right):
        """Draw a simple horizontal gradient bar."""
        steps = 100
        w = 210 / steps
        for i in range(steps):
            t = i / steps
            r = int(color_left[0] + (color_right[0] - color_left[0]) * t)
            g = int(color_left[1] + (color_right[1] - color_left[1]) * t)
            b = int(color_left[2] + (color_right[2] - color_left[2]) * t)
            self.set_fill_color(r, g, b)
            self.rect(i * w, y, w + 0.5, h, "F")

    # ── Cover Page ─────────────────────────────────────────────────────────
    def cover_page(self):
        self.add_page()
        self._dark_page()

        # Top gradient bar
        self._gradient_bar(0, 4, ACCENT_BLUE, ACCENT_PURPLE)

        # Decorative circles
        self.set_draw_color(*ACCENT_BLUE)
        self.set_line_width(0.3)
        for r in range(20, 80, 12):
            self.ellipse(105 - r, 80 - r, r * 2, r * 2, "D")

        # Title
        self.set_y(55)
        self.set_font("Helvetica", "B", 42)
        self.set_text_color(*WHITE)
        self.cell(0, 18, "PROJECT ROADMAP", align="C", new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", "", 16)
        self.set_text_color(*ACCENT_BLUE)
        self.cell(0, 10, "CURATED BY SHAURYA MISHRA // 2026", align="C", new_x="LMARGIN", new_y="NEXT")

        # Divider
        self.ln(5)
        self._gradient_bar(self.get_y(), 1, ACCENT_PURPLE, ACCENT_BLUE)
        self.ln(8)

        # Subtitle
        self.set_font("Helvetica", "", 12)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 7,
            sanitize(
                "A comprehensive collection of 50+ projects curated by Shaurya Mishra.\n"
                "Designed to elevate engineering, architecture, and coding skills.\n"
                "From beginner web apps to expert-level distributed systems."
            ),
            align="C"
        )

        self.ln(12)

        # Stats boxes
        total_projects = sum(len(v) for v in PROJECTS.values())
        stats = [
            (str(total_projects), "Projects", ACCENT_BLUE),
            (str(len(PROJECTS)), "Categories", ACCENT_PURPLE),
            ("4", "Difficulty Tiers", ACCENT_GREEN),
            ("150+", "Est. Build Hours", ACCENT_ORANGE),
        ]
        box_w = 40
        gap = 5
        total_w = len(stats) * box_w + (len(stats) - 1) * gap
        start_x = (210 - total_w) / 2

        for i, (val, label, color) in enumerate(stats):
            x = start_x + i * (box_w + gap)
            y = self.get_y()

            self.set_fill_color(*CARD_BG)
            self.rect(x, y, box_w, 28, "F")

            # Top accent line
            self.set_fill_color(*color)
            self.rect(x, y, box_w, 2, "F")

            self.set_xy(x, y + 5)
            self.set_font("Helvetica", "B", 20)
            self.set_text_color(*color)
            self.cell(box_w, 10, val, align="C", new_x="LMARGIN", new_y="NEXT")

            self.set_xy(x, y + 17)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*MUTED)
            self.cell(box_w, 6, label, align="C")

        self.ln(40)

        # Difficulty Legend
        self.set_y(200)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*WHITE)
        self.cell(0, 8, "DIFFICULTY LEVELS", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

        legend_items = [
            ("Beginner", "Perfect for newcomers", ACCENT_GREEN),
            ("Intermediate", "Some experience needed", ACCENT_ORANGE),
            ("Advanced", "Strong fundamentals required", ACCENT_RED),
            ("Expert", "Deep expertise in domain", ACCENT_PURPLE),
        ]
        for label, desc, color in legend_items:
            self.set_x(40)
            self.set_fill_color(*color)
            self.rect(self.get_x(), self.get_y() + 2, 8, 4, "F")
            self.set_x(52)
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(*color)
            self.cell(30, 8, label)
            self.set_font("Helvetica", "", 9)
            self.set_text_color(*MUTED)
            self.cell(0, 8, f"  {desc}", new_x="LMARGIN", new_y="NEXT")

        # Footer
        self.set_y(260)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DIM)
        self.cell(0, 5, "Curated by Shaurya Mishra  |  Roadmap 2026", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, "Generated April 2026", align="C")

        # Bottom gradient bar
        self._gradient_bar(293, 4, ACCENT_PURPLE, ACCENT_BLUE)

    # ── Table of Contents ──────────────────────────────────────────────────
    def toc_page(self):
        self.add_page()
        self._dark_page()
        self._gradient_bar(0, 2, ACCENT_BLUE, ACCENT_PURPLE)

        self.set_y(15)
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(*WHITE)
        self.cell(0, 12, "TABLE OF CONTENTS", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self._gradient_bar(self.get_y(), 0.5, ACCENT_PURPLE, ACCENT_BLUE)
        self.ln(8)

        for i, (cat, projects) in enumerate(PROJECTS.items(), 1):
            color = CATEGORY_COLORS.get(cat, ACCENT_BLUE)

            self.set_fill_color(*CARD_BG)
            y = self.get_y()
            self.rect(15, y, 180, 18, "F")

            # Left accent bar
            self.set_fill_color(*color)
            self.rect(15, y, 3, 18, "F")

            self.set_xy(22, y + 2)
            self.set_font("Helvetica", "B", 12)
            self.set_text_color(*color)
            icon = CATEGORY_ICONS.get(cat, "")
            self.cell(120, 7, sanitize(f"{i:02d}.  {icon}  {cat}"))

            self.set_xy(22, y + 10)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*MUTED)
            self.cell(120, 6, f"{len(projects)} projects")

            self.set_xy(150, y + 5)
            self.set_font("Helvetica", "", 9)
            self.set_text_color(*DIM)
            difficulties = set(p["difficulty"] for p in projects)
            self.cell(40, 7, " / ".join(sorted(difficulties)), align="R")

            self.set_y(y + 22)

    # ── Category Section ───────────────────────────────────────────────────
    def category_page(self, category, projects):
        color = CATEGORY_COLORS.get(category, ACCENT_BLUE)
        self.add_page()
        self._dark_page()

        # Header bar
        self._gradient_bar(0, 3, color, ACCENT_BLUE if color != ACCENT_BLUE else ACCENT_PURPLE)

        self.set_y(15)
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*color)
        icon = CATEGORY_ICONS.get(category, "")
        self.cell(0, 12, sanitize(f"{icon}  {category}"), align="C", new_x="LMARGIN", new_y="NEXT")

        self.ln(2)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*MUTED)
        self.cell(0, 6, f"{len(projects)} Projects  |  Roadmap 2026", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self._gradient_bar(self.get_y(), 0.5, color, DARK_BG)
        self.ln(8)

        for i, project in enumerate(projects):
            self._project_card(project, color, i + 1)

    def _project_card(self, project, cat_color, num):
        card_h = 52
        if self.get_y() + card_h > 275:
            self.add_page()
            self._dark_page()
            self._gradient_bar(0, 2, cat_color, DARK_BG)
            self.set_y(15)

        y = self.get_y()

        # Card background
        self.set_fill_color(*CARD_BG)
        self.rect(15, y, 180, card_h, "F")

        # Left accent strip
        self.set_fill_color(*cat_color)
        self.rect(15, y, 3, card_h, "F")

        # Project number badge
        self.set_fill_color(*cat_color)
        self.rect(20, y + 3, 10, 7, "F")
        self.set_xy(20, y + 3)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*DARK_BG)
        self.cell(10, 7, f"#{num:02d}", align="C")

        # Project name
        self.set_xy(33, y + 3)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*WHITE)
        self.cell(120, 7, project["name"])

        # Difficulty badge
        diff = project["difficulty"]
        diff_color = DIFFICULTY_COLORS.get(diff, MUTED)
        self.set_xy(155, y + 3)
        self.set_fill_color(*diff_color)
        self.rect(155, y + 3, 38, 7, "F")
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*DARK_BG)
        self.cell(38, 7, diff.upper(), align="C")

        # Description
        self.set_xy(22, y + 14)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*MUTED)
        # Truncate description to fit
        desc = project["desc"]
        self.multi_cell(170, 4, sanitize(desc))

        # Tech stack pills
        tech_y = y + 34
        self.set_xy(22, tech_y)
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*MUTED)
        self.cell(15, 5, "STACK:")

        pill_x = 39
        for tech in project["tech"]:
            pill_w = self.get_string_width(tech) + 6
            if pill_x + pill_w > 190:
                break
            self.set_fill_color(35, 40, 48)
            self.rect(pill_x, tech_y, pill_w, 5, "F")
            self.set_xy(pill_x, tech_y)
            self.set_text_color(*cat_color)
            self.set_font("Helvetica", "", 6)
            self.cell(pill_w, 5, tech, align="C")
            pill_x += pill_w + 2

        # Time estimate
        self.set_xy(22, y + 42)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*DIM)
        self.cell(0, 5, f"Est. Time: {project['time']}")

        self.set_y(y + card_h + 5)

    # ── Summary Page ───────────────────────────────────────────────────────
    def summary_page(self):
        self.add_page()
        self._dark_page()
        self._gradient_bar(0, 3, ACCENT_PURPLE, ACCENT_BLUE)

        self.set_y(20)
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(*WHITE)
        self.cell(0, 12, "PROJECT SUMMARY", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self._gradient_bar(self.get_y(), 0.5, ACCENT_BLUE, ACCENT_PURPLE)
        self.ln(8)

        # Category summary table
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(*CARD_BG)

        # Header row
        self.set_x(15)
        self.set_text_color(*ACCENT_BLUE)
        self.cell(80, 8, "  CATEGORY", fill=True)
        self.cell(25, 8, "PROJECTS", fill=True, align="C")
        self.cell(35, 8, "DIFFICULTY", fill=True, align="C")
        self.cell(40, 8, "EST. TIME", fill=True, align="C")
        self.ln()

        self.set_font("Helvetica", "", 8)
        total_projects = 0
        for cat, projects in PROJECTS.items():
            color = CATEGORY_COLORS.get(cat, ACCENT_BLUE)
            y = self.get_y()

            self.set_x(15)
            self.set_fill_color(18, 22, 28)
            self.set_text_color(*color)
            self.cell(80, 7, sanitize(f"  {cat}"), fill=True)

            self.set_text_color(*WHITE)
            self.cell(25, 7, str(len(projects)), fill=True, align="C")

            diffs = [p["difficulty"] for p in projects]
            avg_diff = max(set(diffs), key=diffs.count)
            d_color = DIFFICULTY_COLORS.get(avg_diff, MUTED)
            self.set_text_color(*d_color)
            self.cell(35, 7, avg_diff, fill=True, align="C")

            # Calculate total time
            self.set_text_color(*MUTED)
            self.cell(40, 7, f"{len(projects) * 6}+ hrs", fill=True, align="C")
            self.ln()

            total_projects += len(projects)

        # Total row
        self.ln(2)
        self.set_x(15)
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(*CARD_BG)
        self.set_text_color(*ACCENT_BLUE)
        self.cell(80, 8, f"  TOTAL", fill=True)
        self.set_text_color(*WHITE)
        self.cell(25, 8, str(total_projects), fill=True, align="C")
        self.cell(35, 8, "All Levels", fill=True, align="C")
        self.set_text_color(*ACCENT_GREEN)
        self.cell(40, 8, "300+ hrs", fill=True, align="C")

        # About section
        self.ln(15)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(*WHITE)
        self.cell(0, 10, "ABOUT THE ROADMAP", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

        self.set_x(20)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*MUTED)
        about_text = (
            "This roadmap is a meticulously compiled guide of 50+ real-world software engineering "
            "projects curated by Shaurya Mishra. Designed to bridge the gap between academic coding "
            "and professional-grade software development, it provides actionable specifications "
            "and architectural profiles for high-impact building blocks.\n\n"
            "Core disciplines covered:\n"
            "  - Next-generation Web Applications and Scalable Services\n"
            "  - Machine Learning models and Agentic Systems\n"
            "  - Distributed Systems, Cloud Automation, and Security Vaults\n"
            "  - Interactive graphics and Game Development engines\n"
            "  - IoT Hardware control and Edge computing interfaces\n\n"
            "Each module contains curated target stacks, functional specifications, "
            "and precise estimation bounds to accelerate hands-on engineering experience."
        )
        self.multi_cell(170, 5, about_text)

        # Footer
        self.ln(10)
        self._gradient_bar(self.get_y(), 0.5, ACCENT_PURPLE, ACCENT_BLUE)
        self.ln(5)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DIM)
        self.cell(0, 5, "github.com/shaurya1906  |  Curated by Shaurya Mishra  |  2026", align="C")

        # Bottom bar
        self._gradient_bar(293, 4, ACCENT_BLUE, ACCENT_PURPLE)

    # ── How To Use Page ────────────────────────────────────────────────────
    def how_to_page(self):
        self.add_page()
        self._dark_page()
        self._gradient_bar(0, 3, ACCENT_GREEN, ACCENT_CYAN)

        self.set_y(20)
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*WHITE)
        self.cell(0, 12, "HOW TO USE THIS ROADMAP", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self._gradient_bar(self.get_y(), 0.5, ACCENT_GREEN, ACCENT_CYAN)
        self.ln(10)

        steps = [
            ("01", "PICK YOUR LEVEL", "Start with projects matching your skill level. Beginners start with portfolio sites or CLI tools. Work up to Expert projects.", ACCENT_GREEN),
            ("02", "OPEN WORKSPACE", "Launch your preferred IDE (e.g. VS Code, Cursor) and open a fresh workspace. Each project is fully self-contained.", ACCENT_BLUE),
            ("03", "DESCRIBE THE PROJECT", "Paste the project specifications or design outlines as your starting blueprint. Map out the database schema, data flows, and routing.", ACCENT_PURPLE),
            ("04", "APPROVE & BUILD", "Review the plan, approve it, and watch the agent scaffold your entire project - code, styles, and config.", ACCENT_ORANGE),
            ("05", "ITERATE & POLISH", "Use follow-up prompts to refine the UI, add features, fix bugs, and deploy. The agent handles it all.", ACCENT_PINK),
            ("06", "DEPLOY TO GITHUB", "Push your finished project to GitHub. Setup comprehensive unit tests, configure CD pipelines, and make it live.", ACCENT_CYAN),
        ]

        for num, title, desc, color in steps:
            y = self.get_y()
            if y + 30 > 275:
                self.add_page()
                self._dark_page()
                self.set_y(15)
                y = 15

            # Step card
            self.set_fill_color(*CARD_BG)
            self.rect(15, y, 180, 28, "F")

            # Number badge
            self.set_fill_color(*color)
            self.rect(15, y, 22, 28, "F")
            self.set_xy(15, y + 8)
            self.set_font("Helvetica", "B", 16)
            self.set_text_color(*DARK_BG)
            self.cell(22, 12, num, align="C")

            # Title
            self.set_xy(42, y + 3)
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(*color)
            self.cell(150, 7, title)

            # Description
            self.set_xy(42, y + 12)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*MUTED)
            self.multi_cell(148, 4, desc)

            self.set_y(y + 33)

        # Bottom CTA
        self.ln(10)
        self.set_fill_color(*CARD_BG)
        y = self.get_y()
        self.rect(25, y, 160, 25, "F")
        self._gradient_bar(y, 2, ACCENT_BLUE, ACCENT_PURPLE)

        self.set_xy(25, y + 6)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*WHITE)
        self.cell(160, 7, "Ready to build? Open your editor and start creating!", align="C", new_x="LMARGIN", new_y="NEXT")

        self.set_xy(25, y + 15)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*ACCENT_BLUE)
        self.cell(160, 6, "github.com/shaurya1906  |  Roadmap 2026  |  All rights reserved", align="C")

        self._gradient_bar(293, 4, ACCENT_GREEN, ACCENT_CYAN)

    # ── Build the full PDF ─────────────────────────────────────────────────
    def build(self, output_path):
        self.cover_page()
        self.toc_page()
        self.how_to_page()

        for cat, projects in PROJECTS.items():
            self.category_page(cat, projects)

        self.summary_page()
        self.output(output_path)
        print(f"[OK] PDF generated: {output_path}")
        total = sum(len(v) for v in PROJECTS.values())
        print(f"     {total} projects across {len(PROJECTS)} categories")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Project_Roadmap_2026.pdf")
    pdf = RoadmapPDF()
    pdf.build(output)
