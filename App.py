import streamlit as st
import pandas as pd
from Engine import DealMatcher

# Load data
matcher = DealMatcher("users.csv", "credit_cards.csv", "restaurants.csv", "promotions.csv")

# Streamlit App UI
st.title("Credit Card & Restaurant Deal Matcher")

# User Selection
users = pd.read_csv("users.csv")
user_list = users["name"].tolist()
selected_user = st.selectbox("Select User", user_list)

if selected_user:
    user_id = users[users["name"] == selected_user]["user_id"].values[0]

    # Find best deals
    deals = matcher.find_best_deals(user_id)

    if deals:
        st.subheader("Best Matched Deals")
        for deal in deals:
            st.write(f"**Restaurant:** {deal['Restaurant']}")
            st.write(f"**Cuisine:** {deal['Cuisine']}")
            st.write(f"**Promotion:** {deal['Promotion']}")
            st.write(f"**Discount:** {deal['Discount']}")
            st.write(f"**Valid Until:** {deal['Valid Until']}")
            st.markdown("---")
    else:
        st.write("No matching deals found.")