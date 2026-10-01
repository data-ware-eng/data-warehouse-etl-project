SELECT 
    f.sale_id,
	u.username,
	p.title AS product_name,
	p.price,
	f.quantity,
	(f.quantity * p.price) AS total_sale
FROM dim_users u
LEFT JOIN fact_sales f ON u.user_id = f.user_id
LEFT JOIN dim_products p ON f.product_id = p.product_id
ORDER BY f.sale_id DESC NULLS LAST;
