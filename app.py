import streamlit as st

# Page Setup
st.set_page_config(page_title="Kenya Waterfront Resorts", layout="wide")

# Title & Introduction
st.title("Beyond the Star Rating: Analyzing Guest Satisfaction in Kenya Waterfront Resorts")
st.markdown("""
**The Problem:** A single Google rating doesn't tell the whole story. Travelers struggle to know the actual prices, popularity, or overall landscape of a region without opening dozens of tabs.
""")

# The 4 Dimensions
st.header("1. Destination (The Where)")
st.write("Explore resorts by clicking on a county map.")
st.image("images/map.png", caption="Interactive Regional Resort Map")

st.header("2. Reputation (The How Good)")
st.write("Top N ranking of the highest-rated resorts by review volume.")
st.image("images/bar_chart.png", caption="Guest Favorites: High Ratings & High Volume")

st.header("3. Pricing & Value (The How Much)")
st.write("Minimum and average price per night (KES) by county.")
st.image("images/price_chart.png", caption="Minimum & Average Prices Per Region")

st.header("4. Popularity (Hidden Gems vs. Tourist Giants)")
st.write("Mapping rating against review count to find hidden gems.")
st.image("images/scatterplot.png", caption="Resort Popularity: Hidden Gems vs. Tourist Giants")

# Key Insight (The "Aha!" Moment)
st.header("The 'Aha!' Discovery")
st.info("A single Google rating hides the real story. Narok (Masai Mara) has the highest average price by far, while the coast and lakes offer more affordable options.")

# Tableau Dashboard Embed
st.header("Interactive Tableau Dashboard")
tableau_url = "https://public.tableau.com/views/Kenya_Waterfront_Resorts_Dashboard/Dashboard?:showVizHome=no&:embed=true"
st.components.v1.iframe(tableau_url, height=800)