import pytest
from datacreation_pages.choose_route import ChooseRoute
from datacreation_pages.choose_flight import ChooseFlight
from datacreation_pages.purchase_ticket import PurchaseFlight
from datacreation_pages.ticket_confirmation import TicketConfirm
from utils.sheet_reader import read_ticket_data
from utils.sheet_writer import write_confirmation

ticket_test_data = read_ticket_data("ticket_data.xlsx")

@pytest.mark.parametrize("row_index, row", enumerate(ticket_test_data))
def test_book_ticket(page, row_index, row):
    from_city = row[0]
    to_city = row[1]
    flight_name = row[2]
    name = row[3]
    address = row[4]
    city = row[5]
    state = row[6]
    zip_code = row[7]
    card_type = row[8]
    card_number = row[9]
    month =row[10]
    year = row[11]
    name_on_card = row[12]

# Choose Route
    route_page = ChooseRoute(page)
    route_page.navigate_flightbooking()
    route_page.select_route(from_city, to_city)

# Choose Flight
    flight_page = ChooseFlight(page)
    flight_page.choose_flight(flight_name)

# Purchase Ticket
    ticket_page = PurchaseFlight(page)
    ticket_page.purchase_flight(name, address, city, state, zip_code, card_type, card_number, month, year, name_on_card)

# Confirmation Message
    confirm_page = TicketConfirm(page)
    confirm_page.confirm_msg()
    booking_id, status, date = confirm_page.get_confirmation_details()

#Write confirmation back to sheet
    write_confirmation("ticket_data.xlsx", row_index, booking_id,status, date)
