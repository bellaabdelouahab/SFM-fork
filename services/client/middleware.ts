import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const PUBLIC_FILE = /\.(.*)$/;
const SUPPORTED_LOCALES = ["ar", "en", "fr"];
const DEFAULT_LOCALE = "ar";

export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;

  // Skip public files and API routes
  if (PUBLIC_FILE.test(pathname) || pathname.startsWith("/api")) {
    return NextResponse.next();
  }

  // Check if the pathname already includes a locale
  const pathnameParts = pathname.split("/");
  const locale = pathnameParts[1];

  if (SUPPORTED_LOCALES.includes(locale)) {
    return NextResponse.next();
  }

  // Redirect to the default locale if no locale is present
  const url = request.nextUrl.clone();
  url.pathname = `/${DEFAULT_LOCALE}${pathname}`;
  return NextResponse.redirect(url);
}
