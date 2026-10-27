import "./globals.css";
import NavBar from "@/components/NavBar";

export const metadata = {
  title: "Vibsocial – Advanced Digital Studio",
  description: "Showcase of cutting‑edge web and AI solutions for businesses & creators.",
  openGraph: {
    title: "Vibsocial",
    description: "Advanced digital studio for businesses and influencers.",
    images: [{ url: "/images/hero-poster.jpg", width: 1200, height: 630 }],
    type: "website"
  },
  viewport: "width=device-width,initial-scale=1"
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="antialiased bg-surface text-text">
      <body className="flex flex-col min-h-screen">
        <NavBar />
        {children}
      </body>
    </html>
  );
}
