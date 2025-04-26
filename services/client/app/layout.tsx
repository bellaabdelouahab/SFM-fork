import type React from "react"
import type { Metadata } from "next"
import { Tajawal } from "next/font/google"
import "./globals.css"
import { Providers } from "@/components/providers"
import { Analytics } from "@/components/analytics"
import { ErrorBoundary } from "@/components/error-boundary"
import { Suspense } from "react"

const tajawal = Tajawal({
  subsets: ["arabic", "latin"],
  weight: ["300", "400", "500", "700"],
  variable: "--font-tajawal",
})

export const metadata: Metadata = {
  title: "الوصول إلى وربط الحلول المحلية",
  description: "Connect with local experts and businesses in Morocco",
    generator: 'v0.dev'
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="ar" dir="rtl" suppressHydrationWarning>
      <body className={`${tajawal.variable} font-sans`}>
        <ErrorBoundary>
          <Providers>
            <Suspense>{children}</Suspense>
            <Analytics />
          </Providers>
        </ErrorBoundary>
      </body>
    </html>
  )
}
