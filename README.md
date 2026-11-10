# Kenya Waterfront Resorts: What Drives Customer Satisfaction?

## 📌 Project Overview
Travelers pay premium prices for waterfront getaways in Kenya, but standard Google ratings don't tell the whole story. This project analyzes **168 waterfront resorts** across the Kenyan coast, inland lakes, and safari rivers to uncover what actually drives customer satisfaction. 

The central finding is that **noise is a dealbreaker for lake resorts, but not for the coast**. Coast travelers often expect and enjoy lively surroundings, which is why noise doesn't hurt coastal ratings. Inland lake travelers expect peace and nature. When they get noise instead, their satisfaction drops significantly.

## 💡 Key Insights
*   **The Drivers:** Service and Food are the most mentioned topics in reviews. However, noise remains a critical, hidden pain point.
*   **The Pain Point:** Noisier resorts get significantly lower ratings at inland lakes (dropping from 4.45 to 4.14), but not at the coast. 
*   **The Reputation:** We identified the Top 10 and Bottom 10 resorts (filtering for those with at least 50 reviews) to show travelers the best and worst extremes.
*   **The Destination:** Interactive mapping shows the geographic spread of these resorts and their respective "vibes."

## 🛠️ Tools & Technologies
*   **Google Places API:** Used to collect resort data, including guest ratings, review counts, review texts, and the number of nearby noise sources (bars, nightclubs, transit stations, and places of worship) within a 1 km radius.
*   **Python (Pandas):** Used for data cleaning, calculating distance metrics (Haversine formula), counting noise sources, and text analysis to categorize review mentions (Service, Food, Rooms, Noise, etc.).
*   **Tableau:** Used to build the final interactive dashboard, visualizing the four dimensions of customer satisfaction (Reputation, Drivers, Pain Point, Destination).
*   **Jupyter Notebook:** Documents the entire API collection and data-cleaning process step-by-step.

## 📊 The 4 Dimensions of the Dashboard
The Tableau dashboard is structured around four key questions:
1.  **Reputation:** Which resorts have the highest and lowest satisfaction?
2.  **Drivers:** What factors matter most to guests?
3.  **Pain Point:** Does noise affect ratings differently depending on the water body?
4.  **Destination:** Where are these resorts located?

## 📂 Repository Structure
*   `Data/` - Contains the master CSV dataset (`kenya_resorts_master.csv`) and any backup files.
*   `resort_analysis.ipynb` - The Jupyter Notebook containing the Python code for data collection, cleaning, and exploratory analysis.
*   `project_template.md` - The narrative summary of the project (Context, Audience, Insights, and Business Value).

## ⚠️ Limitations
*   This analysis shows **correlation, not causation**. Guests rate resorts for many reasons.
*   A noise count of zero means "no recorded noise sources nearby on Google," not absolute silence.
*   The text analysis uses keyword matching to count mentions, not sentiment analysis (it does not determine if a mention was positive or negative).