# 1. What is the problem you are solving?
> Businesses or your audience care about problems. Make the problem clear and relatable

**The Problem:** Travelers rely on a single Google rating to choose a **Kenyan waterfront resort**, but a single score hides the real story. Does a high rating come from great food, excellent service, or a peaceful environment? Without knowing *what* actually drives a **Kenyan waterfront resort's** score, travelers struggle to find a place that matches their personal priorities—whether they want a lively beach scene, or a quiet lakeside retreat.

**The Audience:** Travelers booking **Kenyan waterfront resorts**.

**The Decision:** How to choose a **Kenyan waterfront resort** based on their personal priorities (such as service, food, or noise) rather than just an overall rating.

**The Question:** What drives customer satisfaction across different types of **Kenyan waterfront resorts** (coastal, lakeside, and riverside), and how can travelers use that data to find the best fit for them?

# 2. What tools did you use?
> Python? GeoPandas? Google Big Query? Tell your audience how you got the answer, tools show your capability. Dive deep in this in your technical article

- **Google Places API:** Collected 168 waterfront resorts, their Google ratings, review counts, and categorized nearby noise sources within 1 km.
- **Python (Pandas):** Cleaned the data and used keyword analysis to categorize what guests mention most in their reviews.
- **Tableau:** Built an interactive 3-part dashboard to visualize customer satisfaction.

# 3. What insights did you or do you want to discover? / What Solutions do you want to offer? Do People even need these solutions?
> Don’t just say “dashboard done.” Share the “aha!” moments, they matter more that the visuals

- **Dimension 1: Reputation** 
  * **Question:** Which resorts have the highest, middle, and lowest satisfaction? 
  * **Chart:** Top 5, Middle 5, and Bottom 5 Resorts for each resort type.
- **Dimension 2: Drivers** 
  * **Question:** What factors matter most to guests? 
  * **Chart:** What guests mention most in reviews (Service, Food, Noise, etc.).
- **Dimension 3: Destination** 
  * **Question:** Where are these resorts located? 
  * **Chart:** Interactive map of Kenyan waterfront resorts.

**The "Aha!" Discovery:** A single Google rating hides the real story. While Service and Food are the top drivers of satisfaction across all resorts, the interactive dashboard reveals that the "best" resort depends entirely on what the traveler is looking for. 
**Limits:** The review text analysis uses keyword matching to count mentions, not sentiment analysis. A zero noise count means "no recorded noise nearby," not "silent."

# 4. How would a business or a community benefit from your work?
> Be specific. Think money saved, process improves, better decisions made. That’s your real value

- **For Travelers:** Empowers them to filter by what matters most. They can easily find the Top 5 resorts for their specific destination (e.g., coastal or lakeside) without having to dig through hundreds of reviews.
- **For Resort Operators:** Shows exactly what guests are talking about. Operators can use this to see if they are falling behind competitors on key drivers like Service or Food.