"use client"

import { useEffect } from "react"
import { usePathname, useSearchParams } from "next/navigation"
import * as Sentry from "@sentry/nextjs"

export function Analytics() {
  const pathname = usePathname()
  const searchParams = useSearchParams()

  useEffect(() => {
    const url = pathname + (searchParams?.toString() ? `?${searchParams.toString()}` : "")

    // Track page views
    if (process.env.NEXT_PUBLIC_ANALYTICS_ENABLED === "true") {
      // Example analytics call
      console.log(`Page view: ${url}`)
    }

    // Set Sentry breadcrumb for navigation
    Sentry.addBreadcrumb({
      category: "navigation",
      message: `Navigation to ${url}`,
      level: "info",
    })
  }, [pathname, searchParams])

  return null
}
