#sayings.py
#Tps25-Capstone
#Date: 02-Aug-2025

'''
File for sayings. Sayings are broken up by weather type and are tied to icons.

'''


SUNNY = [
    "A sunny day keeps the bugs away.",
    "If you're in Phoenix and see vultures over your head, don't worry. It's a dry heat.",
    "Eos d'erchomenē, rhododaktylos, exéphēne\n(When the child of morning, rosy-fingered Dawn, appeared.)\n— Homer, The Odyssey",
    "Do not stare at the sun. It's bad for your eyes. It's bad for your eyes and besides, the sun hates being stared at."
]

RAIN = [
    "It's raining so much, I'm thinking about building a boat.",
    "The Ferengi have 178 words for rain; right now it's glebbening out there. And that's bad.",
    "Every time it rains, my mother makes soup... I hate soup.",
    "Seattle has 2 forecasts: it's raining and it's about to rain."
]

FUNNY = [
    "The weatherman predicted 10 inches of snow, we got 34. So they were 2 feet off. If you were a roofer and were 2 feet off... you'd still be in jail. — Lewis Black",
    "Weatherman means liar. — Lewis Black",
    "Tornadoes — I don't like air I can see.",
    "How dare you! — Greta Thunberg",
    "The weather is like the government, always in the wrong. — Jerome K. Jerome"
]

THUNDER = [
    "They say lightning never strikes twice in the same place... tell that to Frankenstein.",
    "In Norse mythology, thunder is attributed to Thor and his hammer Mjolnir. His two goats might also have something to do with it.",
    "In Japanese mythology, thunder is attributed to Raijin and his awesome drum set.",
    "In Taíno mythology (Caribbean), Guabancex is the goddess of storms, chaos, and destruction. Not a happy person."
]


SAYINGS_BY_WEATHER = {
    "sunny": SUNNY,
    "rain": RAIN,
    "thunder": THUNDER,
    "funny": FUNNY,
    "default": FUNNY  # pick whatever you like as default
}

ICON_TO_SAYINGS_KEY = {
    "01d": "sunny", "01n": "sunny",
    "02d": "sunny", "02n": "sunny",
    "03d": "cloudy", "03n": "cloudy",
    "04d": "cloudy", "04n": "cloudy",
    "09d": "rain", "09n": "rain",
    "10d": "rain", "10n": "rain",
    "11d": "thunder", "11n": "thunder",
    "13d": "snow", "13n": "snow",
    "50d": "haze", "50n": "haze",
}