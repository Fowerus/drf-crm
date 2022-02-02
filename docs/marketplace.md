# **Marketplace API documentation** - **`/marketplace/`**   


## **This documentation will be expanded and complited in the future**

## **Address field**
**MProduct**  
The address field in MProduct table should contain list of product address  
```json  
{
	"address":["first", "second"]
}
```  
**MOrder**  
The address field in MOrder table should contain string  
```json  
{
	"address":"String"
}
```  

## **Products field**  
The products field should look like this.  
(`_id` key should contain mproduct `_id`.)  
(`count` key should contain mproduct necessary count.)  
```json  
{
	"products":[
		{"_id":"UHh8higphr8grhgreoTest", "count":4},
		{"_id":"ier7g8&gioejgoTest", "count":2},
	]
}
```   

## **Organization field**  
The organization field should look like this.  
```json  
{
	"organization":{
		"id":1
	}
}
```  

## **Courier field**
**MCourier**  
The courier field should look like this.    
(`id` key should contain organization_member id)  
```json  
{
	"courier":{
		"id":1
	}
}
```  
**MOrder**  
The courier field should look like this.     
(`_id` key should contain mcourier `_id`)   
```json  
{
	"courier":{
		"_id":"Uh8h8hjjy9845jy9j5jy94Test"
	}
}
```  
## **Author field**  
The author field should look like this.    
(`id` key should contain organization_member id)  
```json  
{
	"author":{
		"id":1
	}
}
```  