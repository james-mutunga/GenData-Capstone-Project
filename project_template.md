1. What is the problem you are solving?
> Businesses or your audience care about problems. Make the problem clear and relatable

**The Problem:** Noise from bars, nightclubs, transit stations and places of worship near waterfront resorts can spoil the peaceful getaway guests are paying for.

**The Question:** Does noise near a resort go with lower guest ratings, and does that depend on where the resort is: on the coast, at an inland lake, or on a safari river?

2. What tools did you use?
> Python? GeoPanadas? Google Big Query?
> Tell your audience how you got the answer,  tools show your capability
> Dive deep in this in your technical article

- **Python (Pandas):** Cleaned and structured the resort dataset, counted noise sources, filtered results to places truly within 1 km, and checked the results.

- **Google Places API:** Collected 168 waterfront resorts across Kenya, their Google ratings, and the number of bars, nightclubs, transit stations and places of worship within 1 km of each one.
- **Tableau:** Built the charts that compare noise and ratings across the three water body types (marine coast, inland lake, safari river).

3. What insights did you or do you want to discover?/ What Solutions do you want to offer? Do People even need these solutions?
> Don’t just say “dashboard done.”
> Share the “aha!” moments, they matter more that the visuals

- **The "Aha!" Discovery:** Noisier resorts get lower ratings at inland lakes, but not at the coast.

- **Limits:** This shows a link, not a cause. A zero means "no recorded noise nearby", not "silent".

4. How would a business or a community (for Social Impact Projects) benefit from your work?
> Be specific. Think money saved, process improves, better decisions made
> That’s your **real value**

- **For Inland Lake Resort Operators:** Ratings step down as nearby noise goes up, so noise is worth tracking as a factor in guest satisfaction. Operators can use the noise counts to see how they compare with similar resorts, and to judge whether sound insulation or quieter room placement is worth testing.

- **For Travel Advisors:** Enables data-backed recommendations. Clients who value quiet can be matched with resorts that have few recorded noise sources nearby, instead of relying on vague marketing claims. At the coast, noise counts alone are not a good guide to ratings, so advisors should not use them there.
