import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.conftest import restaurant_reviews_with_two_reviews

def test_add_review():
    reviews = RestaurantReviews()
    result = reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    assert result == "Review added for Cafe Mocha."
    assert reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee and pastries", "rating": 4}

def test_add_review_with_fixture(restaurant_reviews_with_two_reviews):
    assert restaurant_reviews_with_two_reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee and pastries", "rating": 4}
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") == {"review_text": "Fresh sushi", "rating": 4}

def test_add_invalid_rating():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.add_review("Cafe Mocha", "Great coffee and pastries", 6)
    with pytest.raises(ValueError):
        reviews.add_review("Cafe Mocha", "Great coffee and pastries", 0)