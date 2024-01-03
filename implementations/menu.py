class Menu:
    def __init__(self):
        self.reviews = {}

    def add_menu_item(self, restaurant_name, item_name, desription, price):
        if price <= 0:
            raise ValueError("Price must be positive.")
        if restaurant_name not in self.reviews:
            self.reviews[restaurant_name] = {}
        self.reviews[restaurant_name][item_name] = {"desription": desription, "price": price}
        return "Menu item added for {}.".format(restaurant_name)
    
    def get_menu_item(self, restaurant_name):
        if restaurant_name not in self.reviews:
            raise ValueError("No such restaurant exists.")
        return self.reviews[restaurant_name]
    
    def update_menu_item(self, restaurant_name, item_name, new_desription, new_price):
        if restaurant_name not in self.reviews:
            raise ValueError("No such restaurant exists.")
        if item_name not in self.reviews[restaurant_name]:
            raise ValueError("No such item exists.")
        if new_price <= 0:
            raise ValueError("Price must be positive.")
        self.reviews[restaurant_name][item_name] = {"desription": new_desription, "price": new_price}
        return "Menu item updated for {}.".format(restaurant_name)
    
    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name not in self.reviews:
            raise ValueError("No such restaurant exists.")
        if item_name not in self.reviews[restaurant_name]:
            raise ValueError("No such item exists.")
        del self.reviews[restaurant_name][item_name]
        return "Menu item deleted for {}.".format(restaurant_name)