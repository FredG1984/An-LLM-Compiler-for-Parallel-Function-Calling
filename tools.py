
from groq import Groq
from products import (
    get_cheapest_product,
    get_product_info
)
import os
import time
from dotenv import load_dotenv

load_dotenv()

_=os.getenv()
client = Groq()

def get_popular_places(country):
    """Look up popular places information by ID."""
    time.sleep(3)
    places = {
        "France": [
            "Paris",
            "Nice",
            "Lyon",
            "Marseille"
        ],
        "Germany": [
            "Berlin",
            "Hamburg",
            "Bremen",
            "Kiel",
            "Lübeck",
            "Schwerin",
            "Flensburg",
            "Wilhelmshaven",
            "Aurich",
            "Stuttgart",
            "Düsseldorf",
            "Dortmund",
            "Osnabrück"
        ],
        "Sweden": [
            "Stockholm",
            "Götenburg",
            "Malmö",
            "Uppsala"
        ],
        "Italy":[
            "Rom",
            "Florenz",
            "Venedig",
            "San Marino",
            "Neapel",
            "Mailand"
        ]
    }
    return places.get(country, [])

def final_answer(context):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                Create a natural final answer for the user
                based on the tool results.
                """
            },
            {
                "role": "user",
                "content": str(context)
            }
        ]
    )

    return response.choices[0].message.content

TOOLS = {
    "get_product_info": get_product_info,
    "get_popular_places": get_popular_places,
    "get_cheapest_product": get_cheapest_product,
    "final_answer": final_answer
}