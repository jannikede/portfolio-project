# E-Commerce Funnel & Revenue Analysis

## Executive Summary
This e-commerce business faces a revenue paradox: strong cart conversion rates (87.40%) but disappointing overall revenue performance. Using Python and Streamlit, I analyzed user session and purchase data to identify critical gaps in the customer journey. The analysis revealed two major issues:

1. **Poor Customer Retention**: Only 1.2% of paying customers return to the site, while 64% of visits end without a purchase
2. **Revenue Drop Pattern**: Consistent daily revenue decline between 2-4 PM across certain markets

By building an interactive dashboard and conducting funnel analysis, I identified that the biggest revenue opportunities lie in improving customer retention strategies or pivoting the business model to optimize for one-time purchasers.

## Business Problem
Despite healthy conversion rates at the checkout stage, the business is experiencing declining revenue that doesn't align with funnel performance. The company needs to understand:
- Where customers are falling out of the funnel
- Why retention rates are so low (average customer lifespan: 1 month)
- What's causing the daily revenue drop during peak hours
- How to increase Customer Lifetime Value (currently only $128)

## Methodology
1. **Data Extraction & Cleaning**: Processed event-level user session data from Hugging Face synthetic dataset
2. **Funnel Analysis in Python**: Identified drop-off points across the customer journey using Pandas and visualization libraries
3. **Interactive Dashboard in Streamlit**: Built dynamic visualizations to enable stakeholder exploration of key metrics and filters
4. **Time Series Analysis**: Analyzed revenue patterns by hour, day, and country to identify temporal trends

## Skills & Tools
**Python**: Pandas, Matplotlib, Seaborn, Time Series Analysis, Data Manipulation  
**Streamlit**: Interactive dashboards, custom functions, dynamic filtering, layout configuration  
**Analytics**: Funnel analysis, cohort analysis, KPI tracking, statistical analysis

## Key Findings

### 1. Customer Retention Crisis
- **Customer Lifespan**: Average of just 1.01 months
- **Churn Rate**: 98.82% of customers never return
- **Unsuccessful Visits**: 64.03% of site visits result in no purchase

![KPI Dashboard](https://github.com/user-attachments/assets/5a1b0c0f-4a7d-450b-b2fc-e0f20127fbc7)

### 2. Daily Revenue Pattern
- Consistent revenue drop between 2-4 PM
- Pattern varies by geographic market
- Represents significant missed revenue opportunity

![Daily Revenue Pattern](https://github.com/user-attachments/assets/f8c692f9-31ae-4032-832b-f0fe9ca7db52)

## Business Recommendations

### Short-Term Actions
1. **Implement Live Monitoring**: Deploy the Streamlit dashboard with real-time data feeds to track funnel conversion rates and identify issues immediately
2. **Time-Based Campaigns**: Launch targeted promotions during 2-4 PM window to counteract the revenue drop
3. **Campaign Effectiveness Audit**: Analyze baseline performance without active campaigns—current campaigns show equal performance, suggesting potential inefficiency

### Long-Term Strategy
1. **Customer Segmentation**: Identify high-value customer personas based on average order value and purchase frequency to refine targeting
2. **Retention Experiments**: Design A/B tests focusing on:
   - Post-purchase email sequences
   - Loyalty rewards for second purchases
   - Personalized product recommendations
3. **Business Model Decision**: Simulate two scenarios:
   - Revenue impact of 5% retention rate improvement
   - Revenue optimization for one-time buyer model (streamlined acquisition, higher margins)

## Impact & Value
- **Democratized Analytics**: Interactive dashboard enables self-service exploration by stakeholders
- **Data-Driven Decision Making**: Quantified the specific funnel stages requiring intervention
- **Strategic Clarity**: Provided clear direction on whether to invest in retention vs. acquisition optimization

## Next Steps & Limitations
**Limitations**: Dataset is synthetic, resulting in unrealistic uniform distributions in some variables (e.g. traffic source, campaign attribution)

**Future Analysis**:
1. Revenue simulation modeling: 5% retention increase vs. one-time buyer optimization
2. Customer cohort analysis to identify natural retention patterns
3. Statistical significance testing for campaign performance
4. Geographic segmentation analysis for the 2-4 PM revenue drop

---

**Data Source**: [Synthetic User Sessions Dataset](https://huggingface.co/datasets/liniribeiro/synthetic-user-sessions/tree/main) from Hugging Face

**Dashboard**: [Link to deployed Streamlit app if available]
