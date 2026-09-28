import { Navigation } from "./components/Navigation";
import { Hero } from "./components/Hero";
import { Intro } from "./components/Intro";
import { Results } from "./components/Results";
import { Work } from "./components/Work";
import { About } from "./components/About";
import { Expertise } from "./components/Expertise";
import { FAQ } from "./components/FAQ";
import { Services } from "./components/Services";
import { Footer } from "./components/Footer";

export default function App() {
  return (
    <>
      <Navigation />
      <main>
        <Hero />
        <Intro />
        <Results />
        <Work />
        <About />
        <Expertise />
        <FAQ />
        <Services />
      </main>
      <Footer />
    </>
  );
}
