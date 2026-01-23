import sys
import os
import random
from faker import Faker

# Setup the Python path to fine 'app' inside 'src'
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.database.core import SessionLocal
from app.models import Item, Wear

fake = Faker()

CATEGORIES = ["Tops", "Bottoms", "Shoes", "Outerwear", "Accessories"]
BRANDS = ["Nike", "Uniqlo", "Zara", "Levi's", "Thrifted", "Patagonia"]
CLOTHING_NOUNS = ["Hoodie", "Jeans", "T-Shirt", "Jacket", "Sneakers", "Boots"]

def seed_database():
    with SessionLocal() as session:
        print("Seeding database... (20 items, 5 wears each)")

        items_to_add = []

        for _ in range(50):
            item_name = f"{fake.color_name()} {random.choice(CLOTHING_NOUNS)}"

            item = Item(
                name=item_name,
                category=random.choice(CATEGORIES),
                brand=random.choice(BRANDS),
                purchase_price=random.randint(1, 100),
                purchase_date=fake.date(),
                tags=[fake.word(), fake.word()],
            )

            for _ in range(4):
                # Create wears
                wear = Wear(
                    item=item,
                    worn_at=fake.date(),
                    context=fake.text(),
                )
                session.add(wear)

            items_to_add.append(item)

    session.add_all(items_to_add)
    session.commit()
    print("Seeded database")

if __name__ == "__main__":
    seed_database()
