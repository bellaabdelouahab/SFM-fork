import { ReactNode, Suspense } from "react";
import { TranslationProvider } from "@/contexts/translation-context";
import { Tajawal } from "next/font/google";
import { Providers } from "@/components/providers"; // Import Providers
import { Analytics } from "@/components/analytics";
import { ErrorBoundary } from "@/components/error-boundary";
import "../globals.css";

// Define font here
const tajawal = Tajawal({
  subsets: ["arabic", "latin"],
  weight: ["300", "400", "500", "700"],
  variable: "--font-tajawal",
});

// Metadata can potentially be generated dynamically here if needed based on locale
// export async function generateMetadata({ params }: { params: { locale: string } }) { ... }

export default async function LocaleLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: { locale: string };
}) {
  const { locale } = await params;
  const dir = locale === "ar" ? "rtl" : "ltr";

  return (
    <html lang={locale} dir={dir} className="dark" style={{ colorScheme: "dark" }} suppressHydrationWarning>
      <body className={`${tajawal.variable} font-sans`}>
        {/* Wrap content with Providers immediately inside body */}
        <Providers>
          <ErrorBoundary>
            <TranslationProvider>
              <Suspense>{children}</Suspense>
              <Analytics />
            </TranslationProvider>
          </ErrorBoundary>
        </Providers>
      </body>
    </html>
  );
}
