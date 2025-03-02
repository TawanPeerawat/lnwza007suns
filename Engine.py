import pandas as pd

class DealMatcher:
    def __init__(self, users_file, credit_cards_file, restaurants_file, promotions_file):
        self.users = pd.read_csv(users_file)
        self.credit_cards = pd.read_csv(credit_cards_file)
        self.restaurants = pd.read_csv(restaurants_file)
        self.promotions = pd.read_csv(promotions_file)

    def find_best_deals(self, user_id):
        user = self.users[self.users['user_id'] == user_id].iloc[0]
        preferred_cuisine = user['preferred_cuisine']
        preferred_bank = user['preferred_bank']

        # Filter restaurants based on user preference
        matched_restaurants = self.restaurants[self.restaurants['cuisine_type'] == preferred_cuisine]

        # Find promotions that match the user's bank and preferred restaurants
        best_deals = []
        for _, restaurant in matched_restaurants.iterrows():
            promos = self.promotions[(self.promotions['restaurant_id'] == restaurant['restaurant_id']) & 
                                     (self.promotions['bank_name'] == preferred_bank)]
            
            if not promos.empty:
                for _, promo in promos.iterrows():
                    best_deals.append({
                        "Restaurant": restaurant["name"],
                        "Cuisine": restaurant["cuisine_type"],
                        "Promotion": promo["special_offer"],
                        "Discount": f"{promo['discount_percentage']}%",
                        "Valid Until": promo["valid_until"]
                    })

        return best_deals

if __name__ == "__main__":
    matcher = DealMatcher("users.csv", "credit_cards.csv", "restaurants.csv", "promotions.csv")
    user_id = 1  # Example user
    deals = matcher.find_best_deals(user_id)
    print(deals)