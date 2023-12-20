class RestaurantReviews:
    def __init__(self):
        self.reviews = {}

    def add_review(self, restaurant, review_text, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Invalid Rating. It must be between 1 and 5.")
        self.reviews[restaurant] = {"review_text": review_text, "rating": rating}
        return "Review added for {}.".format(restaurant)

    def get_review(self, restaurant):
        if restaurant not in self.reviews:
            raise ValueError("No such restaurant exists.")
        return self.reviews[restaurant]
    
    def update_review(self, restaurant, new_review_text, new_rating):
        if new_rating < 1 or new_rating > 5:
            raise ValueError("Invalid Rating. It must be between 1 and 5.")
        if restaurant not in self.reviews:
            raise ValueError("No such restaurant exists.")
        self.reviews[restaurant] = {"review_text": new_review_text, "rating": new_rating}
        return "Review updated for {}.".format(restaurant)