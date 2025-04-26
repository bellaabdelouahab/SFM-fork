describe("Navigation", () => {
  beforeEach(() => {
    cy.visit("/")
  })

  it("navigates between pages", () => {
    // Navigate to Services page
    cy.get("nav").contains("التخييمات").click()
    cy.url().should("include", "/services")

    // Navigate to Experiences page
    cy.get("nav").contains("البكيفيات").click()
    cy.url().should("include", "/experiences")

    // Navigate to Businesses page
    cy.get("nav").contains("للشركات").click()
    cy.url().should("include", "/businesses")

    // Navigate to About page
    cy.get("nav").contains("معلومات عنا").click()
    cy.url().should("include", "/about")

    // Navigate back to Home page
    cy.get(".logo a").click()
    cy.url().should("not.include", "/about")
  })

  it("shows mobile menu on small screens", () => {
    // Set viewport to mobile size
    cy.viewport("iphone-6")

    // Check that the menu button is visible
    cy.get("button[aria-label='Open menu']").should("be.visible")

    // Click the menu button
    cy.get("button[aria-label='Open menu']").click()

    // Check that the menu items are visible
    cy.get("nav").contains("التخييمات").should("be.visible")
    cy.get("nav").contains("البكيفيات").should("be.visible")
    cy.get("nav").contains("للشركات").should("be.visible")
    cy.get("nav").contains("معلومات عنا").should("be.visible")

    // Click a menu item
    cy.get("nav").contains("التخييمات").click()

    // Check that we navigated to the correct page
    cy.url().should("include", "/services")
  })
})
