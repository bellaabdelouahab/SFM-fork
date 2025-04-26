"use client"

import { useEffect } from "react"
import { usePathname, useSearchParams } from "next/navigation"

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

  }, [pathname, searchParams])

  return null
}
