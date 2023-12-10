# customer.py
from flask import session
from sqlalchemy import Column, Integer, String
from migrations import Base, Restaurant, Review

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')

    def reviews(self):
        return [review.full_review() for review in self.reviews]

    def restaurants(self):
        return [restaurant.name for review in self.reviews]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Implement logic to find the restaurant with the highest star rating
        return session.query(Restaurant).join(Review).filter(Review.customer == self).order_by(Review.star_rating.desc()).first()

    def add_review(self, restaurant, rating):
        new_review = Review(star_rating=rating, customer=self, restaurant=restaurant)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        session.query(Review).filter(Review.customer == self, Review.restaurant == restaurant).delete()
        session.commit()
