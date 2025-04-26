"use client"

import type React from "react"

import { useEffect } from "react"
import { usePathname } from "next/navigation"

interface ErrorBoundaryProps {
  children: React.ReactNode
}

export function ErrorBoundary({ children }: ErrorBoundaryProps) {
  const pathname = usePathname()

  useEffect(() => {
    // This would typically come from your auth provider
    const user = null // Replace with actual user data when available

  }, [pathname])

  return <>{children}</>
}
