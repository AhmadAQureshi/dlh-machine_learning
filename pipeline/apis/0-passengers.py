#!/usr/bin/env python3
"""
Retrieve starships that can hold a specified number of passengers.
"""

import requests


def availableShips(passengerCount):
    """
    Return a list of starship names that can hold passengerCount passengers.
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "")

            if passengers.isdigit():
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])

        url = data["next"]

    return ships