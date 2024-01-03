import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

# test restaurant existant
def test_delete_existing_review():
    reviews = RestaurantReviews()
    reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    result = reviews.delete_review("Cafe Mocha")
    assert result == "Review deleted for Cafe Mocha."

# test restaurant existant with fixture
def test_delete_review_with_fixture(restaurant_reviews_with_two_reviews):
    assert restaurant_reviews_with_two_reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee and pastries", "rating": 4}
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") == {"review_text": "Fresh sushi", "rating": 4}
    restaurant_reviews_with_two_reviews.delete_review("Cafe Mocha")
    with pytest.raises(ValueError):
        restaurant_reviews_with_two_reviews.get_review("Cafe Mocha")
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") == {"review_text": "Fresh sushi", "rating": 4}
    
# test restaurant non existant
def test_delete_non_existing_review():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.delete_review("Caf Mocha")