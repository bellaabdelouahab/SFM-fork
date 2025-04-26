"use client"

import type React from "react"

import { createContext, useContext, useState, useEffect } from "react"
import { translations } from "@/lib/translations"

type Language = "ar" | "en" | "fr"

interface TranslationContextType {
  t: (key: string) => string
  changeLanguage: (lang: Language) => void
  currentLanguage: Language
}

const TranslationContext = createContext<TranslationContextType | undefined>(undefined)

export function TranslationProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguage] = useState<Language>("ar")

  useEffect(() => {
    // Set HTML dir and lang attributes based on language
    const htmlElement = document.documentElement
    htmlElement.lang = language
    htmlElement.dir = language === "ar" ? "rtl" : "ltr"

    // Store language preference
    localStorage.setItem("language", language)
  }, [language])

  useEffect(() => {
    // Load saved language preference
    const savedLanguage = localStorage.getItem("language") as Language | null
    if (savedLanguage && ["ar", "en", "fr"].includes(savedLanguage)) {
      setLanguage(savedLanguage)
    }
  }, [])

  const t = (key: string): string => {
    return translations[language]?.[key] || translations.ar[key] || key
  }

  const changeLanguage = (lang: Language) => {
    setLanguage(lang)
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
