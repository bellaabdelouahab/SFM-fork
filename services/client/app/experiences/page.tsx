import { Header } from "@/components/header"
import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "Experiences | الوصول إلى وربط الحلول المحلية",
  description: "Discover unique local experiences in Morocco",
}

export default function ExperiencesPage() {
  return (
    <main className="min-h-screen">
      <Header />
      <section className="pt-32 pb-16 bg-background">
        <div className="container-custom">
          <h1 className="text-4xl font-bold mb-8 text-primary">البكيفيات</h1>
          <p className="text-lg mb-8">صفحة التجارب قيد الإنشاء. سيتم إضافة المحتوى قريبًا.</p>
          <p className="text-lg mb-8">Our experiences page is under construction. Content will be added soon.</p>
        </div>
      </section>
    </main>
  )
}
