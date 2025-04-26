import { Header } from "@/components/header"
import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "About Us | الوصول إلى وربط الحلول المحلية",
  description: "Learn about our mission to connect local experts with customers in Morocco",
}

export default function AboutPage() {
  return (
    <main className="min-h-screen">
      <Header />
      <section className="pt-32 pb-16 bg-background">
        <div className="container-custom">
          <h1 className="text-4xl font-bold mb-8 text-primary">معلومات عنا</h1>
          <p className="text-lg mb-8">صفحة من نحن قيد الإنشاء. سيتم إضافة المحتوى قريبًا.</p>
          <p className="text-lg mb-8">Our about page is under construction. Content will be added soon.</p>
        </div>
      </section>
    </main>
  )
}
