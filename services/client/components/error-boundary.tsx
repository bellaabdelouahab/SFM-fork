"use client"

import type React from "react"

import { useEffect } from "react"
import * as Sentry from "@sentry/nextjs"
import { usePathname } from "next/navigation"

interface ErrorBoundaryProps {
  children: React.ReactNode
}

export function ErrorBoundary({ children }: ErrorBoundaryProps) {
  const pathname = usePathname()

  useEffect(() => {
    // Set user context for Sentry if user is logged in
    // This would typically come from your auth provider
    const user = null // Replace with actual user data when available

    if (user) {
      Sentry.setUser({
        id: user.id,
        email: user.email,
      })
    } else {
      Sentry.setUser(null)
    }
  }, [pathname])

  return <>{children}</>
}
