/* ==========================================================================
   ROADMAP 2026 — app.js
   Dynamic Filter Engine · 3D Perspective Matrix · Interactive Cyber Prompts
   ========================================================================== */

(function () {
  'use strict';

  // ── 1. EMBEDDED PROJECT DATABASE ────────────────────────────────────────
  const PROJECTS_DB = {
    "Web Development": [
        {
            "name": "E-Commerce Storefront",
            "desc": "Full-featured online store with product catalog, cart system, Stripe checkout, admin dashboard, and order tracking. Responsive design with skeleton loaders.",
            "tech": [
                "Next.js",
                "Stripe API",
                "PostgreSQL",
                "Prisma"
            ],
            "difficulty": "Advanced",
            "time": "8-12 hours"
        },
        {
            "name": "Real-Time Chat Application",
            "desc": "WebSocket-powered chat with rooms, typing indicators, message reactions, file uploads, and online presence. End-to-end encrypted messaging.",
            "tech": [
                "React",
                "Socket.io",
                "Node.js",
                "MongoDB"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        },
        {
            "name": "Blog Platform with CMS",
            "desc": "Markdown-based blogging platform with rich text editor, SEO optimization, RSS feeds, analytics dashboard, and comment system with moderation.",
            "tech": [
                "Next.js",
                "MDX",
                "Supabase",
                "Vercel"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        },
        {
            "name": "Music Streaming App (Retrowave)",
            "desc": "Full music player with decade browsing, search, playlists, audio visualization, and streaming via YouTube Music API. Neon retrowave aesthetic.",
            "tech": [
                "HTML/CSS/JS",
                "Python Flask",
                "yt-dlp",
                "Web Audio API"
            ],
            "difficulty": "Advanced",
            "time": "10-15 hours"
        },
        {
            "name": "Recipe Sharing Platform",
            "desc": "Community-driven recipe site with ingredient-based search, step-by-step instructions, nutritional info, meal planning calendar, and grocery list generator.",
            "tech": [
                "React",
                "Node.js",
                "PostgreSQL",
                "Cloudinary"
            ],
            "difficulty": "Intermediate",
            "time": "6-8 hours"
        }
    ],
    "AI & Machine Learning": [
        {
            "name": "Synthetic AGI Orchestrator",
            "desc": "Multi-model AI synthesis engine that routes queries to GPT, Claude, and Gemini, then merges outputs for maximum accuracy. Features consensus scoring and confidence metrics.",
            "tech": [
                "Python",
                "FastAPI",
                "OpenAI API",
                "Anthropic API",
                "Gemini API"
            ],
            "difficulty": "Expert",
            "time": "12-18 hours"
        },
        {
            "name": "AI-Powered Code Reviewer",
            "desc": "Automated PR review bot that analyzes code quality, security vulnerabilities, performance bottlenecks, and suggests improvements using LLM reasoning.",
            "tech": [
                "Python",
                "GitHub API",
                "Gemini API",
                "FastAPI"
            ],
            "difficulty": "Advanced",
            "time": "6-8 hours"
        },
        {
            "name": "RAG Knowledge Base",
            "desc": "Retrieval-Augmented Generation system with document ingestion, vector embeddings, semantic search, and conversational Q&A with source citations.",
            "tech": [
                "Python",
                "LangChain",
                "ChromaDB",
                "OpenAI Embeddings"
            ],
            "difficulty": "Advanced",
            "time": "5-7 hours"
        },
        {
            "name": "Sentiment Analysis Dashboard",
            "desc": "Real-time social media sentiment tracker with trend visualization, entity extraction, topic modeling, and alerting for brand mentions.",
            "tech": [
                "Python",
                "HuggingFace",
                "Streamlit",
                "Twitter API"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        },
        {
            "name": "AI Image Generator & Editor",
            "desc": "Text-to-image generation interface with inpainting, outpainting, style transfer, and prompt engineering presets. Gallery with favorites and sharing.",
            "tech": [
                "React",
                "Stable Diffusion API",
                "Node.js",
                "S3"
            ],
            "difficulty": "Advanced",
            "time": "8-10 hours"
        },
        {
            "name": "Intelligent Resume Builder",
            "desc": "AI-powered resume creator that analyzes job descriptions, suggests bullet points, optimizes for ATS, and generates multiple format exports (PDF, DOCX).",
            "tech": [
                "Next.js",
                "OpenAI API",
                "Puppeteer",
                "PostgreSQL"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        }
    ],
    "Data & Analytics": [
        {
            "name": "IPL Match Predictor",
            "desc": "Data-driven sports prediction engine using historical stats, player form, venue analysis, and ensemble ML models. Live leaderboard and prediction accuracy tracking.",
            "tech": [
                "Python",
                "Pandas",
                "Scikit-learn",
                "React",
                "D3.js"
            ],
            "difficulty": "Advanced",
            "time": "10-14 hours"
        },
        {
            "name": "Finance Tracker Dashboard",
            "desc": "Personal finance manager with bank sync, expense categorization, budget alerts, investment tracking, and interactive charts with drill-down capability.",
            "tech": [
                "React",
                "Chart.js",
                "Node.js",
                "Plaid API"
            ],
            "difficulty": "Intermediate",
            "time": "6-8 hours"
        },
        {
            "name": "COVID/Health Data Visualizer",
            "desc": "Interactive choropleth maps and time-series charts for health data exploration. Supports custom dataset uploads and comparison views.",
            "tech": [
                "D3.js",
                "Mapbox",
                "Python Flask",
                "Pandas"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        },
        {
            "name": "GitHub Analytics Dashboard",
            "desc": "Visualize your coding activity - commit heatmaps, language breakdowns, PR metrics, contribution streaks, and repository health scores.",
            "tech": [
                "Next.js",
                "GitHub GraphQL API",
                "Recharts",
                "Vercel"
            ],
            "difficulty": "Intermediate",
            "time": "4-5 hours"
        },
        {
            "name": "Real-Time Stock Screener",
            "desc": "Live stock data with technical indicators, candlestick charts, watchlists, alerts, and fundamental analysis filters. Paper trading simulator included.",
            "tech": [
                "React",
                "WebSocket",
                "Alpha Vantage API",
                "TradingView"
            ],
            "difficulty": "Advanced",
            "time": "8-10 hours"
        }
    ],
    "Developer Tools & CLI": [
        {
            "name": "CLI Task Manager (Taskforge)",
            "desc": "Terminal-based project management with Kanban boards, time tracking, git integration, priority sorting, and Pomodoro timer. Syncs to cloud.",
            "tech": [
                "Python",
                "Rich",
                "Click",
                "SQLite"
            ],
            "difficulty": "Beginner",
            "time": "3-4 hours"
        },
        {
            "name": "API Mock Server Generator",
            "desc": "Auto-generate realistic mock APIs from OpenAPI/Swagger specs with faker-powered data, latency simulation, and error scenario testing.",
            "tech": [
                "Node.js",
                "Express",
                "Faker.js",
                "YAML"
            ],
            "difficulty": "Intermediate",
            "time": "3-5 hours"
        },
        {
            "name": "Code Snippet Manager",
            "desc": "Searchable, tagged code snippet library with syntax highlighting, multi-language support, VS Code extension integration, and team sharing.",
            "tech": [
                "Electron",
                "React",
                "SQLite",
                "Prism.js"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        },
        {
            "name": "Log Analyzer & Visualizer",
            "desc": "Parse, filter, and visualize application logs with pattern detection, error clustering, timeline views, and alert rule configuration.",
            "tech": [
                "Python",
                "Elasticsearch",
                "Kibana",
                "FastAPI"
            ],
            "difficulty": "Advanced",
            "time": "6-8 hours"
        },
        {
            "name": "Database Schema Designer",
            "desc": "Visual ERD builder with drag-and-drop tables, relationship mapping, SQL/migration export, and schema versioning. Supports PostgreSQL, MySQL, SQLite.",
            "tech": [
                "React",
                "Canvas API",
                "Node.js",
                "SQL Generator"
            ],
            "difficulty": "Advanced",
            "time": "8-10 hours"
        },
        {
            "name": "Regex Pattern Playground",
            "desc": "Interactive regex tester with real-time matching, group highlighting, cheat sheet, pattern library, and explanation mode that breaks down complex patterns.",
            "tech": [
                "HTML",
                "CSS",
                "JavaScript",
                "Web Workers"
            ],
            "difficulty": "Beginner",
            "time": "2-3 hours"
        }
    ],
    "Games & Interactive": [
        {
            "name": "Multiplayer Trivia Game",
            "desc": "Real-time multiplayer quiz with room codes, live leaderboard, power-ups, custom question packs, and spectator mode. Smooth animations throughout.",
            "tech": [
                "React",
                "Socket.io",
                "Node.js",
                "Redis"
            ],
            "difficulty": "Intermediate",
            "time": "6-8 hours"
        },
        {
            "name": "2D Platformer (Pixel Quest)",
            "desc": "Retro pixel-art platformer with physics engine, level editor, collectibles, enemies with AI pathfinding, and local high-score board.",
            "tech": [
                "HTML5 Canvas",
                "JavaScript",
                "Web Audio API"
            ],
            "difficulty": "Intermediate",
            "time": "8-10 hours"
        },
        {
            "name": "Chess Engine with AI",
            "desc": "Fully playable chess with drag-and-drop, move validation, AI opponent (minimax + alpha-beta pruning), game history, and PGN export.",
            "tech": [
                "JavaScript",
                "Canvas/SVG",
                "Web Workers"
            ],
            "difficulty": "Advanced",
            "time": "10-14 hours"
        },
        {
            "name": "Interactive Data Story",
            "desc": "Scroll-driven narrative visualization combining data journalism with interactive charts. Readers explore data by scrolling through animated story chapters.",
            "tech": [
                "D3.js",
                "ScrollTrigger",
                "GSAP",
                "HTML/CSS"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        },
        {
            "name": "Typing Speed Racer",
            "desc": "Competitive typing game with WPM tracking, accuracy stats, multiplayer races, difficulty levels, and progression system with achievements.",
            "tech": [
                "React",
                "WebSocket",
                "Node.js",
                "MongoDB"
            ],
            "difficulty": "Beginner",
            "time": "3-4 hours"
        }
    ],
    "Cloud & DevOps": [
        {
            "name": "CI/CD Pipeline Dashboard",
            "desc": "Unified view of all CI/CD pipelines across GitHub Actions, GitLab CI, and Jenkins. Build status, deployment history, rollback controls, and Slack notifications.",
            "tech": [
                "Next.js",
                "GitHub API",
                "Docker",
                "WebSocket"
            ],
            "difficulty": "Advanced",
            "time": "8-10 hours"
        },
        {
            "name": "Container Orchestration Monitor",
            "desc": "Real-time Kubernetes cluster dashboard with pod status, resource utilization, log streaming, and auto-scaling visualizations.",
            "tech": [
                "React",
                "Kubernetes API",
                "Grafana",
                "Prometheus"
            ],
            "difficulty": "Expert",
            "time": "12-16 hours"
        },
        {
            "name": "Serverless Function Deployer",
            "desc": "One-click serverless function deployment tool with code editor, environment variables manager, cold-start metrics, and execution logs.",
            "tech": [
                "Next.js",
                "AWS Lambda",
                "Vercel Functions",
                "Monaco Editor"
            ],
            "difficulty": "Advanced",
            "time": "6-8 hours"
        },
        {
            "name": "Infrastructure Cost Calculator",
            "desc": "Estimate and compare cloud costs across AWS, GCP, and Azure. Save configurations, forecast spend, and get optimization recommendations.",
            "tech": [
                "React",
                "Cloud Pricing APIs",
                "Chart.js",
                "Node.js"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        },
        {
            "name": "Uptime Monitor & Status Page",
            "desc": "Monitor website/API health with ping checks, latency tracking, incident management, and a public status page. Email/SMS alerting on downtime.",
            "tech": [
                "Node.js",
                "Cron",
                "PostgreSQL",
                "React",
                "Twilio"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        }
    ],
    "Mobile & PWA": [
        {
            "name": "Habit Tracker PWA",
            "desc": "Offline-first habit tracking app with streak counting, heatmap calendar, push notifications, weekly reports, and motivational quotes.",
            "tech": [
                "React",
                "Service Workers",
                "IndexedDB",
                "Web Push API"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        },
        {
            "name": "Expense Splitter (SplitEase)",
            "desc": "Group expense splitting with real-time balance calculation, payment integration, receipt scanning (OCR), and settlement suggestions.",
            "tech": [
                "React Native / PWA",
                "Node.js",
                "Tesseract.js",
                "Stripe"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        },
        {
            "name": "Workout & Fitness Logger",
            "desc": "Exercise tracking with custom routines, progress charts, rest timers, PR tracking, and body measurement logs. Works offline.",
            "tech": [
                "PWA",
                "IndexedDB",
                "Chart.js",
                "Service Workers"
            ],
            "difficulty": "Beginner",
            "time": "3-5 hours"
        },
        {
            "name": "QR Code Generator & Scanner",
            "desc": "Generate styled QR codes with logos, colors, and shapes. Scan QR codes via camera with history and batch generation support.",
            "tech": [
                "React",
                "qrcode.js",
                "WebRTC Camera API",
                "Canvas"
            ],
            "difficulty": "Beginner",
            "time": "2-3 hours"
        },
        {
            "name": "Offline Notes App (Notecraft)",
            "desc": "Rich-text note-taking with folders, tags, search, markdown support, and cloud sync when online. Dark mode and focus mode included.",
            "tech": [
                "PWA",
                "Tiptap Editor",
                "IndexedDB",
                "CRDTs"
            ],
            "difficulty": "Intermediate",
            "time": "5-7 hours"
        }
    ],
    "IoT & Hardware": [
        {
            "name": "Smart Attendance System (RFID)",
            "desc": "IoT attendance tracker using RFID tags with ESP32, real-time cloud sync, admin dashboard, attendance reports, and late-arrival alerts.",
            "tech": [
                "Arduino/ESP32",
                "MQTT",
                "Node.js",
                "React Dashboard"
            ],
            "difficulty": "Advanced",
            "time": "8-12 hours"
        },
        {
            "name": "Home Environment Monitor",
            "desc": "Temperature, humidity, and air quality monitoring with historical charts, threshold alerts, and smart device integration via MQTT.",
            "tech": [
                "ESP32",
                "DHT22/BME280",
                "InfluxDB",
                "Grafana"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        },
        {
            "name": "Plant Watering Automation",
            "desc": "Soil moisture monitoring with automated watering schedule, camera feed for plant health, and mobile notifications when plants need attention.",
            "tech": [
                "Raspberry Pi",
                "Soil Sensor",
                "Python",
                "Telegram Bot"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        },
        {
            "name": "Smart Door Lock System",
            "desc": "NFC/PIN-based door lock with access logs, remote unlock via app, visitor management, and emergency override. Secure BLE communication.",
            "tech": [
                "ESP32",
                "NFC Module",
                "React Native",
                "Firebase"
            ],
            "difficulty": "Advanced",
            "time": "10-14 hours"
        }
    ],
    "Security & Auth": [
        {
            "name": "OAuth2 Authentication Service",
            "desc": "Full OAuth2/OIDC provider with Google/GitHub social login, JWT tokens, refresh rotation, RBAC, and 2FA (TOTP). Production-grade security.",
            "tech": [
                "Node.js",
                "Passport.js",
                "JWT",
                "PostgreSQL",
                "Redis"
            ],
            "difficulty": "Advanced",
            "time": "6-8 hours"
        },
        {
            "name": "Password Manager (Vault)",
            "desc": "Encrypted password vault with AES-256, master password derivation (Argon2), browser extension, auto-fill, and secure sharing.",
            "tech": [
                "Electron",
                "React",
                "Node.js",
                "Crypto APIs"
            ],
            "difficulty": "Expert",
            "time": "12-16 hours"
        },
        {
            "name": "Vulnerability Scanner",
            "desc": "Automated security scanner for web apps - checks for XSS, SQLi, CSRF, misconfigurations, and generates detailed remediation reports.",
            "tech": [
                "Python",
                "Scrapy",
                "Beautiful Soup",
                "FastAPI"
            ],
            "difficulty": "Expert",
            "time": "10-14 hours"
        },
        {
            "name": "Rate Limiter & API Gateway",
            "desc": "Configurable API gateway with rate limiting, IP whitelisting, request logging, abuse detection, and real-time traffic analytics.",
            "tech": [
                "Node.js",
                "Redis",
                "Express",
                "React Dashboard"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        }
    ],
    "Creative & Media": [
        {
            "name": "Collaborative Whiteboard",
            "desc": "Real-time drawing canvas with layers, shapes, text, image upload, undo/redo, and multi-user collaboration via WebRTC.",
            "tech": [
                "React",
                "Canvas API",
                "WebRTC",
                "Socket.io"
            ],
            "difficulty": "Advanced",
            "time": "8-10 hours"
        },
        {
            "name": "Meme Generator Studio",
            "desc": "Drag-and-drop meme editor with template library, custom text styling, image filters, GIF export, and trending meme feed.",
            "tech": [
                "React",
                "Canvas API",
                "Cloudinary",
                "Node.js"
            ],
            "difficulty": "Beginner",
            "time": "3-4 hours"
        },
        {
            "name": "Podcast Hosting Platform",
            "desc": "Upload, host, and distribute podcasts with RSS feed generation, episode analytics, embedded player widget, and AI-generated transcripts.",
            "tech": [
                "Next.js",
                "AWS S3",
                "Whisper API",
                "PostgreSQL"
            ],
            "difficulty": "Advanced",
            "time": "10-14 hours"
        },
        {
            "name": "Color Palette Generator",
            "desc": "AI-driven color palette generator from images or moods. Includes contrast checker, CSS/Tailwind export, palette saving, and accessibility scoring.",
            "tech": [
                "React",
                "Canvas API",
                "Color Theory Algorithms"
            ],
            "difficulty": "Beginner",
            "time": "2-3 hours"
        },
        {
            "name": "Video Thumbnail Maker",
            "desc": "Template-based thumbnail designer with text overlays, background remover, batch export, and integration with YouTube to auto-suggest styles.",
            "tech": [
                "React",
                "Canvas API",
                "Remove.bg API",
                "Node.js"
            ],
            "difficulty": "Intermediate",
            "time": "4-6 hours"
        }
    ]
};

  const CATEGORY_MAPS = {
    "Web Development":          { cls: "color-web",   icon: "🌐", short: "WEB" },
    "AI & Machine Learning":    { cls: "color-ai",    icon: "🤖", short: "AI" },
    "Data & Analytics":         { cls: "color-data",  icon: "📊", short: "DATA" },
    "Developer Tools & CLI":    { cls: "color-dev",   icon: "🔧", short: "DEV" },
    "Games & Interactive":      { cls: "color-game",  icon: "🎮", short: "GAME" },
    "Cloud & DevOps":           { cls: "color-cloud", icon: "☁️",  short: "CLOUD" },
    "Mobile & PWA":             { cls: "color-app",   icon: "📱", short: "APP" },
    "IoT & Hardware":           { cls: "color-iot",   icon: "🏠", short: "IOT" },
    "Security & Auth":          { cls: "color-sec",   icon: "🔒", short: "SEC" },
    "Creative & Media":         { cls: "color-art",   icon: "🎨", short: "ART" }
  };

  // ── 2. STATE MANAGEMENT ─────────────────────────────────────────────────
  let currentCategory = "all";
  let currentDifficulty = "all";
  let searchQuery = "";

  // ── 3. DOM ELEMENT CACHE ────────────────────────────────────────────────
  const tabTrack       = document.getElementById("categoryTabsTrack");
  const renderGrid     = document.getElementById("projectsRenderGrid");
  const emptyBlock     = document.getElementById("emptyStateBlock");
  const searchInput    = document.getElementById("roadmapSearch");
  const clearSearch    = document.getElementById("clearSearchBtn");
  const diffGroup      = document.getElementById("difficultyBtnGroup");
  const resetFiltersCta = document.getElementById("resetFiltersCta");
  const toastStack     = document.getElementById("toastStack");

  // Stats Counters
  const countProjects  = document.getElementById("statProjectsCount");
  const countCategories = document.getElementById("statCategoriesCount");

  // ── 4. INITIALIZE APP ───────────────────────────────────────────────────
  function init() {
    buildCategoryTabs();
    bindEvents();
    renderBlueprintCards();
    updateDashboardStats();
  }

  // Build the list of domain tabs dynamically
  function buildCategoryTabs() {
    tabTrack.innerHTML = "";
    
    // Add "ALL DOMAINS" tab
    const allTab = document.createElement("button");
    allTab.className = "cat-tab-btn active";
    allTab.setAttribute("data-cat", "all");
    allTab.innerHTML = `<span class="cat-icon">⚙️</span>ALL DOMAINS`;
    tabTrack.appendChild(allTab);

    // Add specific categories
    Object.keys(PROJECTS_DB).forEach(cat => {
      const config = CATEGORY_MAPS[cat] || { cls: "", icon: "📁" };
      const btn = document.createElement("button");
      btn.className = "cat-tab-btn";
      btn.setAttribute("data-cat", cat);
      btn.innerHTML = `<span class="cat-icon">${config.icon}</span>${cat.toUpperCase()}`;
      tabTrack.appendChild(btn);
    });
  }

  // ── 5. FILTER LOGIC & RENDERING ─────────────────────────────────────────
  function getFilteredProjects() {
    let result = [];

    Object.keys(PROJECTS_DB).forEach(cat => {
      // Category filter check
      if (currentCategory !== "all" && currentCategory !== cat) return;

      PROJECTS_DB[cat].forEach((proj, idx) => {
        // Difficulty filter check
        if (currentDifficulty !== "all" && proj.difficulty !== currentDifficulty) return;

        // Search query check
        if (searchQuery) {
          const s = searchQuery.toLowerCase();
          const matchesName = proj.name.toLowerCase().includes(s);
          const matchesDesc = proj.desc.toLowerCase().includes(s);
          const matchesTech = proj.tech.some(t => t.toLowerCase().includes(s));
          if (!matchesName && !matchesDesc && !matchesTech) return;
        }

        // Attach category and dynamic original index for numbering
        result.push({
          ...proj,
          category: cat,
          displayNum: idx + 1
        });
      });
    });

    return result;
  }

  function renderBlueprintCards() {
    const list = getFilteredProjects();

    // Toggle Empty State Block
    if (list.length === 0) {
      renderGrid.style.display = "none";
      emptyBlock.style.display = "flex";
      return;
    }

    renderGrid.style.display = "grid";
    emptyBlock.style.display = "none";

    renderGrid.innerHTML = "";
    list.forEach((proj, i) => {
      const catConfig = CATEGORY_MAPS[proj.category] || { cls: "color-web", icon: "🌐", short: "DEV" };
      const diffLabel = proj.difficulty.toUpperCase();
      
      // Select appropriate difficulty badge coloring
      let diffColor = "var(--neon-green)";
      if (proj.difficulty === "Intermediate") diffColor = "var(--neon-orange)";
      if (proj.difficulty === "Advanced") diffColor = "var(--neon-red)";
      if (proj.difficulty === "Expert") diffColor = "var(--neon-purple)";

      const techPills = proj.tech.map(t => `<span class="tech-stack-pill">${t}</span>`).join("");

      const card = document.createElement("div");
      card.className = `proj-blueprint-card ${catConfig.cls}`;
      card.style.animationDelay = `${i * 0.04}s`;
      
      // Inject details
      card.innerHTML = `
        <div class="proj-card-glow-bar" style="background-color: var(--accent)"></div>
        <div>
          <div class="proj-top-meta">
            <span class="proj-blueprint-num" style="color: var(--accent)">${catConfig.short}-0${proj.displayNum}</span>
            <span class="proj-difficulty-tag" style="background-color: rgba(255,255,255,0.03); color: ${diffColor}; border: 1px solid ${diffColor}20">${diffLabel}</span>
          </div>
          <div class="proj-main-body">
            <h3 class="proj-card-title">${proj.name}</h3>
            <p class="proj-card-desc">${proj.desc}</p>
          </div>
        </div>
        <div>
          <div class="proj-stack-pills-row">
            ${techPills}
          </div>
          <div class="proj-bottom-row">
            <span class="proj-time-est">${proj.time.toUpperCase()}</span>
            <button class="btn-copy-prompt" data-name="${proj.name}" data-desc="${proj.desc}" data-tech="${proj.tech.join(', ')}" data-diff="${proj.difficulty}">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
              </svg>
              Copy Prompt
            </button>
          </div>
        </div>
      `;

      // ── 3D Interactive Tilt Engine ──
      card.addEventListener("mousemove", e => {
        const rect = card.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width;
        const py = (e.clientY - rect.top) / rect.height;
        
        // Tilt calculations
        const rx = (py - 0.5) * -12;
        const ry = (px - 0.5) * 12;
        
        card.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg) scale(1.02)`;
        card.style.setProperty("--mx", (px * 100) + "%");
        card.style.setProperty("--my", (py * 100) + "%");
        card.classList.add("hovered");
      });

      card.addEventListener("mouseleave", () => {
        card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)";
        card.classList.remove("hovered");
      });

      renderGrid.appendChild(card);
    });

    // Re-bind Copy Event Handlers
    bindPromptCopyHandlers();
  }

  // ── 6. PROMPT CONSTRUCTORS & COPY HANDLERS ──────────────────────────────
  function bindPromptCopyHandlers() {
    const copyBtns = renderGrid.querySelectorAll(".btn-copy-prompt");
    copyBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const name = btn.getAttribute("data-name");
        const desc = btn.getAttribute("data-desc");
        const tech = btn.getAttribute("data-tech");
        const diff = btn.getAttribute("data-diff");

        // Format direct system instructions
        const promptTemplate = `Act as an expert solo developer. We are going to build the project: "${name}".

Category Profile:
- Difficulty Tier: ${diff}
- Predefined Stack: [${tech}]
- Design Mandate: Rich Aesthetics, Futuristic Dark Theme, Glassmorphism, Micro-Animations.

Functional Requirements:
${desc}

Let's do this step-by-step:
1. Propose the system design and architecture specs.
2. Initialize tests to cover data modeling and core flows.
3. Write clean, complete modular code using robust validation protocols.

Give me the complete architecture walkthrough to begin!`;

        // Write directly to clipboard
        navigator.clipboard.writeText(promptTemplate).then(() => {
          triggerToast("Blueprint Authenticated", `Prompt for "${name}" copied to clipboard!`);
          
          // Micro interaction state change
          btn.classList.add("copied");
          btn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!`;
          
          setTimeout(() => {
            btn.classList.remove("copied");
            btn.innerHTML = `
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
              </svg>
              Copy Prompt
            `;
          }, 2000);
        }).catch(err => {
          console.error("Failed to copy blueprint prompt:", err);
        });
      });
    });
  }

  // Interactive Custom Toasts
  function triggerToast(title, bodyText) {
    const toast = document.createElement("div");
    toast.className = "cyber-toast";
    toast.innerHTML = `
      <div class="toast-indicator"></div>
      <div class="toast-body">
        <span class="toast-title">${title.toUpperCase()}</span>
        <span class="toast-text">${bodyText}</span>
      </div>
    `;

    toastStack.appendChild(toast);
    
    // Auto purge toast
    setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateY(-10px) scale(0.95)";
      toast.style.transition = "all 0.3s";
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  }

  // ── 7. INTERACTIVE EVENT BINDINGS ──────────────────────────────────────
  function bindEvents() {
    // 1. Search Box input with debounce
    let searchDebounce;
    searchInput.addEventListener("input", e => {
      searchQuery = e.target.value;
      clearSearch.style.display = searchQuery ? "block" : "none";
      
      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(() => {
        renderBlueprintCards();
      }, 150);
    });

    // Clear search trigger
    clearSearch.addEventListener("click", () => {
      searchInput.value = "";
      searchQuery = "";
      clearSearch.style.display = "none";
      renderBlueprintCards();
      searchInput.focus();
    });

    // 2. Difficulty Buttons Group
    const diffBtns = diffGroup.querySelectorAll(".diff-filter-btn");
    diffBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        diffBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentDifficulty = btn.getAttribute("data-diff");
        renderBlueprintCards();
      });
    });

    // 3. Category Tabs Track Click
    tabTrack.addEventListener("click", e => {
      const btn = e.target.closest(".cat-tab-btn");
      if (!btn) return;

      const tabs = tabTrack.querySelectorAll(".cat-tab-btn");
      tabs.forEach(t => t.classList.remove("active"));
      btn.classList.add("active");
      
      currentCategory = btn.getAttribute("data-cat");
      renderBlueprintCards();
      
      // Staggered smooth horizontal scroll to clicked element
      btn.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    });

    // 4. Reset Filters Cta
    resetFiltersCta.addEventListener("click", () => {
      searchInput.value = "";
      searchQuery = "";
      clearSearch.style.display = "none";

      diffBtns.forEach(b => b.classList.remove("active"));
      diffBtns[0].classList.add("active");
      currentDifficulty = "all";

      const tabs = tabTrack.querySelectorAll(".cat-tab-btn");
      tabs.forEach(t => t.classList.remove("active"));
      tabs[0].classList.add("active");
      currentCategory = "all";

      renderBlueprintCards();
    });
  }

  function updateDashboardStats() {
    let totalCount = 0;
    Object.keys(PROJECTS_DB).forEach(cat => {
      totalCount += PROJECTS_DB[cat].length;
    });

    countProjects.textContent = totalCount;
    countCategories.textContent = Object.keys(PROJECTS_DB).length;
  }

  // Run initial sequence
  init();

})();
