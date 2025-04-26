import { type NextRequest, NextResponse } from "next/server"

export async function GET(request: NextRequest) {
  try {
    const searchParams = request.nextUrl.searchParams
    const query = searchParams.get("q") || ""

    // In a real app, this would query a database or external API
    // For now, we'll return mock data
    const results = [
      { id: 1, title: "Local Carpenter", category: "Services" },
      { id: 2, title: "Moroccan Cuisine Expert", category: "Food" },
      { id: 3, title: "Tour Guide in Marrakech", category: "Tourism" },
    ].filter(
      (item) =>
        item.title.toLowerCase().includes(query.toLowerCase()) ||
        item.category.toLowerCase().includes(query.toLowerCase()),
    )

    return NextResponse.json({
      results,
      query,
      timestamp: new Date().toISOString(),
    })
  } catch (error) {

    return NextResponse.json({ error: "An error occurred while processing your request" }, { status: 500 })
  }
}
