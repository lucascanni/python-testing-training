import pytest

from implementations.restaurant_reviews import RestaurantReviews

# test restaurant existant
def test_delete_existing_review():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    result = reviews.delete_review("Cafe Mocha")
    assert result == "Review deleted for Cafe Mocha."
    
# test restaurant non existant
def test_delete_non_existing_review():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.delete_review("Caf Mocha")