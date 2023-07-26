from api_functions import *
from requests.auth import HTTPBasicAuth
from faker import Faker

fake = Faker()


LOCAL_URL = "http://localhost:3001"
PROD_URL = "https://restful-booker.herokuapp.com"
USERNAME = "admin"
PASSWORD = "password123"


def test_smoke():
    # Authentication
    headers = {"Content-Type": "application/json"}
    payload = {"username": USERNAME, "password": PASSWORD}
    auth_response = valid_authentication(LOCAL_URL, headers, payload)
    print(auth_response.json())
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]

    # Create a booking
    headers = {"Content-Type": "application/json"}
    payload =  new_booking_payload()
    checkin_date_str = payload["bookingdates"]["checkin"].strftime('%Y-%m-%d')
    checkout_date_str = payload["bookingdates"]["checkout"].strftime('%Y-%m-%d')
    payload["bookingdates"]["checkin"] = checkin_date_str
    payload["bookingdates"]["checkout"] = checkout_date_str

    create_booking_response = create_booking(LOCAL_URL, headers, payload)
    assert create_booking_response.status_code == 200
    booking_id = create_booking_response.json()["bookingid"]
    print ("booking_id: " + str(booking_id))

    # Get the booking id
    get_booking_id_response = get_booking_id(LOCAL_URL, booking_id)
    assert get_booking_id_response.status_code == 200

    # Partial update the booking
    headers = {"Cookie": f"token=" + token}
    new_payload = {
        "totalprice": fake.random_int()
    }
    partial_update_response = partial_update_booking(LOCAL_URL, booking_id, headers, new_payload)
    assert partial_update_response.status_code == 200

    # Call put request
    headers = {"Cookie": f"token=" + token}
    new_payload = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(),
        "depositpaid": True,
        "bookingdates": {"checkin": fake.past_date(), "checkout": fake.future_date()},
        "additionalneeds": fake.sentence(),
    }
    checkin_date_str = new_payload["bookingdates"]["checkin"].strftime('%Y-%m-%d')
    checkout_date_str = new_payload["bookingdates"]["checkout"].strftime('%Y-%m-%d')
    new_payload["bookingdates"]["checkin"] = checkin_date_str
    new_payload["bookingdates"]["checkout"] = checkout_date_str
    update_booking_response = update_booking(LOCAL_URL, booking_id, headers, new_payload)
    assert update_booking_response.status_code == 200

    # Delete the booking
    headers = {"Cookie": f"token=" + token}
    delete_booking_response = delete_booking(LOCAL_URL, booking_id, headers)
    assert delete_booking_response.status_code == 201

    # Validate the deleted booking
    get_booking_id_response = get_booking_id(LOCAL_URL, booking_id)
    assert get_booking_id_response.status_code == 404

    # Call Get all bookings to validate the deleted booking
    get_all_bookings_response = get_all_bookings(LOCAL_URL)
    for booking in get_all_bookings_response:
        assert "booking_id" not in str(booking_id)


