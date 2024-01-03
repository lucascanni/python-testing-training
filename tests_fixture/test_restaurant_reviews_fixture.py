import pytest
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

def test_get_fixture(restaurant_reviews_with_two_reviews):
    assert restaurant_reviews_with_two_reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee and pastries", "rating": 4}
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") == {"review_text": "Fresh sushi", "rating": 4}
    assert restaurant_reviews_with_two_reviews.get_review("Cafe Mocha") != {"review_text": "Fresh sushi", "rating": 4}
    assert restaurant_reviews_with_two_reviews.get_review("Sushi Express") != {"review_text": "Great coffee and pastries", "rating": 4}