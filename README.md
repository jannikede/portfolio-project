# Portfolio Project: Funnel and Revenue Analysis

The data used for this project is synthetic and was obtained from [(link)](https://huggingface.co/datasets/liniribeiro/synthetic-user-sessions/tree/main) 

# Executive Summary
The Analysis revealed two problems:
1) Only 1.2% of paying Customers visit the website regularly while 64% of site visits are not ending in a sale at all.
2) Every day between 2 and 4PM there is a strong drop in the revenue generated.
   
With high cart conversion rates, the business is not receiving the revenue that it would expect. Using Python I analyzed event and purchasing data of the business-website and identified that the largest opportunities for revenue increase 1) lie in higher customer retention or 2) to focus the business model on predominantly working with one-time-clients.

# Business Problem
In this hypothetical business, it was noticed that conversion rates are good and continuously on an expected level. However, the revenue earned does not reflect these numbers. Additionally, revenue further dropped during the last months and has not recovered. Because the revenue of the business is tied exclusively to sales, the development gives reasons for concern. Where are we missing out, when the conversion rates are looking so promising?

Specs: 8029 unique customers from USA, India, Germany, Brazil and the UK
The Conversion Rates look promising at first: 87.40% of viewed products are purchased. 89.66% of filled carts are purchased. 
However, with a Customer Lifetime Value of only 128$ and an average Customer Lifespan of 1 month, retention rates need to be improved. 

# Methodology
1. Exploratory Data und Funnel Analysis in Python to prepare the data and inspect patterns and relationships between variables.
2. Transfer of Data into Streamlit to visualize key concepts for stakeholders and enable interactive exploration of relationships 


# Skills
Python: Pandas, TimeSeries, MatPlotLib, Seaborn, Data Manipulation
Streamlit: Layout Configuration,  

# Results and Business Recommendations: 
To improve Customer Retention and Average Order Values, I propose to:

1) Stay updated – Set up a Dashboard that receives life data from the website to monitor 
2) Find your Persona – With more information on the unique customers, "positive" outliers based on highest average order value could be extracted to define a target group that marketing should focus on.
3) Experiment – Construct A/B Tests to find out what convinces different visitors to fill their carts and go through with the buy.
4) Go one step backwards – At the moment, every user is connected to one of four campaigns, which all perform equally, when visiting the site. Explore how the revenue is developing without an active campaign to be able to establish a baseline to work from. Do the campaigns even have a significant impact on revenue? Is the "new user offer" actually moving new visitors to buy more than they usually would, or could another offer/strategy be more beneficial to produce new customers?

# Next Steps & Limitations:
Because of the synthetic nature of the Dataset, some variables where not usable, due to the unnatural equal distribution of e.g. traffic source or campaign.

Nevertheless, next steps could inlcude: 
1) Simulating the revenue under a 5% increased customer retention rate.
2) Simulating the revenue generated through focusing campaigns on one-time-buyers.
