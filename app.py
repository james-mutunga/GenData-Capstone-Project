import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(page_title="Beyond the Star Rating", layout="wide")

DASHBOARD_PAGE = (
    "https://public.tableau.com/app/profile/james.mutunga/"
    "viz/Kenya_Waterfront_Resorts_Dashboard/Dashboard"
)
DASHBOARD_EMBED = (
    "https://public.tableau.com/views/"
    "Kenya_Waterfront_Resorts_Dashboard/Dashboard"
    "?:showVizHome=no&:embed=true&:device=desktop&:fit=yes"
)

# Custom CSS for Editorial Dark Mode & Bold Tabs
st.markdown(
    """
    <style>
        .stApp {
            background-color: #111111;
            color: #FFFFFF;
        }

        button[data-baseweb="tab"] {
            font-weight: 900 !important;
            text-transform: uppercase;
            font-size: 1.1rem !important;
            color: #FFFFFF !important;
        }

        button[data-baseweb="tab"] p {
            font-weight: 900 !important;
        }

        h1, h2, h3, h4 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 800;
        }

        h1 {
            font-size: 5rem;
            line-height: 1.1;
            margin-bottom: 10px;
            text-align: center;
        }

        h3 {
            font-size: 2rem;
            color: #E63946;
            margin-bottom: 15px;
        }

        p, li {
            color: #CCCCCC;
            font-size: 1.3rem;
            line-height: 1.7;
        }

        .accent {
            color: #E63946;
            font-weight: bold;
        }

        .hero-sub {
            text-align: center;
            color: #A0A0A0;
            font-size: 1.8rem;
            margin-bottom: 40px;
        }

        .card {
            background-color: #1E1E1E;
            padding: 25px;
            border-radius: 8px;
            height: 100%;
            border: 1px solid #333;
            margin-bottom: 20px;
        }

        .highlight-box {
            background-color: #1E1E1E;
            padding: 40px;
            border-left: 5px solid #E63946;
            margin: 30px 0;
            border-radius: 5px;
        }

        .question-box {
            background-color: #1E1E1E;
            padding: 15px 30px;
            border-left: 5px solid #E63946;
            margin: 10px 0 30px 0;
            border-radius: 5px;
        }

        .question-box p {
            margin: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HERO SECTION ---
st.markdown("<h1>BEYOND THE STAR RATING</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-sub'>"
    "How to choose the right Kenyan waterfront resort using data, not guesswork."
    "</div>",
    unsafe_allow_html=True,
)

# --- TABS ---
tab_intro, tab_loc, tab_rep, tab_price, tab_pop, tab_dash = st.tabs(
    ["INTRO", "DESTINATION", "REPUTATION", "PRICING", "POPULARITY", "LIVE DASHBOARD"]
)

# TAB 1: INTRODUCTION
with tab_intro:
    st.markdown("<h2>The Kenya Waterfront Paradox</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        Kenya is a country defined by its water. From the white sands of the Indian
        Ocean to the shores of Lake Victoria and the quiet rivers of the Masai Mara,
        waterfront resorts offer some of the most unforgettable stays in the world.
        <br><br>
        But finding the <em>right</em> one can be difficult. With
        <span class='accent'>168 waterfront resorts</span> spread across 9 counties,
        the options are vast—and a single rating rarely tells the whole story.
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='highlight-box'>
            <h3>The Project in One Minute</h3>
            <p><span class='accent'>The Problem:</span> Travelers may struggle to
            compare resorts because a single Google rating does not show the full
            picture. It does not reveal how ratings relate to review counts, how
            resorts compare within a county, or what collected prices were returned
            for the dates searched.</p>
            <p><span class='accent'>The Audience:</span> Travelers (business and
            leisure) and travel agents.</p>
            <p><span class='accent'>The Decision:</span> Which waterfront resorts
            should a traveler shortlist in a chosen region of Kenya?</p>
            <p><span class='accent'>The Question:</span> How can travelers filter
            resorts by county and compare their ratings, collected prices, and
            review counts in one place?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h2>The Illusion of the 4.4 Star Rating</h2>", unsafe_allow_html=True)
    st.markdown(
        "When you see a **4.4** on Google, what does it actually tell you?",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #E63946;'>
                <h4>What a Google Rating Hides</h4>
                <p>❌ Whether a 4.4 is based on 3 reviews or 3,000.</p>
                <p>❌ What price was returned for the dates searched.</p>
                <p>❌ How the resort compares with others in the same county.</p>
                <p>❌ How resorts are distributed across the country's waterways.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #4CAF50;'>
                <h4>What This Dashboard Reveals</h4>
                <p>✅ <strong>Ratings & Review Counts:</strong> Compare ratings
                alongside the number of reviews.</p>
                <p>✅ <strong>Pricing Context:</strong> Compare collected prices
                across counties.</p>
                <p>✅ <strong>Regional Rankings:</strong> Explore the highest-rated
                resorts in a selected county.</p>
                <p>✅ <strong>The Big Picture:</strong> Explore the coast, lakes,
                and rivers in one dataset.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><h2>Who is this for?</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        * **For Travelers:** Compare resorts by destination, rating, review count,
          and the prices returned for the searched dates.
        * **For Travel Agents:** Shortlist resorts in a client's preferred county
          using the available rating and pricing information.
        * **For Resort Operators:** Compare a resort's rating, review count, and
          collected price with other resorts in the same county.
        """,
        unsafe_allow_html=True,
    )

# TAB 2: DESTINATION
with tab_loc:
    st.markdown("<h2>Explore the Waterways</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='question-box'><p><span class='accent'>The Question:</span>
        Where are the resorts located, and what is the overall landscape?</p></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        When most people think of a Kenyan waterfront resort, they picture the
        Indian Ocean. But Kenya's waterways offer different travel experiences.
        <br><br>
        Our dataset spans <span class='accent'>9 counties</span> across the country.
        Here is what you need to know before choosing a destination:
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #4CAF50;'>
                <h4>🌊 The Indian Ocean Coast</h4>
                <p><strong>The Vibe:</strong> White sand, coral reefs, and warm
                water. Activities can include snorkeling, dhow sailing, and
                experiencing Swahili culture.</p>
                <p><strong>Key Areas:</strong> Diani, Mombasa, Watamu, Lamu.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #2196F3;'>
                <h4>🦩 Inland Lakes</h4>
                <p><strong>The Vibe:</strong> Freshwater landscapes, birdlife,
                and opportunities for boat trips and peaceful stays.</p>
                <p><strong>Key Areas:</strong> Naivasha, Nakuru, Elementaita,
                Kisumu (Lake Victoria).</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #FF9800;'>
                <h4>🦁 The Safari Rivers</h4>
                <p><strong>The Vibe:</strong> Riverside lodges and camps in
                wildlife areas, offering a different kind of waterfront stay.</p>
                <p><strong>Key Areas:</strong> Narok (Masai Mara), Kajiado,
                Isiolo.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><h2>The Geospatial Landscape</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        Below is the map of all 168 resorts in our dataset. Notice how they
        cluster along the eastern coastline and the Great Rift Valley.
        <br><br>
        <em>Note: Kajiado and Isiolo are included because the dataset contains
        riverside resorts along the Athi and Ewaso Nyiro rivers.</em>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/map.png", use_container_width=True)

# TAB 3: REPUTATION
with tab_rep:
    st.markdown("<h2>The Illusion of the Perfect Score</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='question-box'><p><span class='accent'>The Question:</span>
        Which resorts have the highest ratings in the selected area?</p></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        A rating should be considered alongside its review count. A high score
        based on a small number of reviews has less supporting review volume than
        the same score based on thousands of reviews. Review count adds context;
        it does not prove that one resort is objectively better.
        <br><br>
        Before relying on a rating, consider three questions:
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #E63946;'>
                <h4>1. How many reviews?</h4>
                <p>A resort with relatively few reviews has a smaller body of
                public feedback behind its score. Review count helps put the
                rating into context.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #FF9800;'>
                <h4>2. Compared with what?</h4>
                <p>A rating becomes more useful when compared with ratings from
                other resorts in the same county.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #4CAF50;'>
                <h4>3. Is it a tie?</h4>
                <p>When resorts share the same rating, review count can provide
                an additional way to order them.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><h2>Our Filter: The 50-Review Rule</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        To avoid rankings based on only a few reviews, the chart includes resorts
        with <strong>at least 50 reviews</strong>. Review count is used to break
        rating ties.
        <br><br>
        The chart shows the Top 20 highest-rated resorts that pass this threshold.
        The bars show their Google ratings, and the labels show their review counts.
        """,
        unsafe_allow_html=True,
    )
    st.image("images/bar_chart.png", use_container_width=True)

# TAB 4: PRICING
with tab_price:
    st.markdown("<h2>Decoding the Price Tag</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='question-box'><p><span class='accent'>The Question:</span>
        What are the minimum and average collected prices per night in each
        county?</p></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        Resort prices vary by destination and by the dates searched. The figures
        in this project are collected price snapshots, not guaranteed current
        rates or a continuous live price feed.
        <br><br>
        Here is some context before looking at the numbers:
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #E63946;'>
                <h4>The Mara Price Difference</h4>
                <p>Narok (Masai Mara) has the highest average collected price
                in this dataset, at 87,125 KES per night. This is based only
                on resorts with a returned price.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #FF9800;'>
                <h4>The Price Spread</h4>
                <p>Prices vary within counties too. The red marker on the chart
                shows the minimum collected price, which may be lower than the
                county average.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #4CAF50;'>
                <h4>The Data Gap</h4>
                <p>A price was returned for 96 of the 168 resorts (57%) for
                the dates searched. No price was returned for the remaining
                72 resorts.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><h2>Regional Averages</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        The chart below compares the minimum and average collected price per
        night, in Kenyan Shillings (KES), for counties with returned prices.
        County averages use only resorts with a returned price.
        <br><br>
        Narok (Masai Mara) has the highest average in this dataset at
        <span class='accent'>87,125 KES</span>. This is a comparison of the
        collected sample, not a guarantee of current market prices.
        """,
        unsafe_allow_html=True,
    )

    st.image("images/price_chart.png", use_container_width=True)
    st.info("Note: Isiolo and Kajiado have no returned prices in this dataset.")

# TAB 5: POPULARITY
with tab_pop:
    st.markdown("<h2>Hidden Gems vs. Tourist Giants</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='question-box'><p><span class='accent'>The Question:</span>
        Which resorts have high ratings with relatively few reviews, and which
        have high ratings alongside many reviews?</p></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        Review count can be used as a rough proxy for the volume of public
        feedback a resort has received. It is not a direct measure of visitor
        numbers, occupancy, or how crowded a property is.
        <br><br>
        This chart maps each resort by its Google rating (vertical axis) and
        review count (horizontal axis). It helps identify different combinations
        of rating and review volume.
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #4CAF50; margin-bottom: 20px;'>
                <h4>💎 Highly Rated, Fewer Reviews</h4>
                <p>These resorts have high ratings but fewer reviews. Their
                scores may be based on a smaller body of public feedback, so
                check the review count and read recent reviews.</p>
            </div>
            <div class='card' style='border-top: 4px solid #E63946;'>
                <h4>⚠️ Lower Rated, Fewer Reviews</h4>
                <p>These resorts have lower ratings and fewer reviews. The
                limited review volume makes it useful to examine individual
                feedback before drawing conclusions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card' style='border-top: 4px solid #FF9800; margin-bottom: 20px;'>
                <h4>👑 Highly Rated, Many Reviews</h4>
                <p>These resorts combine high ratings with a larger volume of
                public feedback.</p>
            </div>
            <div class='card' style='border-top: 4px solid #757575;'>
                <h4>🏭 Lower Rated, Many Reviews</h4>
                <p>These resorts have lower ratings alongside a larger volume
                of public feedback. Reading guest comments can help explain
                the scores.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><h2>The Popularity Landscape</h2>", unsafe_allow_html=True)
    st.image("images/scatterplot.png", use_container_width=True)

# TAB 6: LIVE DASHBOARD
with tab_dash:
    st.markdown("<h2>Try It Yourself</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        Everything you have just read comes together in the interactive
        dashboard. Select a county on the map to filter the views, use the
        Top N control to compare the highest-rated resorts, and hover over
        charts to explore the available prices and review counts.
        """,
        unsafe_allow_html=True,
    )

    components.iframe(DASHBOARD_EMBED, height=950, scrolling=True)
    st.markdown(f"[Open the dashboard in its own tab ↗]({DASHBOARD_PAGE})")

    st.markdown(
        """
        <div class='highlight-box'>
            <h3>The Big Idea</h3>
            <p>A single Google rating does not tell the whole story. By combining
            county-level exploration, ratings with review counts, collected
            prices, and review volume, travelers get a broader basis for
            comparing where to stay.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h2>Methodology & Limitations</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='card'>
                <h4>Tools & Methodology</h4>
                <p><strong>Google Places API:</strong> Collected Google ratings
                and review counts for 168 resorts.</p>
                <p><strong>Python & Pandas:</strong> Cleaned and prepared the
                dataset and integrated collected pricing.</p>
                <p><strong>GeoPandas:</strong> Assigned resort coordinates to
                Kenyan county boundaries, with manual corrections where needed.</p>
                <p><strong>Apify:</strong> Collected price information for the
                dates searched.</p>
                <p><strong>Tableau & Streamlit:</strong> Built the interactive
                dashboard and this storytelling app.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='card'>
                <h4>Limitations</h4>
                <p>⚠️ Google Places data does not provide complete pricing or
                amenity information.</p>
                <p>⚠️ A price was returned for 96 resorts (57%) for the dates
                searched. No price was returned for the other 72.</p>
                <p>⚠️ Review count is a proxy for public feedback volume, not
                actual visitor numbers or occupancy.</p>
                <p>⚠️ Review-theme labels are based on keyword matching and
                VADER sentiment; they are indicative, not full review summaries.</p>
                <p>⚠️ The analysis describes patterns in the collected data;
                it does not establish causation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='card'>
                <h4>What's Next</h4>
                <p>🚀 Collect prices across more dates and from additional
                reliable sources to improve coverage.</p>
                <p>🚀 Develop a richer review-analysis approach to better
                summarize why guests praise or criticize each resort.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
