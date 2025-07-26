from playwright.sync_api import sync_playwright, Page

class PurchaseFlight:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_role('textbox', name='Name', exact=True)
        self.address = page.get_by_role('textbox', name='Address')
        self.city = page.get_by_role('textbox', name='City')
        self.state = page.get_by_role('textbox', name='State')
        self.zipcode = page.get_by_role('textbox', name='Zip Code')
        self.cardtype = page.locator('#cardType')
        self.cc_number = page.get_by_role('textbox', name='Credit Card Number')
        self.month = page.get_by_role('textbox', name='Month')
        self.year = page.get_by_role('textbox', name='Year')
        self.nameoncard = page.get_by_role('textbox', name='Name on Card')
        self.purchasebutton = page.get_by_role('button', name='Purchase Flight')

    def purchase_flight(self, name, address, city, state, zip_code, card_type, card_number, month, year, name_on_card):
        self.name.fill(name)
        self.address.fill(address)
        self.city.fill(city)
        self.state.fill(state)
        self.zipcode.fill(str(zip_code))
        self.cardtype.select_option(card_type)
        self.cc_number.fill(str(card_number))
        self.month.fill(str(month))
        self.year.fill(str(year))
        self.nameoncard.fill(name_on_card)
        self.purchasebutton.click()