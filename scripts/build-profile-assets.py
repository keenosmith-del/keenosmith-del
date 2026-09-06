import base64
import html
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "generated"

OUT.mkdir(parents=True, exist_ok=True)

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif"

# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Intro
# ---------------------------------------------------------

intro = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="1200"
    height="330"
    viewBox="0 0 1200 330">

    <rect
        width="1200"
        height="330"
        rx="34"
        fill="#080808"
    />

    <text
        x="600"
        y="135"
        text-anchor="middle"
        fill="#F5F5F7"
        font-family="{FONT}"
        font-size="72"
        font-weight="300"
        letter-spacing="-4">
        Keeno Smith
    </text>

    <text
        x="600"
        y="190"
        text-anchor="middle"
        fill="#86868B"
        font-family="{FONT}"
        font-size="18"
        font-weight="400">
        Full-Stack Software Engineer · Web Developer · AI Application Development
    </text>

</svg>
"""

write_svg("intro.svg", intro)


# ---------------------------------------------------------
# About
# ---------------------------------------------------------

about_lines = [
    "I’m a full-stack software engineer and web developer with a focus on building web applications,",
    "AI-powered software, and full-stack systems. I work across the stack, from designing interfaces",
    "and developing frontend experiences to building APIs, databases, authentication, and deployment",
    "workflows. I’m particularly interested in the intersection of software engineering and AI,",
    "and in using modern tools and technologies to turn ideas into working products.",
]

about_text = "\n".join(
    f"""
    <text
        x="55"
        y="{66 + i * 25}"
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
    height="190"
    viewBox="0 0 1200 190">

    <rect
        width="1200"
        height="190"
        rx="34"
        fill="#080808"
    />

    {about_text}

</svg>
"""

write_svg("about.svg", about)


# ---------------------------------------------------------
# Technologies
# ---------------------------------------------------------

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

            <image
                href="{icon}"
                x="{x + 20}"
                y="{y + 22}"
                width="24"
                height="24"
            />

            <text
                x="{x + 58}"
                y="{y + 41}"
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


# ---------------------------------------------------------
# Project cards
# ---------------------------------------------------------

projects = [
    {
        "filename": "project1.svg",
        "title": "Flagship Full-Stack MERN Platform",
        "description": [
            "A full-stack productivity platform for managing tasks,",
            "projects, goals, reminders, notes, and personal workflows.",
        ],
        "stack": "React · Node.js · Express · MongoDB · Mongoose · JWT",
        "image": "productivityProjectImage.png",
    },
    {
        "filename": "project2.svg",
        "title": "AI Model",
        "description": [
            "An AI application exploring LLM integration, prompt",
            "engineering, RAG, and local model workflows.",
        ],
        "stack": "React · OpenAI · RAG · Hugging Face · LLMs",
        "image": "aiProjectImage.png",
    },
    {
        "filename": "project3.svg",
        "title": "Music API Web App",
        "description": [
            "A full-stack music application for discovery, playback,",
            "queue management, and interacting with music data through an API.",
        ],
        "stack": "FastAPI · MongoDB · Postman · API Development · REST API",
        "image": "musicProjectImage.png",
    },
    {
        "filename": "project4.svg",
        "title": "SQL Enterprise Workspace",
        "description": [
            "A SQL-focused enterprise workspace built around relational",
            "data, structured architecture, and full-stack development.",
        ],
        "stack": "React · Vite · Express · PostgreSQL · Prisma",
        "image": "enterpriseProjectImage.png",
    },
]

for project in projects:
    image = png_image(project["image"])

    desc_svg = "".join(
        f"""
        <text
            x="34"
            y="{340 + i * 23}"
            fill="#8E8E93"
            font-family="{FONT}"
            font-size="13"
            font-weight="400">
            {html.escape(line)}
        </text>
        """
        for i, line in enumerate(project["description"])
    )

    card = f"""
    <svg
        xmlns="http://www.w3.org/2000/svg"
        width="590"
        height="475"
        viewBox="0 0 590 475">

        <defs>
            <clipPath id="cardClip">
                <rect
                    width="590"
                    height="475"
                    rx="28"
                />
            </clipPath>

            <clipPath id="imageClip">
                <rect
                    x="18"
                    y="18"
                    width="554"
                    height="255"
                    rx="20"
                />
            </clipPath>
        </defs>

        <rect
            width="590"
            height="475"
            rx="28"
            fill="#080808"
        />

        <rect
            x="18"
            y="18"
            width="554"
            height="255"
            rx="20"
            fill="#050505"
        />

        <image
            href="{image}"
            x="18"
            y="18"
            width="554"
            height="255"
            preserveAspectRatio="xMidYMid slice"
            clip-path="url(#imageClip)"
        />

        <text
            x="34"
            y="313"
            fill="#F5F5F7"
            font-family="{FONT}"
            font-size="19"
            font-weight="500"
            letter-spacing="-0.5">
            {html.escape(project["title"])}
        </text>

        {desc_svg}

        <text
            x="34"
            y="420"
            fill="#5F5F63"
            font-family="{FONT}"
            font-size="11"
            font-weight="500">
            {html.escape(project["stack"])}
        </text>

        <circle
            cx="536"
            cy="420"
            r="18"
            fill="#101010"
        />

        <path
            d="M530 420H541 M537 416L541 420L537 424"
            fill="none"
            stroke="#A1A1A6"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
        />

    </svg>
    """

    write_svg(project["filename"], card)


# ---------------------------------------------------------
# Link pills
# ---------------------------------------------------------

pills = [
    ("email-pill.svg", "Email", 120),
    ("linkedin-pill.svg", "LinkedIn", 140),
    ("portfolio-pill.svg", "Portfolio", 140),
]

for filename, label, width in pills:
    pill = f"""
    <svg
        xmlns="http://www.w3.org/2000/svg"
        width="{width}"
        height="38"
        viewBox="0 0 {width} 38">

        <rect
            width="{width}"
            height="38"
            rx="19"
            fill="#0D0D0D"
        />

        <text
            x="{width / 2}"
            y="24"
            text-anchor="middle"
            fill="#D2D2D7"
            font-family="{FONT}"
            font-size="13"
            font-weight="500">
            {label}
        </text>

    </svg>
    """

    write_svg(filename, pill)