# Portfolio Project: Funnel and Revenue Analysis

The data used for this project is synthetic and was obtained from [(link)](https://huggingface.co/datasets/liniribeiro/synthetic-user-sessions/tree/main) 

# Executive Summary
The Analysis revealed two problems:
1) Only 1.2% of paying Customers visit the website regularly while 64% of site visits are not ending in a sale at all.
2) Every day between 2 and 4PM there is a strong drop in the revenue generated.
   
With high cart conversion rates, the business is not receiving the revenue that it would expect. Using Python I analyzed event and purchasing data of the business-website and identified that the largest opportunities for revenue increase lie in 1) higher customer retention or 2) focusing the business model on predominantly working with one-time-clients.

# Business Problem
In this hypothetical business, it was noticed that conversion rates (87.40% of viewed products are purchased) are good and continuously on an expected level. However, the revenue earned does not reflect these numbers. Additionally, revenue further dropped during the last months and has not recovered. Because the revenue of the business is tied exclusively to sales, the development gives reasons for concern. Where are we missing out, when the conversion rates are looking so promising? 

# Methodology
1. Exploratory Data und Funnel Analysis in Python to prepare the data and inspect patterns and relationships between variables.
2. Transfer of Data into Streamlit to visualize key concepts for stakeholders and enable interactive exploration of relationships 


# Skills
Python: Pandas, TimeSeries, MatPlotLib, Seaborn, Data Manipulation.  

Streamlit: Layout Configuration, Enabling Filter-Methods, Interactive Graphs.

# Results and Business Recommendations: 

I found that, with a Customer Lifetime Value of only 128$ and an average Customer Lifespan of 1 month, retention rates need to be improved. Additionally, a daily drop in revenue around 3PM further decreases earning opportunities, which needs to be compensated for.

<img width="1328" height="756" alt="Daily Revenue Output" src="https://github.com/user-attachments/assets/f8c692f9-31ae-4032-832b-f0fe9ca7db52" />

<img width="780" height="176" alt="Bildschirmfoto 2025-11-28 um 17 17 57" src="https://github.com/user-attachments/assets/f5772bff-9141-4f8a-9f1e-cc8beeebae7f" />



To improve Customer Retention I propose to:

1) Stay updated – Set up a Dashboard that receives life data from the website to monitor Conversion Rates of the Funnel
2) Find your Persona – With more information on the unique customers, "positive" outliers based on highest average order value could be extracted to define a target group that marketing should focus on.
3) Experiment – Construct A/B Tests to find out what convinces different visitors to fill their carts and go through with the buy.
4) Go one step backwards – At the moment, every user is connected to one of four campaigns, which all perform equally, when visiting the site. Explore how the revenue is developing without an active campaign to be able to establish a baseline to work from. Do the campaigns even have a significant impact on revenue? Is the "new user offer" actually moving new visitors to buy more than they usually would, or could another offer/strategy be more beneficial to produce new customers?

# Next Steps & Limitations:
Because of the synthetic nature of the Dataset, some variables where not usable, (e.g. unnatural equal distribution of traffic source or campaign).

Nevertheless, next steps could inlcude: 
1) Simulating the revenue under a 5% increased customer retention rate.
2) Simulating the revenue generated through focusing campaigns on one-time-buyers.
