import react from "../assets/tech/react.svg";
import javascript from "../assets/tech/javascript.svg";
import nodejs from "../assets/tech/nodedotjs.svg";
import python from "../assets/tech/python.svg";
import express from "../assets/tech/express.svg";
import mongodb from "../assets/tech/mongodb.svg";
import mongoose from "../assets/tech/mongoose.svg";
import postgresql from "../assets/tech/postgresql.svg";
import pytorch from "../assets/tech/pytorch.svg";
import huggingface from "../assets/tech/huggingface.svg";
import claude from "../assets/tech/claude.svg";
import githubcopilot from "../assets/tech/githubcopilot.svg";
import github from "../assets/tech/github.svg";
import docker from "../assets/tech/docker.svg";
import kubernetes from "../assets/tech/kubernetes.svg";
import postman from "../assets/tech/postman.svg";
import jwt from "../assets/tech/jsonwebtokens.svg";
import cloudflare from "../assets/tech/cloudflare.svg";
import render from "../assets/tech/render.svg";
import vercel from "../assets/tech/vercel.svg";

const technologies = [
  { name: "React", icon: react },
  { name: "JavaScript", icon: javascript },
  { name: "Node.js", icon: nodejs },
  { name: "Python", icon: python },
  { name: "Express", icon: express },
  { name: "MongoDB", icon: mongodb },
  { name: "Mongoose", icon: mongoose },
  { name: "PostgreSQL", icon: postgresql },
  { name: "PyTorch", icon: pytorch },
  { name: "Hugging Face", icon: huggingface },
  { name: "Claude", icon: claude },
  { name: "GitHub Copilot", icon: githubcopilot },
  { name: "GitHub", icon: github },
  { name: "Docker", icon: docker },
  { name: "Kubernetes", icon: kubernetes },
  { name: "Postman", icon: postman },
  { name: "JWT", icon: jwt },
  { name: "Cloudflare", icon: cloudflare },
  { name: "Render", icon: render },
  { name: "Vercel", icon: vercel },
];

function TechStack() {
  return (
    <section className="tech-section">

      <div className="tech-grid">
        {technologies.map((technology) => (
          <div className="tech-item" key={technology.name}>
            <div className="tech-icon">
              <img
                src={technology.icon}
                alt=""
                aria-hidden="true"
              />
            </div>

            <span>{technology.name}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

export default TechStack;