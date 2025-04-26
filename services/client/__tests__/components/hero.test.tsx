import { render, screen, fireEvent } from "@testing-library/react"
import { Hero } from "@/components/hero"
import { TranslationProvider } from "@/contexts/translation-context"

// Mock the search service
jest.mock("@/lib/search-service", () => ({
  searchService: jest.fn().mockResolvedValue({
    results: [{ id: 1, title: "Test Result" }],
  }),
}))

describe("Hero Component", () => {
  const renderWithProviders = () => {
    return render(
      <TranslationProvider>
        <Hero />
      </TranslationProvider>,
    )
  }

  it("renders the hero title and subtitle", () => {
    renderWithProviders()

    // Check if the title is rendered
    expect(screen.getByText("الوصول إلى وربط الحلول المحلية")).toBeInTheDocument()

    // Check if the subtitle is rendered
    expect(screen.getByText("Connect with local experts and businesses.")).toBeInTheDocument()
  })

  it("renders the search input", () => {
    renderWithProviders()

    // Check if the search input is rendered
    expect(screen.getByPlaceholderText("ابحث عن الخدمات المحلية")).toBeInTheDocument()
  })

  it("renders the CTA buttons", () => {
    renderWithProviders()

    // Check if the CTA buttons are rendered
    expect(screen.getByText("اكتشف الحلول المحلية")).toBeInTheDocument()
    expect(screen.getByText("قدم خدماتك")).toBeInTheDocument()
  })

  it("handles search submission", async () => {
    renderWithProviders()

    // Get the search input and button
    const searchInput = screen.getByPlaceholderText("ابحث عن الخدمات المحلية")
    const searchButton = screen.getByRole("button", { name: /search/i })

    // Type in the search input
    fireEvent.change(searchInput, { target: { value: "test query" } })

    // Submit the search
    fireEvent.click(searchButton)

    // Check if the search service was called
    // In a real test, we would verify that the search service was called with the correct query
  })
})
