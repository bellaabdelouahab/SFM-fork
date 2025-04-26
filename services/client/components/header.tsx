"use client"

import { useState, useEffect } from "react"
import Link from "next/link"
import Image from "next/image"
import { usePathname } from "next/navigation"
import { Menu, X } from "lucide-react"
import { useTranslation } from "@/hooks/use-translation"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)
  const pathname = usePathname()
  const { t, changeLanguage, currentLanguage } = useTranslation()

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10)
    }

    window.addEventListener("scroll", handleScroll)
    return () => window.removeEventListener("scroll", handleScroll)
  }, [])

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen)
  }

  const closeMenu = () => {
    setIsMenuOpen(false)
  }

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? "bg-primary/95 shadow-md py-2" : "bg-transparent py-4"
      }`}
    >
      <div className="container-custom flex justify-between items-center">
        <div className="logo">
          <Link href="/" className="block">
            <span className="sr-only">الوصول إلى وربط الحلول المحلية</span>
            <span className="text-secondary bg-white rounded-full p-1 inline-block">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-8 h-8">
                <path
                  fillRule="evenodd"
                  d="M18.685 19.097A9.723 9.723 0 0021.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 003.065 7.097A9.716 9.716 0 0012 21.75a9.716 9.716 0 006.685-2.653zm-12.54-1.285A7.486 7.486 0 0112 15a7.486 7.486 0 015.855 2.812A8.224 8.224 0 0112 20.25a8.224 8.224 0 01-5.855-2.438zM15.75 9a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z"
                  clipRule="evenodd"
                />
              </svg>
            </span>
          </Link>
        </div>

        <nav className="hidden md:block">
          <ul className="flex space-x-8 space-x-reverse">
            {[
              { name: t("services"), href: `/${currentLanguage}/services` },
              { name: t("experiences"), href: `/${currentLanguage}/experiences` },
              { name: t("businesses"), href: `/${currentLanguage}/businesses` },
              { name: t("about"), href: `/${currentLanguage}/about` },
            ].map((item) => (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className={`text-white hover:text-secondary transition-colors ${
                    pathname === item.href ? "font-medium border-b-2 border-secondary" : ""
                  }`}
                >
                  {item.name}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        <div className="flex items-center space-x-4 space-x-reverse">
          <div className="flex space-x-2 space-x-reverse">
            <button
              onClick={() => changeLanguage("ar")}
              className={`rounded-full overflow-hidden w-8 h-8 transition-all ${
                currentLanguage === "ar" ? "ring-2 ring-secondary" : ""
              }`}
            >
              <Image src="https://flagcdn.com/w40/ma.png" alt="العربية" width={32} height={32} />
            </button>
            <button
              onClick={() => changeLanguage("en")}
              className={`rounded-full overflow-hidden w-8 h-8 transition-all ${
                currentLanguage === "en" ? "ring-2 ring-secondary" : ""
              }`}
            >
              <Image src="https://flagcdn.com/w40/gb.png" alt="English" width={32} height={32} />
            </button>
            <button
              onClick={() => changeLanguage("fr")}
              className={`rounded-full overflow-hidden w-8 h-8 transition-all ${
                currentLanguage === "fr" ? "ring-2 ring-secondary" : ""
              }`}
            >
              <Image src="https://flagcdn.com/w40/fr.png" alt="Français" width={32} height={32} />
            </button>
          </div>

          <button
            className="md:hidden text-white"
            onClick={toggleMenu}
            aria-label={isMenuOpen ? "Close menu" : "Open menu"}
          >
            {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {isMenuOpen && (
        <div className="md:hidden absolute top-full left-0 right-0 bg-primary/95 shadow-lg">
          <nav className="container-custom py-4">
            <ul className="flex flex-col space-y-4">
              {[
                { name: t("services"), href: `/${currentLanguage}/services` },
                { name: t("experiences"), href: `/${currentLanguage}/experiences` },
                { name: t("businesses"), href: `/${currentLanguage}/businesses` },
                { name: t("about"), href: `/${currentLanguage}/about` },
              ].map((item) => (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    className={`block text-white hover:text-secondary transition-colors ${
                      pathname === item.href ? "font-medium border-r-2 border-secondary pr-2" : ""
                    }`}
                    onClick={closeMenu}
                  >
                    {item.name}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      )}
    </header>
  )
}
