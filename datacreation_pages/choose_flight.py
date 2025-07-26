from playwright.sync_api import sync_playwright, Page

class ChooseFlight:
    def __init__(self, page: Page):
        self.page = page

    def choose_flight(self, flight_name: str):
        self.page.get_by_role('row', name=f'Choose This Flight {flight_name}').get_by_role('button').click()