describe("Home Page", () => {
  beforeEach(() => {
    cy.visit("/")
  })

  it("displays the hero section", () => {
    cy.get("h1").should("contain", "الوصول إلى وربط الحلول المحلية")
    cy.get("input[type=text]").should("be.visible")
    cy.get("a").contains("اكتشف الحلول المحلية").should("be.visible")
    cy.get("a").contains("قدم خدماتك").should("be.visible")
  })

  it("allows searching", () => {
    cy.get("input[type=text]").type("carpenter")
    cy.get("button[type=submit]").click()
    // In a real test, we would check for search results or redirection
  })

  it("navigates to services page", () => {
    cy.get("nav").contains("التخييمات").click()
    cy.url().should("include", "/services")
    cy.get("h1").should("contain", "التخييمات")
  })

  it("changes language", () => {
    // Click on English language button
    cy.get("img[alt='English']").parent().click()

    // Check if the content is now in English
    cy.get("h1").should("contain", "Access and Connect to Local Solutions")

    // Click on French language button
    cy.get("img[alt='Français']").parent().click()

    // Check if the content is now in French
    cy.get("h1").should("contain", "Accès et Connexion aux Solutions Locales")
  })
})
