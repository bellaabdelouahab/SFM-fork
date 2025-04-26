import { Header } from "@/components/header"
import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "For Businesses | الوصول إلى وربط الحلول المحلية",
  description: "Join our platform and connect with customers looking for your services",
}

export default function BusinessesPage() {
  return (
    <main className="min-h-screen">
      <Header />
      <section className="pt-32 pb-16 bg-background">
        <div className="container-custom">
          <h1 className="text-4xl font-bold mb-8 text-primary">للشركات</h1>
          <p className="text-lg mb-8">صفحة الشركات قيد الإنشاء. سيتم إضافة المحتوى قريبًا.</p>
          <p className="text-lg mb-8">Our business page is under construction. Content will be added soon.</p>
        </div>
      </section>
    </main>
  )
}
