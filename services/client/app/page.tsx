import { Hero } from "@/components/hero"
import { Features } from "@/components/features"
import { Header } from "@/components/header"

export default function Home() {
  return (
    <main className="min-h-screen">
      <Header />
      <Hero />
      <Features />
    </main>
  )
}
