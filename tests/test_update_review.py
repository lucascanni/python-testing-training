import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

def test_update_existing_review():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    result = reviews.update_review("Cafe Mocha", "Great coffee, pastries and atmosphere", 5)
    assert result == "Review updated for Cafe Mocha."
    assert reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee, pastries and atmosphere", "rating": 5}

def test_update_non_existing_review():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.update_review("Caf Mocha", "Great coffee and pastries", 4)

def test_update_invalid_rating():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    with pytest.raises(ValueError):
        reviews.update_review("Cafe Mocha", "Great coffee and pastries", 6)
    with pytest.raises(ValueError):
        reviews.update_review("Cafe Mocha", "Great coffee and pastries", 0)

def test_update_review_with_fixture(restaurant_reviews_with_two_reviews):
    assert restaurant_reviews_with_two_reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee and pastries", "rating": 4}
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") == {"review_text": "Fresh sushi", "rating": 4}
    restaurant_reviews_with_two_reviews.update_review("Cafe Mocha", "Great coffee, pastries and atmosphere", 5)
    assert restaurant_reviews_with_two_reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee, pastries and atmosphere", "rating": 5}
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") == {"review_text": "Fresh sushi", "rating": 4}

def test_update_review_with_fixture_invalid_rating(restaurant_reviews_with_two_reviews):
    with pytest.raises(ValueError):
        restaurant_reviews_with_two_reviews.update_review("Cafe Mocha", "Great coffee and pastries", 6)
    with pytest.raises(ValueError):
        restaurant_reviews_with_two_reviews.update_review("Cafe Mocha", "Great coffee and pastries", 0)