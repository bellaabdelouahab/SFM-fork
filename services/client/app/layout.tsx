import type React from "react"
import type { Metadata } from "next"
import "./globals.css"
import { Providers } from "@/components/providers"
import { Analytics } from "@/components/analytics"
import { ErrorBoundary } from "@/components/error-boundary"
import { Suspense } from "react"

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
    <ErrorBoundary>
      <Providers>
        <Suspense>{children}</Suspense>
        <Analytics />
      </Providers>
    </ErrorBoundary>
  )
}
