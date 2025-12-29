select PD.idproducts as id , PD.title as title , group_concat(PDH.title) as hashtags
from products as PD
left join (
	select h1.title as title , PDH1.product_id as product_id
    from product_hashtags as PDH1
    left join hashtags as h1
    on PDH1.hashtag_id = h1.idhashtag
) as PDH
on PD.idproducts = PDH.product_id
group by PD.idproducts
