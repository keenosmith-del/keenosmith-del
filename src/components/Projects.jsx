import {
  ArrowRight,
} from "lucide-react";

import project1Image from "../assets/projects/productivityProjectImage.png";
import project2Image from "../assets/projects/aiProjectImage.png";
import project3Image from "../assets/projects/musicProjectImage.png";
import project4Image from "../assets/projects/enterpriseProjectImage.png";

const projects = [
  {
    title: "Flagship Full-Stack MERN Platform",
    description:
      "A full-stack productivity platform for managing tasks, projects, goals, reminders, notes, and personal workflows.",
    stack: "React · Node.js · Express · MongoDB · Mongoose · JWT",
    image: project1Image,
    repo: "https://github.com/keenosmith-del/personal-productivity-desktop",
  },
  {
    title: "AI Model",
    description:
      "An AI application exploring LLM integration, prompt engineering, RAG, and local model workflows.",
    stack: "React · OpenAI · RAG · Hugging Face · LLMs",
    image: project2Image,
    repo: "https://github.com/keenosmith-del/ai-entity",
  },
  {
    title: "Music API Web App",
    description:
      "A full-stack music application for discovery, playback, queue management, and interacting with music data through an API.",
    stack: "FastAPI · MongoDB · Postman · API Development · REST API",
    image: project3Image,
    repo: "https://github.com/keenosmith-del/music-api",
  },
  {
    title: "SQL Enterprise Workspace",
    description:
      "A SQL-focused enterprise workspace built around relational data, structured architecture, and modern full-stack development.",
    stack: "React · Vite · Express · PostgreSQL · Prisma",
    image: project4Image,
    repo: "https://github.com/keenosmith-del/enterprise-workspace",
  },
];

function Projects() {
  return (
    <section className="projects-section">
      <div className="projects-header">
        <h2>Projects</h2>
      </div>

      <div className="projects-grid">
        {projects.map((project) => (
          <article className="project-card" key={project.title}>
            <div className="project-image-wrapper">
              <img
                src={project.image}
                alt={`${project.title} preview`}
                className="project-image"
              />
            </div>

            <div className="project-content">
              <div>
                <h3>{project.title}</h3>

                <p className="project-description">
                  {project.description}
                </p>

                <p className="project-stack">
                  {project.stack}
                </p>
              </div>

              <a
                className="project-arrow"
                href={project.repo}
                target="_blank"
                rel="noreferrer"
                aria-label={`Open ${project.title} repository`}
              >
                <ArrowRight size={16} strokeWidth={1.7} />
              </a>
            </div>
          </article>
        ))}
      </div>

      <a
        className="projects-portfolio-link"
        href="https://keenosmith.vercel.app"
        target="_blank"
        rel="noreferrer"
      >
        View portfolio
        <ArrowRight size={14} strokeWidth={1.7} />
      </a>
    </section>
  );
}

export default Projects;

