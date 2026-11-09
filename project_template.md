# 1. What is the problem you are solving?
> Businesses or your audience care about problems. Make the problem clear and relatable

**The Problem:** Travelers can't tell if a resort will be quiet just by looking at its overall Google rating. At inland lakes, nearby noise severely lowers guest satisfaction, but this isn't obvious to guests before they book.

**The Audience:** Travelers booking waterfront resorts in Kenya.

**The Question:** What drives customer satisfaction at Kenyan resorts, and does the impact of noise depend on the water body type?

# 2. What tools did you use?
> Python? GeoPandas? Google Big Query? Tell your audience how you got the answer, tools show your capability. Dive deep in this in your technical article

- **Google Places API:** Collected 168 waterfront resorts, their Google ratings, review counts, and noise sources within 1 km.
- **Python (Pandas):** Cleaned the data and analyzed review text to categorize what guests mention most.
- **Tableau:** Built a 4-part dashboard to visualize customer satisfaction.

# 3. What insights did you or do you want to discover? / What Solutions do you want to offer? Do People even need these solutions?
> Don’t just say “dashboard done.” Share the “aha!” moments, they matter more that the visuals

- **Dimension 1: Reputation** 
  * **Question:** Which resorts have the highest and lowest satisfaction? 
  * **Chart:** Top 10 & Bottom 10 Resorts (bar chart).

- **Dimension 2: Drivers** 
  * **Question:** What factors matter most to guests? 
  * **Chart:** What guests mention most in reviews (Service, Food, Noise).

  *   **The "Why":** Guests frequently mention "Setting & views" (nature, scenery). This suggests that travelers to lake resorts expect a peaceful environment. When noise interrupts this expectation, the drop in ratings is severe, proving noise is a dealbreaker for this specific audience.

- **Dimension 3: Pain Point** 
  * **Question:** Does noise affect ratings differently depending on the water body? 
  * **Chart:** Average rating by noise level and water body (line chart).

- **Dimension 4: Destination** 
  * **Question:** Where are these resorts located? 
  * **Chart:** Map of Kenyan waterfront resorts.

- **The "Aha!" Discovery (The Pain Point):** Noisier resorts get significantly lower ratings at inland lakes, but not at the coast. At the coast, noise doesn't seem to hurt the rating.

- **The Context (Why this happens):** Travelers choose resorts based on their desired vibe. Coast travelers often expect and enjoy lively surroundings, which is why noise doesn't hurt coastal ratings. Inland lake travelers expect peace and nature. When they get noise instead, their satisfaction drops.

- **The Evidence (Why lakes are different):** The data shows that "Setting & views" (nature, scenery, peace) is the 4th most mentioned topic in the reviews (129 mentions). When noise interrupts this expectation at an inland lake, satisfaction drops sharply (from 4.45 down to 4.14), whereas coastal ratings stay flat because the coastal vibe is already lively.

- **Limits:** This shows a correlation, not a cause. A zero noise count means "no recorded noise nearby," not "silent."

*Safari River Note: Safari River lodges are excluded from the line chart because they all recorded zero noise sources. Because they all fall into the single "Quiet" tier, they do not form a trend line.*

# 4. How would a business or a community benefit from your work?
> Be specific. Think money saved, process improves, better decisions made. That’s your real value

- **For Travelers:** Get matched with resorts that fit your vibe (quiet lakes vs. lively coasts) instead of guessing based on a single rating.

- **For Lake Resort Operators:** Proves that reducing noise will directly improve your Google rating and guest satisfaction.