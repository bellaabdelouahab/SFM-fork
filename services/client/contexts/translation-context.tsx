"use client"

import type React from "react"
import { createContext, useContext, useState, useEffect } from "react"
import { translations } from "@/lib/translations"
import { useParams, usePathname, useRouter } from "next/navigation" // Import hooks

type Language = "ar" | "en" | "fr"

interface TranslationContextType {
  t: (key: string) => string
  changeLanguage: (lang: Language) => void
  currentLanguage: Language
}

const TranslationContext = createContext<TranslationContextType | undefined>(undefined)

export function TranslationProvider({ children }: { children: React.ReactNode }) {
  const router = useRouter()
  const pathname = usePathname()
  const params = useParams()
  const initialLocale = params.locale as Language || "ar" // Get locale from URL params

  const [language, setLanguage] = useState<Language>(initialLocale)

  useEffect(() => {
    // Update language state if URL locale changes
    const currentPathLocale = pathname.split('/')[1] as Language
    if (currentPathLocale && ["ar", "en", "fr"].includes(currentPathLocale) && currentPathLocale !== language) {
      setLanguage(currentPathLocale)
    }
  }, [pathname, language])

  useEffect(() => {
    // Set HTML dir and lang attributes based on language
    const htmlElement = document.documentElement
    htmlElement.lang = language
    htmlElement.dir = language === "ar" ? "rtl" : "ltr"

    // Store language preference (optional, URL is primary source now)
    // localStorage.setItem("language", language)
  }, [language])

  const t = (key: string): string => {
    return translations[language]?.[key] || translations.ar[key] || key
  }

  const changeLanguage = (lang: Language) => {
    if (lang !== language) {
      const newPathname = pathname.replace(`/${language}`, `/${lang}`)
      setLanguage(lang) // Update state immediately for UI responsiveness
      router.push(newPathname) // Navigate to the new locale path
    }
  }

  return (
    <TranslationContext.Provider value={{ t, changeLanguage, currentLanguage: language }}>
      {children}
    </TranslationContext.Provider>
  )
}

export const useTranslationContext = () => {
  const context = useContext(TranslationContext)
  if (context === undefined) {
    throw new Error("useTranslationContext must be used within a TranslationProvider")
  }
  return context
}
