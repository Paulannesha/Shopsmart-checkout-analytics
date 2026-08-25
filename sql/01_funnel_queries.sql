Use Shopsmart_checkout_analytics;

Select * from shopsmart_experiment limit 5;

-- Overall Conversion by Variant:
Select variant, count(*) as total_users, sum(completed_purchase) as purchases, round(avg(completed_purchase)*100,2) as conversion_rate_pct from shopsmart_experiment group by variant;
-- Funnel drop-off at each stage:
select variant, round(avg(added_to_cart)*100,2) as cart_pct, round(avg(started_checkout)*100,2) as checkout_pct, round(avg(completed_purchase)*100,2) as purchase_pct from shopsmart_experiment group by variant;
-- Revenue by cohort month:
Select cohort_month, variant, round(sum(revenue),2) as total_revenue, round(avg(revenue),2) as avg_revenue_per_user from shopsmart_experiment group by cohort_month, variant order by cohort_month;

-- Retention by variant (month 1/2/3):
Select variant, round(avg(month_1_active)*100,2) as m1_retention, round(avg(month_2_active)*100,2) as m2_retention, round(avg(month_3_active)*100,2) as m3_retention from shopsmart_experiment group by variant;

-- Best-performing cohort month:
Select cohort_month, count(*) as users, round(avg(completed_purchase)*100,2) as conversion_rate from shopsmart_experiment group by cohort_month order by conversion_rate desc;