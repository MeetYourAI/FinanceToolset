### Custom Budget Suggestions
python
import pandas as pd

# Sample spending data
data = pd.DataFrame({
    'Category': ['Groceries', 'Dining', 'Transport', 'Entertainment'],
    'Amount': [200, 150, 100, 120]
})

# User's balance
balance = 1000

def recommend_budget(category, balance):
    category_avg = data[data['Category'] == category]['Amount'].mean()
    budget = balance * 0.2 if pd.isna(category_avg) else category_avg
    return min(budget, balance * 0.2)

category = 'Groceries'
budget = recommend_budget(category, balance)
print(f"Recommended budget for {category}: {budget}")


### Purchase Decision Help
python
def purchase_advice(price, balance):
    if price > balance * 0.1:
        return "It might be better to wait for a better financial period."
    else:
        return "You can make this purchase without significantly impacting your balance."

price = 50
advice = purchase_advice(price, balance)
print(f"Purchase advice: {advice}")


### Timely Spending Notifications
python
def spending_alert(current_spent, category, limit):
    if current_spent > limit:
        return f"Alert: You've exceeded your {category} budget!"
    else:
        return f"You're within your {category} budget."

current_spent = 180
category_limit = 150
alert = spending_alert(current_spent, 'Dining', category_limit)
print(alert)


### Merchant Reviews and Ratings
python
merchant_reviews = {
    'Restaurant A': 4.5,
    'Restaurant B': 3.8
}

def get_merchant_rating(merchant):
    return merchant_reviews.get(merchant, "No rating available")

merchant = 'Restaurant A'
rating = get_merchant_rating(merchant)
print(f"Rating for {merchant}: {rating}")
