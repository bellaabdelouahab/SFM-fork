import { User, Handshake, LightbulbIcon } from "lucide-react"
import { useTranslation } from "@/hooks/use-translation"

export function Features() {
  const { t } = useTranslation()

  const features = [
    {
      icon: <User className="w-6 h-6 text-primary" />,
      title: t("accessExpertise"),
      description: t("accessExpertiseFr"),
    },
    {
      icon: <Handshake className="w-6 h-6 text-primary" />,
      title: t("supportBusinesses"),
      description: t("supportBusinessesFr"),
    },
    {
      icon: <LightbulbIcon className="w-6 h-6 text-primary" />,
      title: t("findIdeas"),
      description: t("findIdeasFr"),
    },
  ]

  return (
    <section className="bg-white py-12 md:py-16">
      <div className="container-custom">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div key={index} className="flex items-start space-x-4 space-x-reverse">
              <div className="flex-shrink-0 p-2">{feature.icon}</div>
              <div>
                <h3 className="text-lg font-medium text-primary mb-1">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
