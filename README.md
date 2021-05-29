# EApteka_server

Get sizes for ingredient_id  
http://90.188.90.101:8000/api/analogs/size?ingredient_id=1

Get products and ingredients by name  
http://90.188.90.101:8000/api/analogs/products_by_name?q=баз

Get values for drop-down list  
http://90.188.90.101:8000/api/analogs/drop_down_values  

Add analogs card  
http://90.188.90.101:8000/api/analogs/add  
```json
{
  "products": '[{"product": "1", "type": "inactive" }]',
  "number_of_times": "5",
  "days": "4",
  "reception_method": "1",
  "reception_time": "before_eating",
  "dosage": "209",
  "text": "209", 
}
```

Get analogs list by ingredient_id  
http://90.188.90.101:8000/api/analogs/list_by_ingredient?ingredient_id=1  

Get analogs set page  
http://90.188.90.101:8000/api/analogs/set?set_id=29  

Get all analogs set page  
http://90.188.90.101:8000/api/analogs/all  

Select analog in analog sets  
http://90.188.90.101:8000/api/analogs/select_analog  
```json
{
  "analog_product_id": "1"
}
```