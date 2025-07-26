from playwright.sync_api import sync_playwright, Page, expect


class TicketConfirm:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role('heading', name='Thank you for your purchase')

    def confirm_msg(self):
        expect(self.heading).to_be_visible()

    def get_confirmation_details(self):
        booking_id = self.page.locator('xpath=//td[text()="Id"]/following-sibling::td').inner_text()
        status = self.page.locator('xpath=//td[text()="Status"]/following-sibling::td').inner_text()
        date = self.page.locator('xpath=//td[text()="Date"]/following-sibling::td').inner_text()
        return booking_id, status, date