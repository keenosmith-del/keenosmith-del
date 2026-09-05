import "./App.css";

import About from "./components/About";
import TechStack from "./components/TechStack";
import Projects from "./components/Projects";

function App() {
  return (
    <main className="profile">

      <section className="hero">
        <img
          src="/assets/hero/memoji.gif"
          alt="Animated Keeno Smith Memoji"
        />
      </section>

      <section className="intro">
        <div className="intro-content">
          <h1>Keeno Smith</h1>

          <p className="intro-title">
            Full-Stack Software Engineer
            <span>·</span>
            Web Developer
            <span>·</span>
            AI Application Development
          </p>

          <nav className="intro-links" aria-label="Contact links">
            <a href="mailto:business.keenosmith@icloud.com">
              Email
            </a>

            <a
              href="https://www.linkedin.com/in/keenotreysmith/"
              target="_blank"
              rel="noreferrer"
            >
              LinkedIn
            </a>

            <a
              href="https://keenosmith.vercel.app"
              target="_blank"
              rel="noreferrer"
            >
              Portfolio
            </a>
          </nav>
        </div>
      </section>

      <About />
      <TechStack />
      <Projects />

    </main>
  );
}

export default App;