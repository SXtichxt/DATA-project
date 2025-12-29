select C.idcategories as id , C.title as tiltle , count(PD.idcategory) as product_count
from categories as C
left join products as PD
on C.idcategories = PD.idcategory
group by C.idcategories