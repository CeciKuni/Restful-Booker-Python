import requests
from requests.auth import HTTPBasicAuth
from faker import Faker

fake = Faker()

def valid_authentication(URL, headers, payload):
    return requests.post(URL + "/auth", headers=headers, json=payload)


def create_booking(URL, headers, payload):
    return requests.post(URL + "/booking", headers=headers, json=payload)

def new_booking_payload():
    return {
    "firstname": fake.first_name(),
    "lastname": fake.last_name(),
    "totalprice": fake.random_int(),
    "depositpaid": True,
    "bookingdates": {
        "checkin": fake.past_date(),
        "checkout": fake.future_date()
    },
    "additionalneeds": fake.sentence()
    }


def get_all_bookings(URL):
    return requests.get(URL + "/booking")

def get_booking_id(URL, booking_id):
    return requests.get(URL + f"/booking/{booking_id}")

def partial_update_booking(URL, booking_id, headers, new_payload):
    return requests.patch(URL + f"/booking/{booking_id}", headers=headers, json=new_payload)

def update_booking(URL, booking_id, headers, new_payload):
    return requests.put(URL + f"/booking/{booking_id}", headers=headers, json=new_payload)

def delete_booking(URL, booking_id, headers):
    return requests.delete(URL + f"/booking/{booking_id}", headers=headers)
