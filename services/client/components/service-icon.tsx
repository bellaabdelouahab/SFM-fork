"use client"

import { useEffect, useState } from "react"
import { Lightbulb, LightbulbIcon, MessageCircle } from "lucide-react"

interface ServiceIconProps {
  icon: string
  title: string
  animate?: boolean
  delay?: number
}

export function ServiceIcon({ icon, title, animate = false, delay = 0 }: ServiceIconProps) {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    if (animate) {
      const timer = setTimeout(() => {
        setIsVisible(true)
      }, delay)
      return () => clearTimeout(timer)
    }
  }, [animate, delay])

  const renderIcon = () => {
    switch (icon) {
      case "Lightbulb":
        return <Lightbulb className="w-8 h-8 text-white" />
      case "LightbulbIcon":
        return <LightbulbIcon className="w-8 h-8 text-white" />
      case "MessageCircle":
        return <MessageCircle className="w-8 h-8 text-white" />
      default:
        return <Lightbulb className="w-8 h-8 text-white" />
    }
  }

  return (
    <div
      className={`flex flex-col items-center transition-all duration-500 ${
        isVisible ? "opacity-100 transform-none" : "opacity-0 translate-y-4"
      }`}
    >
      <div className="icon-circle">{renderIcon()}</div>
      <h3 className="text-white text-center font-medium whitespace-pre-line">{title}</h3>
    </div>
  )
}
