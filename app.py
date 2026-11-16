import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(page_title="Beyond the Star Rating", layout="wide")

# Custom CSS for Editorial Dark Mode & Bold Tabs
st.markdown("""
<style>
    /* Dark Theme */
    .stApp { background-color: #111111; color: #FFFFFF; }
    
    /* BOLD Tab Headings */
    button[data-baseweb="tab"] { 
        font-weight: 900 !important; 
        text-transform: uppercase; 
        font-size: 1.1rem !important; 
        color: #FFFFFF !important; 
    }
    button[data-baseweb="tab"] p { font-weight: 900 !important; }
    
    /* Typography */
    h1, h2, h3, h4 { font-family: 'Helvetica Neue', sans-serif; font-weight: 800; }
    h1 { font-size: 5rem; line-height: 1.1; margin-bottom: 10px; text-align: center; }
    h3 { font-size: 2rem; color: #E63946; margin-bottom: 15px; }
    p, li { color: #CCCCCC; font-size: 1.3rem; line-height: 1.7; }
    .accent { color: #E63946; font-weight: bold; }
    
    /* Layout elements */
    .hero-sub { text-align: center; color: #A0A0A0; font-size: 1.8rem; margin-bottom: 40px; }
    .card { background-color: #1E1E1E; padding: 25px; border-radius: 8px; height: 100%; border: 1px solid #333; margin-bottom: 20px; }
    .highlight-box { background-color: #1E1E1E; padding: 40px; border-left: 5px solid #E63946; margin: 30px 0; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<h1>BEYOND THE STAR RATING</h1>", unsafe_allow_html=True)
st.markdown("<div class='hero-sub'>How to choose the right Kenyan waterfront resort using data, not guesswork.</div>", unsafe_allow_html=True)

# --- TABS ---
tab_intro, tab_loc, tab_rep, tab_price, tab_pop, tab_dash = st.tabs([
    "INTRO", "DESTINATION", "REPUTATION", "PRICING", "POPULARITY", "LIVE DASHBOARD"
])

# TAB 1: INTRODUCTION
with tab_intro:
    st.markdown("<h2>The Kenya Waterfront Paradox</h2>", unsafe_allow_html=True)
    st.markdown("""
    Kenya is a country defined by its water. From the white sands of the Indian Ocean to the shores of Lake Victoria and the quiet rivers of the Masai Mara, waterfront resorts offer some of the most unforgettable stays in the world.
    <br><br>
    But finding the *right* one has become a guessing game. With <span class='accent'>168 waterfront resorts</span> spread across 9 counties, the options are vast—and the information available is often one-sided.
    """, unsafe_allow_html=True)

    st.markdown("<h2>The Illusion of the 4.4 Star Rating</h2>", unsafe_allow_html=True)
    st.markdown("""
    When you see a **4.4** on Google, what does it actually mean? 
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #E63946;'>
            <h4>What a Google Rating Hides</h4>
            <p>❌ Whether a 4.4 is based on 3 reviews or 3,000.</p>
            <p>❌ If the nightly price is standard for the area or a massive markup.</p>
            <p>❌ How the resort compares to others in the same region.</p>
            <p>❌ The overall landscape of the area you want to visit.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #4CAF50;'>
            <h4>What This Dashboard Reveals</h4>
            <p>✅ <strong>Hidden Gems vs. Tourist Giants:</strong> See rating vs. review volume.</p>
            <p>✅ <strong>Pricing Context:</strong> Compare real prices to the area average.</p>
            <p>✅ <strong>Regional Rankings:</strong> Instantly see the top-rated resorts in a specific area.</p>
            <p>✅ <strong>The Big Picture:</strong> Explore the coast, lakes, and rivers seamlessly.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><h2>The Full Picture</h2>", unsafe_allow_html=True)
    st.markdown("""
    This project cuts through the noise. We break the data down into four clear areas: <strong>Location, Reputation, Pricing, and Popularity</strong>. 
    <br><br>
    Whether you're booking a holiday, building a client itinerary, or checking out the competition, this dashboard gives you the full landscape. Filter by region, spot overpriced areas, and find hidden gems before anyone else does.
    """, unsafe_allow_html=True)

# TAB 2: DESTINATION
with tab_loc:
    st.markdown("<h2>Explore the Waterways</h2>", unsafe_allow_html=True)
    st.markdown("""
    When most people think of a Kenyan waterfront resort, they picture the Indian Ocean. But Kenya's waterways offer three completely different travel experiences depending on what you are looking for.
    <br><br>
    Our dataset spans <span class='accent'>9 counties</span> across the country. Here is what you need to know before you choose your destination:
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #4CAF50;'>
            <h4>🌊 The Indian Ocean Coast</h4>
            <p><strong>The Vibe:</strong> White sand, coral reefs, and warm water. Perfect for snorkeling, dhow sailing, and experiencing Swahili culture.</p>
            <p><strong>Key Areas:</strong> Diani, Mombasa, Watamu, Lamu.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #2196F3;'>
            <h4>🦩 Inland Lakes</h4>
            <p><strong>The Vibe:</strong> Cooler climates, freshwater, and incredible birdlife. Perfect for boat safaris, spotting hippos, and peaceful sunsets.</p>
            <p><strong>Key Areas:</strong> Naivasha, Nakuru, Elementaita, Kisumu (Lake Victoria).</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #FF9800;'>
            <h4>🦁 The Safari Rivers</h4>
            <p><strong>The Vibe:</strong> Rugged, remote, and wild. Perfect for luxury tented camps where you can watch elephants and big cats come down to drink.</p>
            <p><strong>Key Areas:</strong> Narok (Masai Mara), Kajiado, Isiolo.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><h2>The Geospatial Landscape</h2>", unsafe_allow_html=True)
    st.markdown("""
    Below is the map of all 168 resorts in our dataset. Notice how they cluster along the eastern coastline and the Great Rift Valley. 
    <br><br>
    <em>Note: Kajiado and Isiolo are included because they host riverside resorts along the Athi and Ewaso Nyiro rivers, proving that a 'waterfront' stay doesn't always mean the ocean.</em>
    """, unsafe_allow_html=True)
    st.image("images/map.png", use_container_width=True)

# TAB 3: REPUTATION
with tab_rep:
    st.markdown("<h2>The Illusion of the Perfect Score</h2>", unsafe_allow_html=True)
    st.markdown("""
    A 5-star rating from 2 people means absolutely nothing. In the hotel business, volume is everything. A 4.5 rating from 2,000 guests is worth far more than a 4.9 from a handful of friends and family.
    <br><br>
    Before you trust a rating, you have to ask three questions:
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #E63946;'>
            <h4>1. How many people?</h4>
            <p>If a resort only has 10 reviews, one bad stay can ruin their score. You need a large number of reviews to find the true average experience.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #FF9800;'>
            <h4>2. When was it reviewed?</h4>
            <p>A resort might have a 4.8 from 2019, but what if it changed owners last year? High review numbers help balance out old, outdated opinions.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #4CAF50;'>
            <h4>3. Is the sample size large enough?</h4>
            <p>Sometimes, a sudden burst of 5-star reviews is suspicious. High review numbers mean the resort has survived the test of time and real, paying guests.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><h2>Our Filter: The 50-Review Rule</h2>", unsafe_allow_html=True)
    st.markdown("""
    To protect you from false positives and statistical noise, we applied a strict rule to this analysis. <strong>Any resort with fewer than 50 reviews was excluded.</strong>
    <br><br>
    What you are looking at below is the <strong>Top 20 highest-rated resorts</strong> in Kenya that have passed this threshold. The bars show their Google Rating, and the numbers on the right show exactly how many people left that score.
    """, unsafe_allow_html=True)
    st.image("images/bar_chart.png", use_container_width=True)

# TAB 4: PRICING
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #E63946;'>
            <h4>The "Mara Premium"</h4>
            <p>Narok (Masai Mara) is the most expensive region in the dataset by a wide margin, averaging 87,125 KES per night.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #FF9800;'>
            <h4>The Price Spread</h4>
            <p>Even within the same county, prices vary wildly. The red tick on the chart shows the lowest price, which is often much lower than the average.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #4CAF50;'>
            <h4>The Data Gap</h4>
            <p>We found live prices for 96 resorts. The other 72 didn't list their prices on Google Hotels. These are often smaller guesthouses or self-catering villas.</p>
        </div>
        """, unsafe_allow_html=True)

# TAB 5: POPULARITY
with tab_pop:
    st.markdown("<h2>Hidden Gems vs. Tourist Giants</h2>", unsafe_allow_html=True)
    st.markdown("""
    We all want a place that is highly rated. But do you want a place that is packed with thousands of tourists, or do you want a quiet, hidden retreat? 
    <br><br>
    This chart helps you find the <span class='accent'>sweet spot</span>. It maps every resort by its rating (how high it is) and its popularity (how far right it is). You can instantly see who is a heavyweight champion, and who is an undiscovered gem.
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #4CAF50; margin-bottom: 20px;'>
            <h4>💎 The Hidden Gems (Top Left)</h4>
            <p>High ratings, low review counts. These are places doing something really special, but haven't been discovered by the masses. <em>Check the review count before you trust a high rating.</em></p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='card' style='border-top: 4px solid #E63946;'>
            <h4>⚠️ The Underdogs (Bottom Left)</h4>
            <p>Low ratings, low review counts. These are often new places that are still finding their feet, or older places that have lost their touch.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card' style='border-top: 4px solid #FF9800; margin-bottom: 20px;'>
            <h4>👑 The Tourist Giants (Top Right)</h4>
            <p>High ratings, thousands of reviews. The heavyweights. They are proven by thousands of guests, though they might be busy and pricey.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='card' style='border-top: 4px solid #757575;'>
            <h4>🏭 The Crowd Pleasers (Bottom Right)</h4>
            <p>Lower ratings, thousands of reviews. These are massive resorts that handle huge crowds, but the quality might have slipped.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><h2>The Popularity Landscape</h2>", unsafe_allow_html=True)
    st.image("images/scatterplot.png", use_container_width=True)

# TAB 6: LIVE DASHBOARD
with tab_dash:
    st.markdown("<h2>How to Use This Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("""
    This dashboard is designed to answer your specific travel questions. Here is how to navigate it:
    <br><br>
    <strong>1. Pick Your Location:</strong> Click on a county on the map (like Kwale or Nakuru) to filter the entire dashboard to that specific area.
    <br>
    <strong>2. Check the Rankings:</strong> Look at the bar chart to see the highest-rated resorts in your chosen area. Use the slider to see the Top 5, 10, or 20.
    <br>
    <strong>3. Compare Prices:</strong> Look at the price chart to see the average cost in that county. Hover over the bars to see the minimum price.
    <br>
    <strong>4. Spot the Gems:</strong> Look at the scatterplot to see if the top-rated resorts are crowded tourist hubs or quiet hidden gems.
    """, unsafe_allow_html=True)
    
    st.markdown("<h2>The Interactive Dashboard</h2>", unsafe_allow_html=True)
    # Forcing desktop view and fit-to-width to prevent the squished mobile view
    tableau_url = "https://public.tableau.com/views/Kenya_Waterfront_Resorts_Dashboard/Dashboard?:showVizHome=no&:embed=true&:device=desktop&:fit=yes"
    tableau_html = f"""
    <iframe src="{tableau_url}" 
    width="100%" 
    height="950" 
    style="border: none;">
    </iframe>
    """
    components.html(tableau_html, height=970, scrolling=False)

    st.markdown("<br><h2>Key Insights Discovered</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='highlight-box'>
        <h4>1. The "Mara Premium" is Real</h4>
        <p>Narok (Masai Mara) averages 87,125 KES, roughly three to four times the coastal averages. You are paying for the exclusivity of the wildlife.</p>
    </div>
    
    <div class='highlight-box'>
        <h4>2. Lamu stands out</h4>
        <p>Lamu has the highest average rating (4.67) with a mid-range average price (22,050 KES). Kwale (Diani) averages 20,014 KES, similar to Nakuru.</p>
    </div>

    <div class='highlight-box'>
        <h4>3. Hidden Gems are Everywhere (but check the reviews)</h4>
        <p>While we found many highly-rated resorts with low reviews, always check the review count before you trust a high rating. Places with fewer than 10 reviews might not be statistically reliable.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Methodology & Tools</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
            <h4>Data Sourcing</h4>
            <p>Collected 168 resorts using the Google Places API. Live pricing was scraped using Apify (Google Hotels Scraper), scraped in batches because of free-tier limits.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
            <h4>Spatial Analysis</h4>
            <p>Used Python and GeoPandas to perform a spatial join, assigning each resort to its official Kenyan county, correcting the few that did not match.</p>
        </div>
        """, unsafe_allow_html=True)