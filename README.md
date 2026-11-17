# Kenya Waterfront Resorts: What Matters to Guests?

## Live Dashboards
- **[Interactive Tableau Dashboard](https://public.tableau.com/app/profile/james.mutunga/viz/Kenya_Waterfront_Resorts_Dashboard/Dashboard)** — explore the data.
- **[Streamlit Storytelling App](https://gendata-capstone-project-pwhzhknvfsdeitztyethbe.streamlit.app/)**

## Project Overview
Travelers choosing a waterfront resort in Kenya usually see a single Google rating, which does not show the full picture. This project analyzes **168 waterfront resorts** across the Kenyan coast, inland lakes, and safari rivers to help travelers compare destinations.

A single rating can hide important differences. By combining geospatial mapping, rating-based rankings, collected pricing, and review-count data, the project lets travelers filter resorts by county and explore the highest-rated options in that area.

## Key Insights
- **Interactive exploration:** Select a Kenyan county on the map to filter the dashboard.
- **Top N ranking:** Choose to view the Top 5, 10, or 20 highest-rated resorts in the selected county. To reduce the influence of ratings based on very few reviews, this chart includes only resorts with at least 50 reviews.
- **Pricing context:** Compare the minimum and average collected price per night (KES) by county. County averages use only resorts with a returned price.
- **Hidden gems vs. tourist giants:** Explore the relationship between a resort's Google rating and its review count. This helps distinguish highly rated resorts with relatively few reviews from highly rated, widely reviewed resorts.

## Tools & Technologies
- **Google Places API:** Collected Google ratings and review counts for 168 waterfront resorts.
- **Python (Pandas):** Used for data cleaning, formatting, deduplication, and merging pricing data.
- **Python (GeoPandas):** Performed a spatial join to assign resort coordinates to Kenyan county boundaries, with manual corrections where needed.
- **Apify (Google Hotels Scraper):** Collected pricing information for 96 of the 168 resorts (57%) for the dates searched. No price was returned for the remaining 72 resorts. These collected prices are a snapshot and may change; they are not a continuous real-time feed.
- **Python (VADER and keyword-based aspect analysis):** Examined review text for positive mentions of themes such as views, service, food, rooms, and amenities, then assigned each resort its most frequently mentioned positive theme. Resorts without a matching positive mention are labelled “General”.
- **Tableau:** Built the interactive dashboard with four analytical views.
- **Streamlit:** Built the storytelling app, which presents the findings and embeds the Tableau dashboard.

## The Four Dimensions of the Dashboard
The analysis is organized around four questions:

1. **Destination:** Where are the resorts located? — interactive county map.
2. **Reputation:** Which resorts have the highest ratings? — Top N bar chart.
3. **Pricing & Value:** What are the minimum and average collected prices per night? — price chart.
4. **Popularity:** How do ratings relate to review counts? — scatterplot.

## Repository Structure
- `Data/` — contains the final master dataset (`kenya_resorts_clean.csv`) and the Kenyan county shapefiles.
- `images/` — contains the chart images displayed in the Streamlit app.
- `resort_analysis.ipynb` — notebook for API data collection, cleaning, geospatial analysis, pricing collection, and review-theme analysis.
- `app.py` — Streamlit storytelling application.
- `project_template.md` — project narrative and business value summary.
- `README.md` — project documentation.
- `requirements.txt` — required Python packages.

## Limitations
- Google Places data does not provide complete pricing or amenity information.
- Pricing was returned for 96 resorts (57%) for the dates searched. No price was returned for the other 72 resorts; missing prices are excluded from county price averages.
- **County coverage:** The dataset includes resorts in Kajiado and Isiolo along the Athi and Ewaso Nyiro rivers, respectively, as part of the project's wider definition of waterfront destinations.
- The review-theme labels use keyword matching and VADER sentiment at the clause level. They are indicative labels, not a full summary of guest reviews.
- The analysis describes relationships in the collected data; it does not establish that location causes a particular rating.

## Future Improvements
- Collect pricing across more dates and from additional reliable sources to improve coverage.
- Develop a richer review-analysis approach that summarizes the reasons guests praise or criticize each resort.
