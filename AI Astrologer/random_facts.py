# facts.py
import random

ASTRO_FACTS = [
    "Your Ascendant changes roughly every two hours ⏳",
    "The Moon influences your emotions 🌙",
    "Mercury retrograde is often blamed for miscommunication 💬",
    "Venus represents love and relationships 💕",
    "Mars represents energy and drive 🔥",
    "Jupiter is linked with luck and growth 🍀",
    "Saturn is the planet of discipline and lessons 📘",
    "Neptune rules dreams and intuition 🌊",
    "Pluto relates to transformation and rebirth 🌀"
]

def random_fact():
    return random.choice(ASTRO_FACTS)
