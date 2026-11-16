# Kenya Waterfront Resorts: What Matters to Guests?

## 🔗 Live Dashboard
[Click here to view the interactive Tableau Dashboard](https://public.tableau.com/app/profile/james.mutunga/viz/Kenya_Waterfront_Resorts_Dashboard/Dashboard?publish=yes)

## 📌 Project Overview
Travelers choosing a waterfront resort in Kenya usually see only one Google rating, which doesn't show the full picture. This project analyzes **168 waterfront resorts** across the Kenyan coast, inland lakes, and safari rivers to help travelers find the perfect stay.

The central finding is that a single Google rating hides the real story. By combining geospatial mapping with dynamic ranking, real pricing, and popularity metrics, travelers can instantly filter resorts by their chosen county and see the highest-rated options in that exact area.

## 💡 Key Insights
*   **Interactive Exploration:** The Tableau dashboard allows users to click a specific Kenyan county on the map to instantly filter all the data.
*   **Top N Ranking:** Users can adjust a slider to see the Top 5, 10, or 20 highest-rated resorts in their selected region. (Note: To avoid ratings based on only a few reviews, the Top N chart only includes resorts with at least 50 reviews).
*   **Pricing Context:** Users can view the minimum and average price per night (in KES) per region. Hovering over the bars reveals the minimum prices. Averages use only resorts with a listed price.
*   **Hidden Gems vs. Tourist Giants:** A scatterplot reveals the relationship between a resort's rating and its review count, helping users find hidden gems or highly popular destinations.

## 🛠️ Tools & Technologies
*   **Google Places API:** Used to collect real-world data for 168 waterfront resorts, including guest ratings and review counts.
*   **Python (Pandas):** Used for initial data cleaning, formatting, and merging pricing data.
*   **Python (GeoPandas):** Used to perform a spatial join, assigning each resort's latitude and longitude to its official Kenyan county, correcting the few that did not match.
*   **Apify (Google Hotels Scraper):** Used to fetch live pricing data. We successfully scraped 96 real prices out of 168 resorts (57%), with the rest left blank as they do not list prices on Google Hotels.
*   **Tableau:** Used to build the final interactive dashboard with 4 distinct charts.

## 📊 The 4 Dimensions of the Dashboard
The Tableau dashboard is structured around four key questions:
1.  **Destination:** Where are these resorts located? (Interactive Map)
2.  **Reputation:** Which resorts are the highest-rated? (Top N Bar Chart)
3.  **Pricing & Value:** What is the minimum and average cost per night? (Price Chart)
4.  **Popularity:** Are they hidden gems or tourist giants? (Scatterplot)

## ▶️ How to Run
1. Install the required libraries: `pip install -r requirements.txt`
2. To skip the Google and Apify calls (Sections B, C, D, K), load the dataset directly:
   `df = pd.read_csv("Data/kenya_resorts_clean.csv")`
3. To view the dashboard, open the Tableau file and explore the map.

## 📂 Repository Structure
*   `Data/` - Contains the final master CSV dataset (`kenya_resorts_clean.csv`) and the Kenyan county shapefiles.
*   `resort_analysis.ipynb` - The Jupyter Notebook containing the Python code for API data collection, cleaning, GeoPandas spatial joins, and pricing scraping.
*   `project_template.md` - The narrative summary of the project.
*   `README.md` - This file.
*   `requirements.txt` - List of required Python packages.

## ⚠️ Limitations
*   Google Places API does not provide exact real-time pricing or complete amenity data. 
*   While we scraped 96 live prices (57% of the dataset), some smaller guesthouses do not list their prices on Google Hotels, resulting in empty values for 72 resorts. Tableau handles these nulls automatically.
*   **County Coverage:** The dataset includes 3 resorts in Kajiado and Isiolo. These are located along the Athi and Ewaso Nyiro rivers. They are kept in the dataset to ensure comprehensive waterfront coverage.
*   The analysis shows correlation between location and rating, but does not prove causation for why guests rate the way they do.

## 🚀 Future Improvements
*   Integrate a more robust hotel scraping API to pull real-time pricing for 100% of the resorts.
*   Upgrade the NLP text analysis to summarize the actual review text, telling the user exactly *why* a hotel is highly rated.