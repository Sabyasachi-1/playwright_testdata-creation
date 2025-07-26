from playwright.sync_api import sync_playwright, Page

class ChooseRoute:
    def __init__(self, page: Page):
        self.page = page
        self.departurecity = page.locator('select[name="fromPort"]')
        self.destinationcity = page.locator('select[name="toPort"]')
        self.findflight = page.get_by_role('button', name='Find Flights')

    def navigate_flightbooking (self):
        self.page.goto("https://blazedemo.com/")

    def select_route (self, from_city, to_city):
        self.departurecity.select_option(label=from_city)
        self.destinationcity.select_option(label=to_city)
        self.findflight.click()
