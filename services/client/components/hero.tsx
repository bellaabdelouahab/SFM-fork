"use client"

import type React from "react"

import { useState, useEffect } from "react"
import { Search } from "lucide-react"
import { useTranslation } from "@/hooks/use-translation"
import { ServiceIcon } from "@/components/service-icon"
import { searchService } from "@/lib/search-service"

export function Hero() {
  const [searchQuery, setSearchQuery] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [animateIcons, setAnimateIcons] = useState(false)
  const { t } = useTranslation()

  useEffect(() => {
    // Trigger animation after component mounts
    const timer = setTimeout(() => {
      setAnimateIcons(true)
    }, 100)

    return () => clearTimeout(timer)
  }, [])

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!searchQuery.trim()) return

    try {
      setIsLoading(true)
      await searchService(searchQuery)
      // Handle search results
    } catch (error) {
      console.error("Search error:", error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <section className="relative min-h-screen flex flex-col items-center justify-center py-16 px-4">
      {/* Background */}
      <div
        className="absolute inset-0 z-0 bg-cover bg-center bg-no-repeat"
        style={{
          backgroundImage:
            "linear-gradient(rgba(10, 74, 76, 0.85), rgba(10, 74, 76, 0.85)), url('/images/morocco-background.jpg')",
        }}
      >
        {/* Pattern overlay */}
        <div
          className="absolute inset-0"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Cpath fill='%23ffffff10' d='M50 0C22.388 0 0 22.388 0 50s22.388 50 50 50 50-22.388 50-50S77.612 0 50 0zm20 77c-14.912 0-27-12.088-27-27s12.088-27 27-27 27 12.088 27 27-12.088 27-27 27zm-40-50c-14.088 0-25 12.088-25 27s12.088 27 27 27 27-12.088 27-27-12.088-27-27-27z'/%3E%3C/svg%3E")`,
            opacity: 0.1,
          }}
        />
      </div>

      <div className="container-custom relative z-10 flex flex-col items-center">
        {/* Service Icons */}
        <div className="flex flex-col md:flex-row justify-center gap-8 md:gap-20 mb-10 md:mb-16">
          <ServiceIcon icon="LightbulbIcon" title={t("intelligentSearch")} animate={animateIcons} delay={0} />
          <ServiceIcon icon="Lightbulb" title={t("solutionIdeas")} animate={animateIcons} delay={200} />
          <ServiceIcon icon="MessageCircle" title={t("linkProvider")} animate={animateIcons} delay={400} />
        </div>

        {/* Hero Content */}
        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-4 slide-up">{t("heroTitle")}</h1>
          <p className="text-xl md:text-2xl text-white font-light mb-1 slide-up">{t("heroSubtitle")}</p>
          <p className="text-lg md:text-xl text-white/80 font-light mb-8 slide-up">{t("heroSubtitleFr")}</p>

          {/* Search */}
          <form onSubmit={handleSearch} className="w-full max-w-2xl mx-auto mb-10 fade-in">
            <div className="relative flex items-center">
              <input
                type="text"
                placeholder={t("searchPlaceholder")}
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full py-4 px-6 pr-12 rounded-full text-gray-700 focus:outline-none focus:ring-2 focus:ring-primary/50 shadow-lg"
                disabled={isLoading}
              />
              <button
                type="submit"
                className="absolute left-3 text-primary hover:text-primary/80 transition-colors"
                disabled={isLoading}
              >
                <Search size={24} />
                <span className="sr-only">{t("search")}</span>
              </button>
            </div>
          </form>

          {/* CTA Buttons */}
          <div className="flex flex-col md:flex-row justify-center gap-4 md:gap-8 fade-in">
            <a href="/discover" className="btn btn-primary min-w-[250px] flex flex-col items-center">
              <span className="text-lg font-bold">{t("discoverSolutions")}</span>
              <span className="text-sm font-normal">{t("discoverSolutionsEn")}</span>
            </a>
            <a href="/offer" className="btn btn-secondary min-w-[250px] flex flex-col items-center">
              <span className="text-lg font-bold">{t("offerServices")}</span>
              <span className="text-sm font-normal">{t("offerServicesFr")}</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
