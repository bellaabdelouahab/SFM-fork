import * as Sentry from "@sentry/nextjs"

export async function searchService(query: string): Promise<any> {
  try {
    // In a real app, this would be an API call to your search service
    // For now, we'll simulate a delay and return mock data
    await new Promise((resolve) => setTimeout(resolve, 500))

    // Mock search results
    return {
      results: [
        { id: 1, title: "Local Carpenter", category: "Services" },
        { id: 2, title: "Moroccan Cuisine Expert", category: "Food" },
        { id: 3, title: "Tour Guide in Marrakech", category: "Tourism" },
      ],
      query,
      timestamp: new Date().toISOString(),
    }
  } catch (error) {
    // Log error to Sentry
    Sentry.captureException(error, {
      tags: {
        feature: "search",
      },
      extra: {
        query,
      },
    })

    // Re-throw for component handling
    throw error
  }
}
