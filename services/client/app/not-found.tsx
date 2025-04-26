import Link from "next/link"

export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-background px-4">
      <div className="text-center">
        <h2 className="text-4xl font-bold text-primary mb-4">404</h2>
        <h3 className="text-2xl font-bold mb-4">الصفحة غير موجودة</h3>
        <p className="text-lg mb-6">عذرًا، الصفحة التي تبحث عنها غير موجودة.</p>
        <p className="text-base mb-8 text-gray-600">Sorry, the page you are looking for does not exist.</p>
        <Link href="/" className="btn btn-primary">
          العودة إلى الصفحة الرئيسية / Return Home
        </Link>
      </div>
    </div>
  )
}
