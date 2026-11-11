# Kenya Waterfront Resorts: What Matters to Guests?

## 🔗 Live Dashboard
[Click here to view the interactive Tableau Dashboard](https://public.tableau.com/app/profile/james.mutunga/viz/KenyaWaterResorts/ResortNoiseDashboard#1)

## 📌 Project Overview
Travelers choosing a waterfront resort in Kenya usually see only one Google rating, which doesn't show what guests care about. This project analyzes **168 waterfront resorts** across the Kenyan coast, inland lakes, and safari rivers to see what matters to guests.

The central finding is that a single Google rating hides the real story. The "best" resort depends on what the traveler is looking for. The dashboard shows the highest-rated resorts, filtered to those where guests mention the chosen priority, and sentiment analysis removes the few resorts whose reviews are overall negative.

## 💡 Key Insights
*   **Interactive Exploration:** The Tableau dashboard allows users to filter by Resort Type (Marine Coast, Inland Lake, Safari River) and by their preferred Priority (Service, Food, Rooms, etc.). 
*   **The Reputation:** The Top 5, Middle 5, and Bottom 5 resorts for each resort type, pre-ranked by overall Google rating. The Priority filter hides resorts whose reviews do not mention the chosen priority.
*   **The Destination:** The map shows the geographic spread of these resorts, allowing travelers to see where their preferred vibe is located.

## 🛠️ Tools & Technologies
*   **Google Places API:** Used to collect resort data, including guest ratings, review counts, and review texts.
*   **Python (Pandas):** Used for data cleaning and text analysis to categorize review mentions.
*   **Python (VADER):** Used Natural Language Processing (NLP) to score each resort's combined reviews, removing the few resorts whose reviews are overall negative.
*   **Tableau:** Used to build the final interactive dashboard.
*   **Jupyter Notebook:** Documents the entire API collection, cleaning, and sentiment analysis process step-by-step.

## 📊 The 2 Dimensions of the Dashboard
The Tableau dashboard is structured around two key questions:
1.  **Destination:** Where are these resorts located, and how can users filter them?
2.  **Reputation:** Among the highest, middle, and lowest rated resorts, which ones do guests mention for the user's selected priority?

## ▶️ How to Run
1. Install the libraries: `pip install -r requirements.txt`
2. To skip the Google API calls, run the **Fast Track** cell in the notebook. It loads `Data/kenya_resorts_final.csv`.
3. To re-run the Google cells (Sections C to F), create a `.env` file containing `GOOGLE_MAPS_API_KEY=your_key_here`. The key is not included in this repository.

## 📂 Repository Structure
*   `Data/` - Contains the master CSV dataset (`kenya_resorts_final.csv`) and any backup files.
*   `resort_analysis.ipynb` - The Jupyter Notebook containing the Python code for data collection, cleaning, and analysis.
*   `project_template.md` - The narrative summary of the project (Context, Audience, Insights, and Business Value).

## ⚠️ Limitations
*   This analysis shows **correlation, not causation**. Guests rate resorts for many reasons.
*   The sentiment analysis is **document-level**. It scores the overall review as positive or negative, but does not perform sentence-level (Aspect-Based) analysis to isolate the exact sentence mentioning the specific priority.
*   Google returns only about 5 reviews per resort, so the text analysis is a sample.
*   Almost every resort scores positive (163 of 168), so the filter mostly shows whether guests *mention* a topic, not whether they praised it.

## 🚀 Future Improvements
*   **Aspect-Based Sentiment Analysis:** Upgrade the NLP model to analyze sentiment at the sentence level. This would allow us to isolate the exact sentence mentioning "Food" or "Service" to ensure that specific aspect was positive, rather than just the overall review.
*   **Live API Integration:** Instead of a static CSV, the dashboard could connect directly to the Google Places API for live updates.