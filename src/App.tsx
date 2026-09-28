import { Navigation } from "./components/Navigation";
import { Hero } from "./components/Hero";
import { About } from "./components/About";
import { Results } from "./components/Results";
import { Work } from "./components/Work";
import { Expertise } from "./components/Expertise";
import { FAQ } from "./components/FAQ";
import { Footer } from "./components/Footer";

export default function App() {
  return (
    <>
      <Navigation />
      <main>
        <Hero />
        <About />
        <Results />
        <Work />
        <Expertise />
        <FAQ />
      </main>
      <Footer />
    </>
  );
}
