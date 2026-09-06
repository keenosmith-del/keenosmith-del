import base64
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "generated"

OUT.mkdir(parents=True, exist_ok=True)

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"


def data_uri(path: Path, mime: str):
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def write_svg(filename: str, content: str):
    path = OUT / filename
    path.write_text(content, encoding="utf-8")
    print(f"Generated {path.relative_to(ROOT)}")


def svg_icon(filename: str):
    return data_uri(ASSETS / "tech" / filename, "image/svg+xml")


def png_image(filename: str):
    return data_uri(ASSETS / "projects" / filename, "image/png")


# =========================================================
# INTRO
# =========================================================

intro = """
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="1200"
    height="390"
    viewBox="0 0 1200 390">

    <rect
        width="1200"
        height="390"
        rx="34"
        fill="#080808"
    />

    <text
        x="600"
        y="125"
        text-anchor="middle"
        fill="#F5F5F7"
        font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
        font-size="72"
        font-weight="300"
        letter-spacing="-4">
        Keeno Smith
    </text>

    <text
        x="600"
        y="178"
        text-anchor="middle"
        fill="#86868B"
        font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
        font-size="18"
        font-weight="400">
        Full-Stack Software Engineer · Web Developer · AI Application Development
    </text>

    <!-- Email -->

    <a href="mailto:business.keenosmith@icloud.com">
        <rect
            x="360"
            y="245"
            width="130"
            height="40"
            rx="20"
            fill="#101010"
        />

        <text
            x="425"
            y="270"
            text-anchor="middle"
            fill="#D2D2D7"
            font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
            font-size="13"
            font-weight="500">
            Email
        </text>
    </a>

    <!-- LinkedIn -->

    <a href="https://www.linkedin.com/in/keenotreysmith/">
        <rect
            x="505"
            y="245"
            width="140"
            height="40"
            rx="20"
            fill="#101010"
        />

        <text
            x="575"
            y="270"
            text-anchor="middle"
            fill="#D2D2D7"
            font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
            font-size="13"
            font-weight="500">
            LinkedIn
        </text>
    </a>

    <!-- Portfolio -->

    <a href="https://keenosmith.vercel.app">
        <rect
            x="660"
            y="245"
            width="140"
            height="40"
            rx="20"
            fill="#101010"
        />

        <text
            x="730"
            y="270"
            text-anchor="middle"
            fill="#D2D2D7"
            font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"
            font-size="13"
            font-weight="500">
            Portfolio
        </text>
    </a>

</svg>
"""

write_svg("intro.svg", intro)


# =========================================================
# ABOUT
# =========================================================

about_lines = [
    "I’m a full-stack software engineer and web developer with a focus on building web applications, AI-powered software, and full-stack systems. I",
    "work across the stack, from designing interfaces and developing frontend experiences to building APIs, databases, authentication, and deployment",
    "workflows. I’m particularly interested in the intersection of software engineering and AI, and in using modern tools and technologies to turn ideas into working products.",
]

about_text = "\n".join(
    f"""
    <text
        x="45"
        y="{72 + i * 27}"
        fill="#8E8E93"
        font-family="{FONT}"
        font-size="14"
        font-weight="400">
        {html.escape(line)}
    </text>
    """
    for i, line in enumerate(about_lines)
)

about = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="1200"
    height="180"
    viewBox="0 0 1200 180">

    <rect
        width="1200"
        height="180"
        rx="34"
        fill="#080808"
    />

    {about_text}

</svg>
"""

write_svg("about.svg", about)


# =========================================================
# TECHNOLOGIES
# =========================================================

technologies = [
    ("React", "react.svg"),
    ("JavaScript", "javascript.svg"),
    ("Node.js", "nodedotjs.svg"),
    ("Express", "express.svg"),
    ("MongoDB", "mongodb.svg"),

    ("Mongoose", "mongoose.svg"),
    ("PostgreSQL", "postgresql.svg"),
    ("Python", "python.svg"),
    ("PyTorch", "pytorch.svg"),
    ("Hugging Face", "huggingface.svg"),

    ("Claude", "claude.svg"),
    ("GitHub Copilot", "githubcopilot.svg"),
    ("GitHub", "github.svg"),
    ("Docker", "docker.svg"),
    ("Kubernetes", "kubernetes.svg"),

    ("Postman", "postman.svg"),
    ("JWT", "jsonwebtokens.svg"),
    ("Cloudflare", "cloudflare.svg"),
    ("Render", "render.svg"),
    ("Vercel", "vercel.svg"),
]

tech_items = []

cols = 5
card_w = 208
card_h = 68
gap_x = 12
gap_y = 12

start_x = 44
start_y = 46

for index, (name, icon_file) in enumerate(technologies):

    row = index // cols
    col = index % cols

    x = start_x + col * (card_w + gap_x)
    y = start_y + row * (card_h + gap_y)

    icon = svg_icon(icon_file)

    tech_items.append(
        f"""
        <g>

            <rect
                x="{x}"
                y="{y}"
                width="{card_w}"
                height="{card_h}"
                rx="18"
                fill="#0D0D0D"
            />

            <!-- white icon backing -->
            <image
                href="{icon}"
                x="{x + 20}"
                y="{y + 22}"
                width="24"
                height="24"
                style="filter: brightness(0) invert(1);"
            />

            <text
                x="{x + 58}"
                y="{y + 39}"
                fill="#D2D2D7"
                font-family="{FONT}"
                font-size="13"
                font-weight="500">
                {html.escape(name)}
            </text>

        </g>
        """
    )

tech = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="1200"
    height="390"
    viewBox="0 0 1200 390">

    <rect
        width="1200"
        height="390"
        rx="34"
        fill="#080808"
    />

    {''.join(tech_items)}

</svg>
"""

write_svg("technologies.svg", tech)


# =========================================================
# PROJECTS
# =========================================================

projects = [
    {
        "title": "Flagship Full-Stack MERN Platform",
        "description": [
            "A full-stack productivity platform for managing tasks,",
            "projects, goals, reminders, notes, and personal workflows.",
        ],
        "stack": "React · Node.js · Express · MongoDB · Mongoose · JWT",
        "image": "productivityProjectImage.png",
        "repo": "https://github.com/keenosmith-del/personal-productivity-desktop",
    },

    {
        "title": "AI Model",
        "description": [
            "An AI application exploring LLM integration, prompt",
            "engineering, RAG, and local model workflows.",
        ],
        "stack": "React · OpenAI · RAG · Hugging Face · LLMs",
        "image": "aiProjectImage.png",
        "repo": "https://github.com/keenosmith-del/ai-entity",
    },

    {
        "title": "Music API Web App",
        "description": [
            "A full-stack music application for discovery, playback,",
            "queue management, and interacting with music data through an API.",
        ],
        "stack": "FastAPI · MongoDB · Postman · API Development · REST API",
        "image": "musicProjectImage.png",
        "repo": "https://github.com/keenosmith-del/music-api",
    },

    {
        "title": "SQL Enterprise Workspace",
        "description": [
            "A SQL-focused enterprise workspace built around relational",
            "data, structured architecture, and full-stack development.",
        ],
        "stack": "React · Vite · Express · PostgreSQL · Prisma",
        "image": "enterpriseProjectImage.png",
        "repo": "https://github.com/keenosmith-del/enterprise-workspace",
    },
]


# =========================================================
# PROJECTS CONTAINER
# =========================================================

PROJECT_W = 554
PROJECT_H = 440

container_width = 1200
container_height = 1120

card_positions = [
    (44, 150),
    (602, 150),
    (44, 605),
    (602, 605),
]

project_items = []

for project, (x, y) in zip(projects, card_positions):

    image = png_image(project["image"])

    description_svg = "".join(
        f"""
        <text
            x="{x + 16}"
            y="{y + 292 + (i * 23)}"
            fill="#8E8E93"
            font-family="{FONT}"
            font-size="13"
            font-weight="400">
            {html.escape(line)}
        </text>
        """
        for i, line in enumerate(project["description"])
    )

    project_items.append(
        f"""
        <a href="{project["repo"]}">

            <rect
                x="{x}"
                y="{y}"
                width="{PROJECT_W}"
                height="{PROJECT_H}"
                rx="28"
                fill="#0D0D0D"
            />

            <defs>
                <clipPath id="projectClip{x}{y}">
                    <rect
                        x="{x + 16}"
                        y="{y + 16}"
                        width="{PROJECT_W - 32}"
                        height="235"
                        rx="20"
                    />
                </clipPath>
            </defs>

            <image
                href="{image}"
                x="{x + 16}"
                y="{y + 16}"
                width="{PROJECT_W - 32}"
                height="235"
                preserveAspectRatio="xMidYMid slice"
                clip-path="url(#projectClip{x}{y})"
            />

            <text
                x="{x + 16}"
                y="{y + 275}"
                fill="#F5F5F7"
                font-family="{FONT}"
                font-size="18"
                font-weight="500"
                letter-spacing="-0.5">
                {html.escape(project["title"])}
            </text>

            {description_svg}

            <text
                x="{x + 16}"
                y="{y + 375}"
                fill="#5F5F63"
                font-family="{FONT}"
                font-size="11"
                font-weight="500">
                {html.escape(project["stack"])}
            </text>

            <circle
                cx="{x + PROJECT_W - 34}"
                cy="{y + 375}"
                r="18"
                fill="#101010"
            />

            <path
                d="M{x + PROJECT_W - 40} {y + 375}
                   H{x + PROJECT_W - 29}
                   M{x + PROJECT_W - 35} {y + 371}
                   L{x + PROJECT_W - 29} {y + 375}
                   L{x + PROJECT_W - 35} {y + 379}"
                fill="none"
                stroke="#A1A1A6"
                stroke-width="1.5"
                stroke-linecap="round"
                stroke-linejoin="round"
            />

        </a>
        """
    )


projects_svg = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{container_width}"
    height="{container_height}"
    viewBox="0 0 {container_width} {container_height}">

    <rect
        width="{container_width}"
        height="{container_height}"
        rx="34"
        fill="#080808"
    />

    <!-- Projects heading -->

    <text
        x="44"
        y="55"
        fill="#F5F5F7"
        font-family="{FONT}"
        font-size="24"
        font-weight="500"
        letter-spacing="-0.7">
        Projects
    </text>

    <text
        x="44"
        y="82"
        fill="#6E6E73"
        font-family="{FONT}"
        font-size="13"
        font-weight="400">
        Selected full-stack, AI, API, and database projects.
    </text>

    <!-- Project grid -->

    {''.join(project_items)}

    <!-- View portfolio -->

    <a href="https://keenosmith.vercel.app">

        <rect
            x="515"
            y="1000"
            width="170"
            height="44"
            rx="22"
            fill="#101010"
        />

        <text
            x="600"
            y="1087"
            text-anchor="middle"
            fill="#D2D2D7"
            font-family="{FONT}"
            font-size="13"
            font-weight="500"
            letter-spacing="-0.1">
            View portfolio
        </text>

    </a>

</svg>
"""

write_svg("projects.svg", projects_svg)
