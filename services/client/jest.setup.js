// Learn more: https://github.com/testing-library/jest-dom
import "@testing-library/jest-dom"

// Mock next/navigation
jest.mock("next/navigation", () => ({
  useRouter: () => ({
    push: jest.fn(),
    replace: jest.fn(),
    prefetch: jest.fn(),
  }),
  useSearchParams: () => ({
    get: jest.fn(),
  }),
  usePathname: () => "/",
}))

// Mock next/image
jest.mock("next/image", () => ({
  __esModule: true,
  default: (props) => {
    // eslint-disable-next-line @next/next/no-img-element
    return <img {...props} alt={props.alt} />
  },
}))

// Mock environment variables
process.env.NEXT_PUBLIC_SENTRY_DSN = "https://example@sentry.io/123"
process.env.NEXT_PUBLIC_ANALYTICS_ENABLED = "false"
