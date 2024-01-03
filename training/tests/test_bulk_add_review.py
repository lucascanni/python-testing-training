import pytest

from implementations.restaurant_reviews import RestaurantReviews

# Parametrization valid review
@pytest.mark.parametrize("restaurant, review_text, rating, expected", [
    ("Cafe Mocha", "Great coffee and pastries", 4, "Review added for Cafe Mocha."),
    ("Cafe Sushi", "Great coffee and Sushi", 4, "Review added for Cafe Sushi."),
    ("Cafe Pizza", "Great coffee and Pizza", 4, "Review added for Cafe Pizza."),
    ("Cafe Burger", "Great coffee and Burger", 4, "Review added for Cafe Burger."),
])
def test_add_review(restaurant, review_text, rating, expected):
    reviews = RestaurantReviews()
    result = reviews.add_review(restaurant, review_text, rating)
    assert result == expected
    assert reviews.get_review(restaurant) == {"review_text": review_text, "rating": rating}

# Parametrization invalid review
@pytest.mark.parametrize("restaurant, review_text, rating, expected", [
    ("Cafe Mocha", "Great coffee and pastries", 6, ValueError),
    ("Cafe Mocha", "Great coffee and pastries", 0, ValueError),
])
def test_add_invalid_review(restaurant, review_text, rating, expected):
    reviews = RestaurantReviews()
    with pytest.raises(expected):
        reviews.add_review(restaurant, review_text, rating)