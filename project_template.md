# 1. What problem are you solving?

**The Problem:** Travelers can struggle to choose the right resort because a single Google rating does not tell the whole story. It does not show the range of destinations in a region, the prices returned for the dates being researched, or how widely reviewed a highly rated resort is.

**The Audience:** Leisure and business travelers, as well as travel agents helping clients compare accommodation.

**The Decision:** Which waterfront resort should a traveler shortlist in a chosen region of Kenya?

**The Question:** How can travelers filter resorts by county and compare their ratings, collected prices, and review counts in one place?

# 2. What tools did you use?

- **Google Places API:** Collected data for 168 waterfront resorts, including Google ratings and review counts.
- **Python (Pandas):** Cleaned the dataset, removed duplicates, and prepared the data for analysis and visualization.
- **Python (GeoPandas):** Performed a spatial join to assign resort coordinates to official Kenyan county boundaries, with manual corrections where needed.
- **Apify (Google Hotels Scraper):** Collected pricing information for 96 resorts (57%) for the dates searched. No price was returned for the remaining 72 resorts. The collected prices are a snapshot and may change.
- **Python (VADER and keyword-based aspect analysis):** Examined positive review clauses for keyword mentions of themes such as views, service, food, rooms, and amenities, then assigned each resort its most frequently mentioned positive theme. Resorts without a matching positive mention are labelled “General”.
- **Tableau:** Built the interactive dashboard, including the county map, Top N filter, price chart, and popularity scatterplot.
- **Streamlit:** Built the storytelling web app, which presents the findings and embeds the Tableau dashboard.

# 3. What insights do you want to discover, and what solutions do you offer?

The analysis is organized around four dimensions that users can explore interactively.

## Dimension 1: Location — The “Where”

**Question:** Where are the resorts located, and what does the overall distribution look like?

**Solution:** An interactive map of Kenya's nine resort-hosting counties. Selecting a county filters the dashboard to show resorts in that area. Kajiado and Isiolo are included because the dataset contains riverside resorts along the Athi and Ewaso Nyiro rivers.

## Dimension 2: Reputation — The “How Good”

**Question:** Which resorts have the highest ratings in the selected county?

**Solution:** A Top N horizontal bar chart. Users can select the Top 5, 10, or 20 resorts, ranked by Google rating.

**Methodology:** The chart includes only resorts with at least 50 reviews to reduce the influence of ratings based on very few reviews. Review count is used to break rating ties.

## Dimension 3: Pricing & Value — The “How Much”

**Question:** What are the minimum and average collected prices per night in the selected county?

**Solution:** A county-level price chart showing the average base price in Kenyan Shillings (KES), with a marker for the minimum price.

**Methodology:** Pricing information was returned for 96 of the 168 resorts (57%) for the dates searched. No price was returned for the remaining 72 resorts. Missing prices are excluded from county averages, so each average is based only on resorts with a returned price. The collected prices are a snapshot and may change.

## Dimension 4: Popularity — “Hidden Gems vs. Tourist Giants”

**Question:** Which resorts are highly rated but have relatively few reviews, and which combine high ratings with many reviews?

**Solution:** A scatterplot mapping Google rating on the Y-axis against review count on the X-axis. It helps users explore highly rated resorts with fewer reviews alongside highly rated resorts with many reviews.

## The Main Discovery

A single Google rating does not tell the whole story. Combining county-level filtering, rating-based rankings, collected prices, and review counts gives travelers a broader basis for comparing waterfront resorts. In this dataset, Narok (Masai Mara) has the highest average collected price, while coastal and lake destinations offer other price points. These comparisons describe the collected dataset and should not be treated as a guarantee of current prices.

# 4. How could a business or community benefit from your work?

- **For Travelers:** The dashboard makes it easier to compare resorts by destination, rating, price, and review count without manually opening many listings.
- **For Travel Agents:** It provides a starting point for shortlisting resorts in a client's preferred county and comparing the available rating and pricing information.
- **For Resort Operators:** It offers a way to compare their resort's rating, review count, and collected price with other resorts in the same county.

The dashboard is a research and comparison aid. Travelers should confirm current prices and availability with the resort before booking.
