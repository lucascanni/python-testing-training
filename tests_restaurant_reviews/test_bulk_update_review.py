import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

# Parametrization update valid review
@pytest.mark.parametrize("restaurant, new_review_text, new_rating, expected", [
    ("Cafe Mocha", "Great coffee and pastries and others", 4, "Review updated for Cafe Mocha."),
    ("Sushi Express", "Fresh sushiman", 4, "Review updated for Sushi Express."),
])
def test_update_review(restaurant_reviews_with_two_reviews, restaurant, new_review_text, new_rating, expected):
    assert restaurant_reviews_with_two_reviews.update_review(restaurant, new_review_text, new_rating) == expected
    assert restaurant_reviews_with_two_reviews.get_review(restaurant) == {"review_text": new_review_text, "rating": new_rating}

# Parametrization update invalid review
@pytest.mark.parametrize("restaurant, new_review_text, new_rating, expected", [
    ("Cafe Mocha", "Great coffee and pastries", 6, ValueError),
    ("Cafe Mocha", "Great coffee and pastries", 0, ValueError),
])
def test_update_invalid_review(restaurant_reviews_with_two_reviews, restaurant, new_review_text, new_rating, expected):
    with pytest.raises(expected):
        restaurant_reviews_with_two_reviews.update_review(restaurant, new_review_text, new_rating)