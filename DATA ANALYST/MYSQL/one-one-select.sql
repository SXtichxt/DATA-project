select PD.idproducts,PD.title,PDN.note
from products AS PD
left join product_notes AS PDN
on PD.idproducts = PDN.product_id
order by idproducts asc;