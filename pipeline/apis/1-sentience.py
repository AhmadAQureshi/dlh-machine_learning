#!/usr/bin/env python3
"""
Returns the home planets of all sentient species using the SWAPI API.
"""

import requests


def sentientPlanets():
    """
    Return a list containing the home planet names of sentient species.
    """
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data["results"]:
            classification = species["classification"]
            designation = species["designation"]

            if classification == "sentient" or designation == "sentient":
                homeworld = species["homeworld"]

                if homeworld:
                    planet_response = requests.get(homeworld)
                    planet_data = planet_response.json()
                    planets.append(planet_data["name"])

        url = data["next"]

    return planets