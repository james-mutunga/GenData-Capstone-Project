# 1. What is the problem you are solving?
> Businesses or your audience care about problems. Make the problem clear and relatable

**The Problem:** Travelers rely on a single Google rating to choose a **Kenyan waterfront resort**, but that score hides what matters most to different guests. Without knowing which topics guests talk about (service, food, views), travelers struggle to find a place that matches their personal priorities.

**The Audience:** Travelers booking **Kenyan waterfront resorts**.

**The Decision:** How to choose a resort based on personal priorities rather than just an overall rating.

**The Question:** What matters to guests across different resort types, and how can travelers use that data to find the best fit?

# 2. What tools did you use?
> Python? GeoPandas? Google Big Query? Tell your audience how you got the answer, tools show your capability. Dive deep in this in your technical article

- **Google Places API:** Collected data for 168 waterfront resorts, including ratings and review texts.
- **Python (Pandas):** Cleaned the data and used keyword analysis to flag which topics guests mention.
- **Python (VADER):** Used NLP sentiment analysis to remove the few resorts whose reviews are overall negative.
- **Tableau:** Built the interactive dashboard with a Priority filter.

# 3. What insights did you or do you want to discover? / What Solutions do you want to offer? Do People even need these solutions?
> Don’t just say “dashboard done.” Share the “aha!” moments, they matter more that the visuals

- **Dimension 1: Reputation** 
  * **Question:** Among the highest, middle and lowest rated resorts, which ones do guests mention for a specific priority?
  * **Chart:** Top 5, Middle 5 and Bottom 5 resorts for each water body type (ranked by overall rating), filtered to those whose reviews mention the selected priority.
- **Dimension 2: Destination** 
  * **Question:** Where are these resorts located? 
  * **Chart:** Interactive map of Kenyan waterfront resorts.

**The "Aha!" Discovery:** A single Google rating hides the real story. The best resort depends on the traveler. The dashboard shows the highest-rated resorts, filtered to those where guests mention the chosen priority, and removes the few resorts whose reviews are overall negative.

**Limits:** Google returns only about 5 reviews per resort, and sentiment is scored on those reviews combined, so almost every resort scores positive. The filter shows whether guests mention a topic, not whether they praised it.

# 4. How would a business or a community benefit from your work?
> Be specific. Think money saved, process improves, better decisions made. That’s your real value

- **For Travelers:** Helps them quickly shortlist the highest-rated resorts for their destination and priority, without digging through hundreds of reviews themselves.
- **For Resort Operators:** Shows which topics, like Service or Food, come up most in guest reviews, so operators can compare themselves with similar resorts.