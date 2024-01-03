import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

def test_get_existing_review():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    result = reviews.get_review("Cafe Mocha")
    assert result == {"review_text": "Great coffee and pastries", "rating": 4}

def test_get_review_with_fixture():
    reviews = RestaurantReviews()
    reviews.add_review(restaurant_reviews_with_two_reviews())
    result = reviews.get_review("Cafe Mocha")
    assert result == {"review_text": "Great coffee and pastries", "rating": 4}

def test_get_non_existing_review():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.get_review("Caf Mocha")