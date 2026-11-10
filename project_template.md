# 1. What is the problem you are solving?
> Businesses or your audience care about problems. Make the problem clear and relatable

**The Problem:** Travelers rely on a single Google rating to choose a **Kenyan waterfront resort**, but that score hides what actually drives guest satisfaction. Without knowing what matters (service, food, views), travelers struggle to find a place that matches their personal priorities.

**The Audience:** Travelers booking **Kenyan waterfront resorts**.

**The Decision:** How to choose a resort based on personal priorities rather than just an overall rating.

**The Question:** What drives customer satisfaction across different resort types, and how can travelers use that data to find the best fit?

# 2. What tools did you use?
> Python? GeoPandas? Google Big Query? Tell your audience how you got the answer, tools show your capability. Dive deep in this in your technical article

- **Google Places API:** Collected data for 168 waterfront resorts, including ratings and review texts.
- **Python (Pandas):** Cleaned the data and used keyword analysis to categorize guest mentions.
- **Python (VADER):** Used NLP sentiment analysis to ensure the dashboard only highlights positive guest experiences.
- **Tableau:** Built the interactive dashboard with a dynamic Priority filter.

# 3. What insights did you or do you want to discover? / What Solutions do you want to offer? Do People even need these solutions?
> Don’t just say “dashboard done.” Share the “aha!” moments, they matter more that the visuals

- **Dimension 1: Reputation** 
  * **Question:** Which resorts have the highest, middle, and lowest satisfaction based on a specific priority? 
  * **Chart:** Dynamic Top 5, Middle 5, and Bottom 5 Resorts that update based on the selected priority.
- **Dimension 2: Destination** 
  * **Question:** Where are these resorts located? 
  * **Chart:** Interactive map of Kenyan waterfront resorts.

**The "Aha!" Discovery:** A single Google rating hides the real story. The best resort depends entirely on the traveler. By using sentiment analysis, the dashboard filters out negative reviews, ranking resorts based *only* on positive experiences.
**Limits:** The sentiment analysis is document-level, meaning it scores the whole review, not the specific sentence mentioning the priority. A zero noise count means "no recorded noise nearby," not "silent."

# 4. How would a business or a community benefit from your work?
> Be specific. Think money saved, process improves, better decisions made. That’s your real value

- **For Travelers:** Empowers them to instantly find the Top 5 resorts for their specific destination based *only* on positive reviews, without digging through hundreds of reviews themselves.
- **For Resort Operators:** Highlights exactly what guests are praising. Operators can see if they are falling behind competitors on key priorities like Service or Food and identify areas for improvement.