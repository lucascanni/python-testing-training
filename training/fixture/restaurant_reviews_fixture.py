import pytest

from implementations.restaurant_reviews import RestaurantReviews

@pytest.fixture
def restaurant_reviews_with_two_reviews():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    reviews.add_review("Sushi Express", "Fresh sushi", 4)
    return reviews