-- 04_Route_Profitability/sql/waterfall_prep.sql
-- Preparing data for a Financial Waterfall Chart

SELECT 
    route_id,
    '1. Gross Revenue' as category,
    total_revenue as amount
FROM route_stats

UNION ALL

SELECT 
    route_id,
    '2. Fuel Cost' as category,
    -fuel_cost as amount
FROM route_stats

UNION ALL

SELECT 
    route_id,
    '3. Crew Cost' as category,
    -crew_cost as amount
FROM route_stats

UNION ALL

SELECT 
    route_id,
    '4. Airport Fees' as category,
    -airport_fees as amount
FROM route_stats;
