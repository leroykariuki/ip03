# restaurant.py
from flask import session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from customer import Customer
from migrations import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')

    def reviews(self):
        return [review.star_rating for review in self.reviews]

    def customers(self):
        return [Customer.full_name() for review in self.reviews]

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]
