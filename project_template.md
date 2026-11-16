# 1. What is the problem you are solving?
> Businesses or your audience care about problems. Make the problem clear and relatable

**The Problem:** Travelers struggle to choose the right hotel because a single Google rating doesn't tell the whole story. They don't know what the overall landscape of a region looks like, what the actual prices are, or which hotels are truly the best in a specific area without reading hundreds of reviews.

**The Audience:** Travelers (business and pleasure) and travel agents.

**The Decision:** Which specific hotel to book in a chosen region of Kenya.

**The Question:** How can travelers interactively filter resorts by region to instantly see the highest-rated options, real prices, and popularity, alongside the average price?

# 2. What tools did you use?
> Python? GeoPandas? Google Big Query? Tell your audience how you got the answer, tools show your capability. Dive deep in this in your technical article

- **Google Places API:** Collected the data for 168 waterfront resorts, including ratings and review counts.
- **Python (Pandas):** Cleaned the dataset, removed duplicates, and structured the data for visualization.
- **GeoPandas:** Used to perform a spatial join, assigning each resort's latitude and longitude to its official Kenyan county, correcting the few that did not match.
- **Apify (Google Hotels Scraper):** Used to fetch live pricing data (in USD and KES) and hotel classes. Prices were scraped in batches because of free-tier limits. 
- **Tableau:** Used to build the interactive dashboard, including the county map, the Top N filter, the price charts, and the popularity scatterplot.

# 3. What insights did you or do you want to discover? / What Solutions do you want to offer? Do People even need these solutions?
> Don’t just say “dashboard done.” Share the “aha!” moments, they matter more that the visuals

*The dashboard is built around four verifiable dimensions, allowing the user to freely explore the data:*

- **Dimension 1: Location (The "Where")** 
  * **Question:** Where are the resorts located, and what is the overall landscape of this area?
  * **Solution:** An interactive map of Kenya's counties. When the user clicks a county (like Lamu or Nakuru), the entire dashboard filters to show only the resorts in that area.

- **Dimension 2: Reputation (The "How Good")** 
  * **Question:** Which resorts are the highest rated in the area I selected?
  * **Solution:** A Top N horizontal bar chart. The user can use a slider to see the Top 5, 10, or 20 resorts in the selected county, ranked by Google Rating. 
  * **Methodology Note:** To avoid ratings based on only a few reviews, the Top N chart only includes resorts with at least 50 reviews. Ties are broken by review count.

- **Dimension 3: Pricing & Value (The "How Much")**
  * **Question:** What is the average cost per night in the region I selected?
  * **Solution:** A dynamic price chart showing the average base price (in KES) per county. Hovering over a bar reveals the Minimum and Maximum prices for that county.
  * **Methodology:** We successfully scraped 96 live prices (57% of the dataset). The remaining 72 resorts did not have a price listed on Google Hotels for the selected dates. Tableau automatically excludes these empty values (`NaN`) when calculating the county average. Averages use only resorts with a listed price.

- **Dimension 4: Popularity (The "Hidden Gems vs. Tourist Giants")**
  * **Question:** Which resorts are highly rated but have very few reviews, and which are highly rated with thousands of reviews? 
  * **Solution:** A Scatterplot mapping Rating (Y-axis) against Review Count (X-axis). This reveals "Hidden Gems" (top-left: high rating, low reviews) and "Tourist Giants" (top-right: high rating, massive reviews).

**The "Aha!" Discovery:** A single Google rating hides the real story. By combining geospatial filtering, dynamic ranking, real pricing, and popularity, we give travelers a complete picture. They can see that Narok (Masai Mara) has the highest average price by far, while the coast and lakes offer more affordable options. 

# 4. How would a business or a community benefit from your work?
> Be specific. Think money saved, process improves, better decisions made. That’s your real value

- **For Travelers:** It saves them time and protects their money. Instead of reading endless reviews and opening 20 tabs to check prices, they can click their desired destination on the map and instantly see a ranked list of the highest-rated resorts alongside the average regional price.
- **For Travel Agents:** It acts as a quick shortlisting tool. When a client says, "I want to go to Diani, and my budget is around 15,000 KES a night," the agent can instantly see the top-rated resorts in that area and filter for budget-appropriate options.
- **For Resort Operators:** It provides competitive intelligence. They can see how they rank against other resorts in their specific county, and how their pricing compares to the regional average.