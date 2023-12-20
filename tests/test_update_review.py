import pytest

from implementations.restaurant_reviews import RestaurantReviews

def test_update_existing_review():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    result = reviews.update_review("Cafe Mocha", "Great coffee, pastries and atmosphere", 5)
    assert result == "Review updated for Cafe Mocha."
    assert reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee, pastries and atmosphere", "rating": 5}

def test_update_non_existing_review():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.update_review("Cafe Mocha", "Great coffee and pastries", 6)
    with pytest.raises(ValueError):
        reviews.update_review("Cafe Mocha", "Great coffee and pastries", 0)
    with pytest.raises(ValueError):
        reviews.update_review("Caf Mocha", "Great coffee and pastries", 4)
