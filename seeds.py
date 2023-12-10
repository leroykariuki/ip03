# seeds.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from migrations import Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
# Restaurants
restaurant1 = Restaurant(name='Tasty Delights', price=3)
restaurant2 = Restaurant(name='Gourmet Haven', price=4)
restaurant3 = Restaurant(name='Culinary Bliss', price=5)

# Customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')
customer3 = Customer(first_name='Bob', last_name='Johnson')

# Reviews
review1 = Review(star_rating=4, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=5, customer=customer2, restaurant=restaurant2)
review3 = Review(star_rating=3, customer=customer3, restaurant=restaurant3)

# Commit the changes
session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, customer3, review1, review2, review3])
session.commit()
