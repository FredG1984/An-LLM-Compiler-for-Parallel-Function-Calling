PRODUCTS = {
    "Ethiopian-Yirgacheffe": {
        "name": "Ethiopian Yirgacheffe Single-Origin",
        "origin": "Yirgacheffe region, Ethiopia",
        "flavor_profile":"Bright citrus, floral aroma, light body",
        "price":18.99,
        "certifications": ["Fair Trade", "Oraganic"]
    },
    "House-Blend": {
        "name": "GlobalJava House Blend",
        "origin": "Colombia and Brazil blend",
        "flavor_profile":"Balanced, chocolatey,nutty",
        "price": 12.99,
        "certifications":[]
    },
    "Geisha-Reserve": {
        "name":"Limited Edition Geisha Reserve",
        "origin": "Hacienda La Esmeralda, Panama",
        "flavor_profile":"Jasmine, bergamot, white peach",
        "price": 89.99,
        "certifications": ["Single Estate","Competition Grade"]
    }
}

def get_product_info(product_id: str)-> dict:
    """Look up product information by ID."""
    if product_id not in PRODUCTS:
        return {"error": f"Product '{product_id}' not found"}
    return PRODUCTS[product_id]


def get_cheapest_product(_=None):

    cheapest = min(
        PRODUCTS.items(),
        key=lambda x: x[1]["price"]
    )
    return cheapest