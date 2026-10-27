import "./globals.css";
import Hero from "@/components/Hero";
import ProofStrip from "@/components/ProofStrip";
import HowItWorks from "@/components/HowItWorks";
import FeatureBlock from "@/components/FeatureBlock";
import Pricing from "@/components/Pricing";
import FinalCTA from "@/components/FinalCTA";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <>
      <Hero />
      <ProofStrip />
      <HowItWorks />
      <section className="py-24 px-4 md:px-12 space-y-16">
        <FeatureBlock
          title="AI‑Powered Prototyping"
          description="Turn design sketches into functional components with a click. No hand‑coding required."
          imgSrc="/images/feature1.jpg"
          reverse={false}
        />
        <FeatureBlock
          title="Realtime 3‑D Configurator"
          description="Clients can customise colours, materials and layout directly in‑browser."
          imgSrc="/images/feature2.jpg"
          reverse={true}
        />
        <FeatureBlock
          title="Scalable Cloud Deployments"
          description="Deploy to Vercel, Netlify or any Docker host with a single command."
          imgSrc="/images/feature3.jpg"
          reverse={false}
        />
      </section>
      <Pricing />
      <FinalCTA />
      <Footer />
    </>
  );
}
