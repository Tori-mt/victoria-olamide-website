import { Navigation } from "./components/Navigation";
import { Hero } from "./components/Hero";
import { Results } from "./components/Results";
import { Work } from "./components/Work";
import { About } from "./components/About";
import { Solutions } from "./components/Solutions";
import { Expertise } from "./components/Expertise";
import { Insights } from "./components/Insights";
import { Services } from "./components/Services";
import { Contact } from "./components/Contact";
import { Footer } from "./components/Footer";

export default function App() {
  return (
    <>
      <Navigation />
      <main>
        <Hero />
        <Results />
        <Work />
        <About />
        <Solutions />
        <Expertise />
        <Insights />
        <Services />
        <Contact />
      </main>
      <Footer />
    </>
  );
}