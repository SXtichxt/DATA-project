select PD.idproducts,PD.title,C.title as category
from products AS PD
left join categories AS C
on PD.idcategory = C.idcategories;
