# Kenya Waterfront Resorts: What Drives Customer Satisfaction?

## 🔗 Live Dashboard
[Click here to view the interactive Tableau Dashboard](https://public.tableau.com/app/profile/james.mutunga/viz/KenyaWaterResorts/ResortNoiseDashboard#1)

## 📌 Project Overview
Travelers pay premium prices for waterfront getaways in Kenya, but standard Google ratings don't tell the whole story. This project analyzes **168 waterfront resorts** across the Kenyan coast, inland lakes, and safari rivers to uncover what actually drives customer satisfaction. 

The central finding is that a single Google rating hides the real story. The "best" resort depends entirely on what the traveler is looking for. By using sentiment analysis, this dashboard filters out negative reviews, ranking resorts based *only* on positive guest experiences.

## 💡 Key Insights
*   **Interactive Exploration:** The Tableau dashboard allows users to filter by Resort Type (Coastal, Lakeside, Riverside) and by their preferred Priority (Service, Food, Rooms, etc.). 
*   **The Reputation:** We identified the Top 5, Middle 5, and Bottom 5 resorts *for each specific resort type* based on the user's selected priority and positive sentiment.
*   **The Destination:** The map shows the geographic spread of these resorts, allowing travelers to see where their preferred vibe is located.

## 🛠️ Tools & Technologies
*   **Google Places API:** Used to collect resort data, including guest ratings, review counts, and review texts.
*   **Python (Pandas):** Used for data cleaning and text analysis to categorize review mentions.
*   **Python (VADER):** Used Natural Language Processing (NLP) to score the sentiment of every review, ensuring the dashboard only highlights positive guest experiences.
*   **Tableau:** Used to build the final interactive dashboard.
*   **Jupyter Notebook:** Documents the entire API collection, cleaning, and sentiment analysis process step-by-step.

## 📊 The 2 Dimensions of the Dashboard
The Tableau dashboard is structured around two key questions:
1.  **Destination:** Where are these resorts located, and how can users filter them?
2.  **Reputation:** Which resorts have the highest, middle, and lowest satisfaction based on the user's selected priority?

## 📂 Repository Structure
*   `Data/` - Contains the master CSV dataset (`kenya_resorts_final.csv`) and any backup files.
*   `resort_analysis.ipynb` - The Jupyter Notebook containing the Python code for data collection, cleaning, and analysis.
*   `project_template.md` - The narrative summary of the project (Context, Audience, Insights, and Business Value).

## ⚠️ Limitations
*   This analysis shows **correlation, not causation**. Guests rate resorts for many reasons.
*   The sentiment analysis is **document-level**. It scores the overall review as positive or negative, but does not perform sentence-level (Aspect-Based) analysis to isolate the exact sentence mentioning the specific priority.

## 🚀 Future Improvements
*   **Aspect-Based Sentiment Analysis:** Upgrade the NLP model to analyze sentiment at the sentence level. This would allow us to isolate the exact sentence mentioning "Food" or "Service" to ensure that specific aspect was positive, rather than just the overall review.
*   **Live API Integration:** Instead of a static CSV, the dashboard could connect directly to the Google Places API for live updates.