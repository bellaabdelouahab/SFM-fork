"use client"

import { useEffect } from "react"

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
  }, [error])

  return (
    <div className="min-h-screen flex items-center justify-center bg-background px-4">
      <div className="text-center">
        <h2 className="text-2xl font-bold text-primary mb-4">عذرًا، حدث خطأ ما</h2>
        <p className="text-lg mb-6">نواجه مشكلة في تحميل هذه الصفحة. يرجى المحاولة مرة أخرى.</p>
        <p className="text-base mb-8 text-gray-600">We're experiencing an issue loading this page. Please try again.</p>
        <button onClick={() => reset()} className="btn btn-primary">
          إعادة المحاولة / Try Again
        </button>
      </div>
    </div>
  )
}
