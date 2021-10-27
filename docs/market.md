# **Market API documentation** - **`/market/`**   


## **Token error**
If the request is made without a token   
*`Response 401`*  
```json  
{
	"detail": "Authentication credentials were not provided."
}
```  
If you do not have enough rights or the account is not confirmed or the session has been deleted  
*`Response 403`*
```json  
{
	"detail": "You do not have permission to perform this action."
}
```  


## **ProductCategory**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **GET** `product-category-l/1/`           
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Phone",
	        "created_at": "2021-10-25T08:14:57.130029Z",
	        "updated_at": "2021-10-25T08:14:57.130065Z"
	    }
	]
	```   

## **Transaction**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **GET** `transaction-l/1/`           
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Phone",
	        "cashbox":1,
	        "sale_order":2,
	        "sale_product":null,
	        "purchase":null,
	        "created_at": "2021-10-25T08:14:57.130029Z",
	        "updated_at": "2021-10-25T08:14:57.130065Z"
	    }
	]
	```   

## **Product**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `product-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
	    "name": [
	        "This field is required."
	    ],
	    "purchase_price": [
	        "This field is required."
	    ],
	    "sale_price": [
	        "This field is required."
	    ],
	    "count": [
	        "This field is required."
	    ],
	    "supplier": [
	        "This field is required."
	    ],
	    "irreducible_balance": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```  
	**Input data**     
	```json  
	{
	    "name": "Macbook",
	    "purchase_price": "10.00",
	    "sale_price": "10.00",
	    "count": 50,
	    "supplier": "Stive",
	    "irreducible_balance": "0.0",
	    "organization": 1,
	    "service": 1,
	    "category": 1
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Macbook",
	    "purchase_price": "10.00",
	    "sale_price": "10.00",
	    "count": 50,
	    "supplier": "Stive",
	    "irreducible_balance": "0.0",
	    "organization": 1,
	    "service": 1,
	    "category": 1
	}
	```  
* **GET** `product-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Macbook",
	        "code": "603638776150318",
	        "barcode": "603638776942600",
	        "purchase_price": "10.00",
	        "sale_price": "10.00",
	        "count": 50,
	        "supplier": "Stive",
	        "irreducible_balance": "0.00",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "category": {
	            "id": 1,
	            "name": "Phone",
	            "created_at": "2021-10-25T08:14:57.130029Z",
	            "updated_at": "2021-10-25T08:14:57.130065Z"
	        },
	        "created_at": "2021-10-25T08:33:06.622719Z",
	        "updated_at": "2021-10-25T08:33:06.622757Z"
	    }
	]
	```   
* **PUT** `product-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	    "purchase_price": [
	        "This field is required."
	    ],
	    "sale_price": [
	        "This field is required."
	    ],
	    "count": [
	        "This field is required."
	    ],
	    "supplier": [
	        "This field is required."
	    ],
	    "irreducible_balance": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**      
	```json   
	{
	    "name": "Macbook2",
	    "purchase_price": "10.02",
	    "sale_price": "10.02",
	    "count": 52,
	    "supplier": "Stive2",
	    "irreducible_balance": "0.2",
	    "service": 1,
	    "category": 1
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Macbook2",
	    "purchase_price": "10.02",
	    "sale_price": "10.02",
	    "count": 52,
	    "supplier": "Stive2",
	    "irreducible_balance": "0.20",
	    "service": 1,
	    "category": 1
	}
	```  
* **PATCH** `product-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "Macbook2",
	    "purchase_price": "10.02",
	    "sale_price": "10.02",
	    "count": 52,
	    "supplier": "Stive2",
	    "irreducible_balance": "0.20",
	    "service": 1,
	    "category": 1
	}
	```   
	**Input data**      
	```json  
	{
	    "name": "Macbook",
	    "purchase_price": "10.00",
	    "sale_price": "10.00",
	    "count": 50,
	    "supplier": "Stive",
	    "irreducible_balance": "0.0",
	    "service": 1,
	    "category": 1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "Macbook",
	    "purchase_price": "10.00",
	    "sale_price": "10.00",
	    "count": 50,
	    "supplier": "Stive",
	    "irreducible_balance": "0.0",
	    "service": 1,
	    "category": 1
	}
	```  
* **DELETE** `product-ud/1/`  
	**Input data**       
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `product-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Macbook",
        "code": "603638776150318",
        "barcode": "603638776942600",
        "purchase_price": "10.00",
        "sale_price": "10.00",
        "count": 50,
        "supplier": "Stive",
        "irreducible_balance": "0.00",
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "category": {
            "id": 1,
            "name": "Phone",
            "created_at": "2021-10-25T08:14:57.130029Z",
            "updated_at": "2021-10-25T08:14:57.130065Z"
        },
        "created_at": "2021-10-25T08:33:06.622719Z",
        "updated_at": "2021-10-25T08:33:06.622757Z"
    }
	```  

## **Cashbox**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `cashbox-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
	    "name": [
	        "This field is required."
	    ],
	    "cash": [
	        "This field is required."
	    ],
	    "account_money": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**     
	```json  
	{
	    "organization":1,
	    "name":"Cashbox",
	    "cash":"3.0",
	    "account_money":"10.00",
	    "service":1
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Cashbox",
	    "cash": "3.00",
	    "account_money": "10.00",
	    "organization": 1,
	    "service": 1
	}
	```  
* **GET** `cashbox-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Cashbox",
	        "cash": "3.00",
	        "account_money": "10.00",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "created_at": "2021-10-25T09:38:44.934208Z",
	        "updated_at": "2021-10-25T09:38:44.934246Z"
	    }
	]
	```   
* **PUT** `cashbox-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	    "cash": [
	        "This field is required."
	    ],
	    "account_money": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	If you want to add or to subtract money from cashbox you need to add prefix field in your request body. Prefix cat be '+' or '-'  
	```   
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"Cashbox2",
	    "cash":"4.00",
	    "account_money":"60.00",
	    "service":1,
	    "prefix":"+"
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Cashbox2",
	    "cash": "7.00",
	    "account_money": "70.00",
	    "service": 1,
	    "prefix": "+"
	}
	```  
* **PATCH** `cashbox-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "Cashbox2",
	    "cash": "7.00",
	    "account_money": "70.00",
	    "service": 1
	}
	```   
	If you want to add or to subtract money from cashbox you need to add prefix field in your request body. Prefix cat be '+' or '-'     
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"Cashbox",
	    "cash":"4.00",
	    "account_money":"60.00",
	    "service":1,
	    "prefix":"-"
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Cashbox",
	    "cash": "3.00",
	    "account_money": "10.00",
	    "service": 1,
	    "prefix": "-"
	}
	```  
* **DELETE** `cashbox-ud/1/`  
	**Input data**       
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `cashbox-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Cashbox",
        "cash": "3.00",
        "account_money": "10.00",
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "created_at": "2021-10-25T09:38:44.934208Z",
        "updated_at": "2021-10-25T09:38:44.934246Z"
    }
	```  
## **PurchaseRequest**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `purchase-request-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
	    "price": [
	        "This field is required."
	    ],
	    "cashbox": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ],
	    "product": [
	        "This field is required."
	    ],
	    "count": [
	        "This field is required."
	    ],
	    "is_cash": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**     
	```json  
	{
	    "organization":1,
	    "service":1,
	    "product":4,
	    "count":2,
	    "cashbox":1,
	    "is_cash":false
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "organization": 1,
	    "cashbox": 1,
	    "service": 1,
	    "product": 4,
	    "count": 2,
	    "is_deferred": false,
	    "is_cash": false
	}
	```  
* **GET** `purchase-request-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 24,
	        "price": "20.00",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "cashbox": {
	            "id": 1,
	            "name": "Cashbox",
	            "cash": "3.00",
	            "account_money": "50.00",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "created_at": "2021-10-25T09:38:44.934208Z",
	            "updated_at": "2021-10-25T11:58:05.856366Z"
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "is_deferred": false,
	        "product": {
	            "id": 4,
	            "name": "Org2product",
	            "code": "4ey5r6uyikujgfh",
	            "barcode": "ytukhuytu6",
	            "purchase_price": "10.00",
	            "sale_price": "10.00",
	            "count": 10,
	            "supplier": "Org2",
	            "irreducible_balance": "0.00",
	            "organization": {
	                "id": 2,
	                "name": "Test2",
	                "description": "Test2",
	                "address": "Test2",
	                "creator": {
	                    "id": 2,
	                    "surname": "a2",
	                    "name": "a2",
	                    "second_name": "a2",
	                    "address": "a2",
	                    "email": "a2@gmail.com",
	                    "phone": null,
	                    "image": null,
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-24T11:46:46.122045Z",
	                    "updated_at": "2021-10-24T11:46:46.122074Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-24T12:51:25.358058Z",
	                "updated_at": "2021-10-24T12:51:25.358111Z"
	            },
	            "service": {
	                "id": 2,
	                "name": "TestService",
	                "address": "sfsfsgs",
	                "phone": "+79968269263",
	                "organization": {
	                    "id": 2,
	                    "name": "Test2",
	                    "description": "Test2",
	                    "address": "Test2",
	                    "creator": {
	                        "id": 2,
	                        "surname": "a2",
	                        "name": "a2",
	                        "second_name": "a2",
	                        "address": "a2",
	                        "email": "a2@gmail.com",
	                        "phone": null,
	                        "image": null,
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-24T11:46:46.122045Z",
	                        "updated_at": "2021-10-24T11:46:46.122074Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-24T12:51:25.358058Z",
	                    "updated_at": "2021-10-24T12:51:25.358111Z"
	                },
	                "created_at": "2021-10-25T11:55:57.294669Z",
	                "updated_at": "2021-10-25T11:55:57.294707Z"
	            },
	            "category": {
	                "id": 1,
	                "name": "Phone",
	                "created_at": "2021-10-25T08:14:57.130029Z",
	                "updated_at": "2021-10-25T08:14:57.130065Z"
	            },
	            "created_at": "2021-10-25T11:56:54.819323Z",
	            "updated_at": "2021-10-25T11:56:54.819360Z"
	        },
	        "count": 2,
	        "created_at": "2021-10-25T12:34:46.221325Z",
	        "updated_at": "2021-10-25T12:34:46.221367Z"
	    }
	]
	```   
* **DELETE** `purchase-request-ud/1/`  
	**Input data**       
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `purchase-request-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 24,
        "price": "20.00",
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "cashbox": {
            "id": 1,
            "name": "Cashbox",
            "cash": "3.00",
            "account_money": "50.00",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "created_at": "2021-10-25T09:38:44.934208Z",
            "updated_at": "2021-10-25T11:58:05.856366Z"
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "is_deferred": false,
        "product": {
            "id": 4,
            "name": "Org2product",
            "code": "4ey5r6uyikujgfh",
            "barcode": "ytukhuytu6",
            "purchase_price": "10.00",
            "sale_price": "10.00",
            "count": 10,
            "supplier": "Org2",
            "irreducible_balance": "0.00",
            "organization": {
                "id": 2,
                "name": "Test2",
                "description": "Test2",
                "address": "Test2",
                "creator": {
                    "id": 2,
                    "surname": "a2",
                    "name": "a2",
                    "second_name": "a2",
                    "address": "a2",
                    "email": "a2@gmail.com",
                    "phone": null,
                    "image": null,
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-24T11:46:46.122045Z",
                    "updated_at": "2021-10-24T11:46:46.122074Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-24T12:51:25.358058Z",
                "updated_at": "2021-10-24T12:51:25.358111Z"
            },
            "service": {
                "id": 2,
                "name": "TestService",
                "address": "sfsfsgs",
                "phone": "+79968269263",
                "organization": {
                    "id": 2,
                    "name": "Test2",
                    "description": "Test2",
                    "address": "Test2",
                    "creator": {
                        "id": 2,
                        "surname": "a2",
                        "name": "a2",
                        "second_name": "a2",
                        "address": "a2",
                        "email": "a2@gmail.com",
                        "phone": null,
                        "image": null,
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-24T11:46:46.122045Z",
                        "updated_at": "2021-10-24T11:46:46.122074Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-24T12:51:25.358058Z",
                    "updated_at": "2021-10-24T12:51:25.358111Z"
                },
                "created_at": "2021-10-25T11:55:57.294669Z",
                "updated_at": "2021-10-25T11:55:57.294707Z"
            },
            "category": {
                "id": 1,
                "name": "Phone",
                "created_at": "2021-10-25T08:14:57.130029Z",
                "updated_at": "2021-10-25T08:14:57.130065Z"
            },
            "created_at": "2021-10-25T11:56:54.819323Z",
            "updated_at": "2021-10-25T11:56:54.819360Z"
        },
        "count": 2,
        "created_at": "2021-10-25T12:34:46.221325Z",
        "updated_at": "2021-10-25T12:34:46.221367Z"
    }
	```  
## **PurchaseAccept**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **GET** `purchase-accept-l/2/`           
	**Response**  
	*`Response 400`*    
	```json  
	[
	    {
	        "id": 17,
	        "purchase_request": {
	            "id": 25,
	            "price": "20.00",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "cashbox": {
	                "id": 1,
	                "name": "Cashbox",
	                "cash": "3.00",
	                "account_money": "50.00",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "service": {
	                    "id": 1,
	                    "name": "Test",
	                    "address": "Test",
	                    "phone": "+79999999999",
	                    "organization": {
	                        "id": 1,
	                        "name": "Test",
	                        "description": "Test",
	                        "address": "Test",
	                        "creator": {
	                            "id": 1,
	                            "surname": "a",
	                            "name": "a",
	                            "second_name": "a",
	                            "address": "a",
	                            "email": "a@gmail.com",
	                            "phone": null,
	                            "image": "../static/Users/default-user-image.jpeg",
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-21T15:38:07.599042Z",
	                            "updated_at": "2021-10-22T10:52:18.483765Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-21T15:45:34.434734Z",
	                        "updated_at": "2021-10-21T15:45:34.434767Z"
	                    },
	                    "created_at": "2021-10-21T15:46:42.682220Z",
	                    "updated_at": "2021-10-21T15:46:42.682258Z"
	                },
	                "created_at": "2021-10-25T09:38:44.934208Z",
	                "updated_at": "2021-10-25T11:58:05.856366Z"
	            },
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "is_deferred": false,
	            "product": {
	                "id": 4,
	                "name": "Org2product",
	                "code": "4ey5r6uyikujgfh",
	                "barcode": "ytukhuytu6",
	                "purchase_price": "10.00",
	                "sale_price": "10.00",
	                "count": 10,
	                "supplier": "Org2",
	                "irreducible_balance": "0.00",
	                "organization": {
	                    "id": 2,
	                    "name": "Test2",
	                    "description": "Test2",
	                    "address": "Test2",
	                    "creator": {
	                        "id": 2,
	                        "surname": "a2",
	                        "name": "a2",
	                        "second_name": "a2",
	                        "address": "a2",
	                        "email": "a2@gmail.com",
	                        "phone": null,
	                        "image": null,
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-24T11:46:46.122045Z",
	                        "updated_at": "2021-10-24T11:46:46.122074Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-24T12:51:25.358058Z",
	                    "updated_at": "2021-10-24T12:51:25.358111Z"
	                },
	                "service": {
	                    "id": 2,
	                    "name": "TestService",
	                    "address": "sfsfsgs",
	                    "phone": "+79968269263",
	                    "organization": {
	                        "id": 2,
	                        "name": "Test2",
	                        "description": "Test2",
	                        "address": "Test2",
	                        "creator": {
	                            "id": 2,
	                            "surname": "a2",
	                            "name": "a2",
	                            "second_name": "a2",
	                            "address": "a2",
	                            "email": "a2@gmail.com",
	                            "phone": null,
	                            "image": null,
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-24T11:46:46.122045Z",
	                            "updated_at": "2021-10-24T11:46:46.122074Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-24T12:51:25.358058Z",
	                        "updated_at": "2021-10-24T12:51:25.358111Z"
	                    },
	                    "created_at": "2021-10-25T11:55:57.294669Z",
	                    "updated_at": "2021-10-25T11:55:57.294707Z"
	                },
	                "category": {
	                    "id": 1,
	                    "name": "Phone",
	                    "created_at": "2021-10-25T08:14:57.130029Z",
	                    "updated_at": "2021-10-25T08:14:57.130065Z"
	                },
	                "created_at": "2021-10-25T11:56:54.819323Z",
	                "updated_at": "2021-10-25T11:56:54.819360Z"
	            },
	            "count": 2,
	            "created_at": "2021-10-25T12:55:52.531332Z",
	            "updated_at": "2021-10-25T12:55:52.531370Z"
	        },
	        "organization": {
	            "id": 2,
	            "name": "Test2",
	            "description": "Test2",
	            "address": "Test2",
	            "creator": {
	                "id": 2,
	                "surname": "a2",
	                "name": "a2",
	                "second_name": "a2",
	                "address": "a2",
	                "email": "a2@gmail.com",
	                "phone": null,
	                "image": null,
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-24T11:46:46.122045Z",
	                "updated_at": "2021-10-24T11:46:46.122074Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-24T12:51:25.358058Z",
	            "updated_at": "2021-10-24T12:51:25.358111Z"
	        },
	        "is_cash": false,
	        "accept": false,
	        "updated_at": "2021-10-25T12:56:16.668720Z",
	        "created_at": "2021-10-25T12:56:16.668683Z"
	    }
	]
	```     
* **GET** `purchase-accept-r/17/2/`           
	**Response**  
	*`Response 400`*    
	```json  
    {
        "id": 17,
        "purchase_request": {
            "id": 25,
            "price": "20.00",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "cashbox": {
                "id": 1,
                "name": "Cashbox",
                "cash": "3.00",
                "account_money": "50.00",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "service": {
                    "id": 1,
                    "name": "Test",
                    "address": "Test",
                    "phone": "+79999999999",
                    "organization": {
                        "id": 1,
                        "name": "Test",
                        "description": "Test",
                        "address": "Test",
                        "creator": {
                            "id": 1,
                            "surname": "a",
                            "name": "a",
                            "second_name": "a",
                            "address": "a",
                            "email": "a@gmail.com",
                            "phone": null,
                            "image": "../static/Users/default-user-image.jpeg",
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-21T15:38:07.599042Z",
                            "updated_at": "2021-10-22T10:52:18.483765Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-21T15:45:34.434734Z",
                        "updated_at": "2021-10-21T15:45:34.434767Z"
                    },
                    "created_at": "2021-10-21T15:46:42.682220Z",
                    "updated_at": "2021-10-21T15:46:42.682258Z"
                },
                "created_at": "2021-10-25T09:38:44.934208Z",
                "updated_at": "2021-10-25T11:58:05.856366Z"
            },
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "is_deferred": false,
            "product": {
                "id": 4,
                "name": "Org2product",
                "code": "4ey5r6uyikujgfh",
                "barcode": "ytukhuytu6",
                "purchase_price": "10.00",
                "sale_price": "10.00",
                "count": 10,
                "supplier": "Org2",
                "irreducible_balance": "0.00",
                "organization": {
                    "id": 2,
                    "name": "Test2",
                    "description": "Test2",
                    "address": "Test2",
                    "creator": {
                        "id": 2,
                        "surname": "a2",
                        "name": "a2",
                        "second_name": "a2",
                        "address": "a2",
                        "email": "a2@gmail.com",
                        "phone": null,
                        "image": null,
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-24T11:46:46.122045Z",
                        "updated_at": "2021-10-24T11:46:46.122074Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-24T12:51:25.358058Z",
                    "updated_at": "2021-10-24T12:51:25.358111Z"
                },
                "service": {
                    "id": 2,
                    "name": "TestService",
                    "address": "sfsfsgs",
                    "phone": "+79968269263",
                    "organization": {
                        "id": 2,
                        "name": "Test2",
                        "description": "Test2",
                        "address": "Test2",
                        "creator": {
                            "id": 2,
                            "surname": "a2",
                            "name": "a2",
                            "second_name": "a2",
                            "address": "a2",
                            "email": "a2@gmail.com",
                            "phone": null,
                            "image": null,
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-24T11:46:46.122045Z",
                            "updated_at": "2021-10-24T11:46:46.122074Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-24T12:51:25.358058Z",
                        "updated_at": "2021-10-24T12:51:25.358111Z"
                    },
                    "created_at": "2021-10-25T11:55:57.294669Z",
                    "updated_at": "2021-10-25T11:55:57.294707Z"
                },
                "category": {
                    "id": 1,
                    "name": "Phone",
                    "created_at": "2021-10-25T08:14:57.130029Z",
                    "updated_at": "2021-10-25T08:14:57.130065Z"
                },
                "created_at": "2021-10-25T11:56:54.819323Z",
                "updated_at": "2021-10-25T11:56:54.819360Z"
            },
            "count": 2,
            "created_at": "2021-10-25T12:55:52.531332Z",
            "updated_at": "2021-10-25T12:55:52.531370Z"
        },
        "organization": {
            "id": 2,
            "name": "Test2",
            "description": "Test2",
            "address": "Test2",
            "creator": {
                "id": 2,
                "surname": "a2",
                "name": "a2",
                "second_name": "a2",
                "address": "a2",
                "email": "a2@gmail.com",
                "phone": null,
                "image": null,
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-24T11:46:46.122045Z",
                "updated_at": "2021-10-24T11:46:46.122074Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-24T12:51:25.358058Z",
            "updated_at": "2021-10-24T12:51:25.358111Z"
        },
        "is_cash": false,
        "accept": false,
        "updated_at": "2021-10-25T12:56:16.668720Z",
        "created_at": "2021-10-25T12:56:16.668683Z"
    }
	```   
* **PUT** `purchase-accept-ud/17/`    
	**Empty request body**     
	**Response**    
	If the necessary conditions related to the money at the buyer's cashbox or the quantity of products are correct   
	*`Response 400`*   
	```json    
	{
	    "accept": true
	}
	```   
* **PATCH** `purchase-accept-ud/17/`    
	**Empty request body**     
	**Response**    
	If the necessary conditions related to the money at the buyer's cashbox or the quantity of products are correct   
	*`Response 400`*   
	```json    
	{
	    "accept": true
	}
	```   
* **DELETE** `purchase-accept-ud/17/`   
	**Input data**  
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
## **ProductOrder**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `product-order-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json   
	{
	    "name": [
	        "This field is required."
	    ],
	    "products": [
	        "This field is required."
	    ],
	    "order": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**       
	```json   
	{
	    "organization":1,
	    "name":"OrderPack",
	    "products":[9,9,5],
	    "order":1,
	    "service":1
	}
	```   
	**Response**  
	*`Response 201`*    
	```json   
	{
	    "name": "OrderPack",
	    "organization": 1,
	    "products": [
	        5,
	        9
	    ],
	    "order": 1,
	    "service": 1
	}
	```  
* **GET** `product-order-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 9,
	        "name": "Test4",
	        "price": "30.00",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "products": [
	            {
	                "id": 5,
	                "name": "Org2product",
	                "code": "574426714052815",
	                "barcode": "574426714845097",
	                "purchase_price": "10.00",
	                "sale_price": "10.00",
	                "count": 3,
	                "supplier": "Test2",
	                "irreducible_balance": "0.00",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "service": {
	                    "id": 1,
	                    "name": "Test",
	                    "address": "Test",
	                    "phone": "+79999999999",
	                    "organization": {
	                        "id": 1,
	                        "name": "Test",
	                        "description": "Test",
	                        "address": "Test",
	                        "creator": {
	                            "id": 1,
	                            "surname": "a",
	                            "name": "a",
	                            "second_name": "a",
	                            "address": "a",
	                            "email": "a@gmail.com",
	                            "phone": null,
	                            "image": "../static/Users/default-user-image.jpeg",
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-21T15:38:07.599042Z",
	                            "updated_at": "2021-10-22T10:52:18.483765Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-21T15:45:34.434734Z",
	                        "updated_at": "2021-10-21T15:45:34.434767Z"
	                    },
	                    "created_at": "2021-10-21T15:46:42.682220Z",
	                    "updated_at": "2021-10-21T15:46:42.682258Z"
	                },
	                "category": {
	                    "id": 1,
	                    "name": "Phone",
	                    "created_at": "2021-10-25T08:14:57.130029Z",
	                    "updated_at": "2021-10-25T08:14:57.130065Z"
	                },
	                "created_at": "2021-10-25T13:26:32.306469Z",
	                "updated_at": "2021-10-25T16:32:58.474888Z"
	            },
	            {
	                "id": 9,
	                "name": "Test item",
	                "code": "tryukhjbmgftryukmnbg",
	                "barcode": "wt4eyuiykj",
	                "purchase_price": "10.00",
	                "sale_price": "2.00",
	                "count": 3,
	                "supplier": "I",
	                "irreducible_balance": "0.00",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "service": {
	                    "id": 1,
	                    "name": "Test",
	                    "address": "Test",
	                    "phone": "+79999999999",
	                    "organization": {
	                        "id": 1,
	                        "name": "Test",
	                        "description": "Test",
	                        "address": "Test",
	                        "creator": {
	                            "id": 1,
	                            "surname": "a",
	                            "name": "a",
	                            "second_name": "a",
	                            "address": "a",
	                            "email": "a@gmail.com",
	                            "phone": null,
	                            "image": "../static/Users/default-user-image.jpeg",
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-21T15:38:07.599042Z",
	                            "updated_at": "2021-10-22T10:52:18.483765Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-21T15:45:34.434734Z",
	                        "updated_at": "2021-10-21T15:45:34.434767Z"
	                    },
	                    "created_at": "2021-10-21T15:46:42.682220Z",
	                    "updated_at": "2021-10-21T15:46:42.682258Z"
	                },
	                "category": {
	                    "id": 1,
	                    "name": "Phone",
	                    "created_at": "2021-10-25T08:14:57.130029Z",
	                    "updated_at": "2021-10-25T08:14:57.130065Z"
	                },
	                "created_at": "2021-10-25T16:17:57.120771Z",
	                "updated_at": "2021-10-25T16:32:58.473126Z"
	            }
	        ],
	        "order": {
	            "id": 1,
	            "order_code": "eawtt",
	            "description": "retw4bt54t43",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "executor": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "client": 1,
	            "done": false,
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "order_status": 1,
	            "created_at": "2021-10-21T15:54:30.332013Z",
	            "updated_at": "2021-10-21T15:54:30.332050Z",
	            "device_type": "rer",
	            "device_maker": "werwer",
	            "device_model": "werwerewrwe",
	            "device_kit": "",
	            "device_appearance": "",
	            "device_defect": ""
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "created_at": "2021-10-25T17:22:07.109240Z",
	        "updated_at": "2021-10-25T17:22:07.109277Z"
	    }
	]
	```   
* **PUT** `product-order-ud/4/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	    "price": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"OrderPackBagFixProMaxCostAdd++",
	    "price":15.00,
	    "service":1
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "OrderPackBagFixProMaxCostAdd++",
	    "price": "15.00",
	    "service": 1
	}
	```  
* **PATCH** `product-order-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "OrderPackBagFixProMaxCostAdd++",
	    "price": "15.00",
	    "service": 1
	}
	```   
	**Input data**      
	```json  
	{
	    "organization":1,
	    "name":"OrderPackComeback",
	    "price":14.00,
	    "service":1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "OrderPackComeback",
	    "price": "14.00",
	    "service": 1
	}
	```  
* **DELETE** `product-order-ud/1/`  
	**Input data**  
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `sale-product-r/9/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 9,
        "name": "Test4",
        "price": "30.00",
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "products": [
            {
                "id": 5,
                "name": "Org2product",
                "code": "574426714052815",
                "barcode": "574426714845097",
                "purchase_price": "10.00",
                "sale_price": "10.00",
                "count": 3,
                "supplier": "Test2",
                "irreducible_balance": "0.00",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "service": {
                    "id": 1,
                    "name": "Test",
                    "address": "Test",
                    "phone": "+79999999999",
                    "organization": {
                        "id": 1,
                        "name": "Test",
                        "description": "Test",
                        "address": "Test",
                        "creator": {
                            "id": 1,
                            "surname": "a",
                            "name": "a",
                            "second_name": "a",
                            "address": "a",
                            "email": "a@gmail.com",
                            "phone": null,
                            "image": "../static/Users/default-user-image.jpeg",
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-21T15:38:07.599042Z",
                            "updated_at": "2021-10-22T10:52:18.483765Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-21T15:45:34.434734Z",
                        "updated_at": "2021-10-21T15:45:34.434767Z"
                    },
                    "created_at": "2021-10-21T15:46:42.682220Z",
                    "updated_at": "2021-10-21T15:46:42.682258Z"
                },
                "category": {
                    "id": 1,
                    "name": "Phone",
                    "created_at": "2021-10-25T08:14:57.130029Z",
                    "updated_at": "2021-10-25T08:14:57.130065Z"
                },
                "created_at": "2021-10-25T13:26:32.306469Z",
                "updated_at": "2021-10-25T16:32:58.474888Z"
            },
            {
                "id": 9,
                "name": "Test item",
                "code": "tryukhjbmgftryukmnbg",
                "barcode": "wt4eyuiykj",
                "purchase_price": "10.00",
                "sale_price": "2.00",
                "count": 3,
                "supplier": "I",
                "irreducible_balance": "0.00",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "service": {
                    "id": 1,
                    "name": "Test",
                    "address": "Test",
                    "phone": "+79999999999",
                    "organization": {
                        "id": 1,
                        "name": "Test",
                        "description": "Test",
                        "address": "Test",
                        "creator": {
                            "id": 1,
                            "surname": "a",
                            "name": "a",
                            "second_name": "a",
                            "address": "a",
                            "email": "a@gmail.com",
                            "phone": null,
                            "image": "../static/Users/default-user-image.jpeg",
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-21T15:38:07.599042Z",
                            "updated_at": "2021-10-22T10:52:18.483765Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-21T15:45:34.434734Z",
                        "updated_at": "2021-10-21T15:45:34.434767Z"
                    },
                    "created_at": "2021-10-21T15:46:42.682220Z",
                    "updated_at": "2021-10-21T15:46:42.682258Z"
                },
                "category": {
                    "id": 1,
                    "name": "Phone",
                    "created_at": "2021-10-25T08:14:57.130029Z",
                    "updated_at": "2021-10-25T08:14:57.130065Z"
                },
                "created_at": "2021-10-25T16:17:57.120771Z",
                "updated_at": "2021-10-25T16:32:58.473126Z"
            }
        ],
        "order": {
            "id": 1,
            "order_code": "eawtt",
            "description": "retw4bt54t43",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "executor": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "client": 1,
            "done": false,
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "order_status": 1,
            "created_at": "2021-10-21T15:54:30.332013Z",
            "updated_at": "2021-10-21T15:54:30.332050Z",
            "device_type": "rer",
            "device_maker": "werwer",
            "device_model": "werwerewrwe",
            "device_kit": "",
            "device_appearance": "",
            "device_defect": ""
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "created_at": "2021-10-25T17:22:07.109240Z",
        "updated_at": "2021-10-25T17:22:07.109277Z"
    }
	```    
## **SaleProduct**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `sale-product-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
	    "cash": [
	        "This field is required."
	    ],
	    "card": [
	        "This field is required."
	    ],
	    "bank_transfer": [
	        "This field is required."
	    ],
	    "discount": [
	        "This field is required."
	    ],
	    "cashbox": [
	        "This field is required."
	    ],
	    "product": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```
	Also you can add client field in request body     
	**Input data**     
	```json  
	{
	    "organization":1,
	    "cash":20.00,
	    "card":0,
	    "bank_transfer":0,
	    "discount":0,
	    "cashbox":1,
	    "product":5,
	    "service":1
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "cash": "20.00",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "organization": 1,
	    "cashbox": 1,
	    "product": 5,
	    "service": 1
	}
	```  
* **GET** `sale-product-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "cash": "20.00",
	        "card": "0.00",
	        "bank_transfer": "0.00",
	        "discount": "0.00",
	        "client": null,
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "cashbox": {
	            "id": 1,
	            "name": "Cashbox",
	            "cash": "23.00",
	            "account_money": "10.00",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "created_at": "2021-10-25T09:38:44.934208Z",
	            "updated_at": "2021-10-25T15:38:53.298977Z"
	        },
	        "product": {
	            "id": 5,
	            "name": "Org2product",
	            "code": "574426714052815",
	            "barcode": "574426714845097",
	            "purchase_price": "10.00",
	            "sale_price": "10.00",
	            "count": -1,
	            "supplier": "Test2",
	            "irreducible_balance": "0.00",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "category": {
	                "id": 1,
	                "name": "Phone",
	                "created_at": "2021-10-25T08:14:57.130029Z",
	                "updated_at": "2021-10-25T08:14:57.130065Z"
	            },
	            "created_at": "2021-10-25T13:26:32.306469Z",
	            "updated_at": "2021-10-25T15:38:53.295302Z"
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "created_at": "2021-10-25T15:38:53.278389Z",
	        "updated_at": "2021-10-25T15:38:53.301514Z"
	    }
	]
	```   
* **PUT** `sale-product-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "cash": [
	        "This field is required."
	    ],
	    "card": [
	        "This field is required."
	    ],
	    "bank_transfer": [
	        "This field is required."
	    ],
	    "discount": [
	        "This field is required."
	    ],
	    "cashbox": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**      
	```json   
	{
	    "cash": "20.02",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "cashbox": 1,
	    "service": 1
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "ServicePrice2",
	    "price": 20.02
	}
	```  
* **PATCH** `sale-product-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "cash": "20.02",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "cashbox": 1,
	    "service": 1
	}
	```   
	**Input data**      
	```json  
	{
	    "organization":1,
	    "cash":20.00,
	    "card":0,
	    "bank_transfer":0,
	    "discount":0,
	    "cashbox":1,
	    "product":5,
	    "service":1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "cash": "20.00",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "cashbox": 1,
	    "service": 1
	}
	```  
* **DELETE** `sale-product-ud/1/`  
	**Input data**  
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `sale-product-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "cash": "20.00",
        "card": "0.00",
        "bank_transfer": "0.00",
        "discount": "0.00",
        "client": null,
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "cashbox": {
            "id": 1,
            "name": "Cashbox",
            "cash": "23.00",
            "account_money": "10.00",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "created_at": "2021-10-25T09:38:44.934208Z",
            "updated_at": "2021-10-25T15:38:53.298977Z"
        },
        "product": {
            "id": 5,
            "name": "Org2product",
            "code": "574426714052815",
            "barcode": "574426714845097",
            "purchase_price": "10.00",
            "sale_price": "10.00",
            "count": -1,
            "supplier": "Test2",
            "irreducible_balance": "0.00",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "category": {
                "id": 1,
                "name": "Phone",
                "created_at": "2021-10-25T08:14:57.130029Z",
                "updated_at": "2021-10-25T08:14:57.130065Z"
            },
            "created_at": "2021-10-25T13:26:32.306469Z",
            "updated_at": "2021-10-25T15:38:53.295302Z"
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "created_at": "2021-10-25T15:38:53.278389Z",
        "updated_at": "2021-10-25T15:38:53.301514Z"
    }
	```    
## **SaleOrder**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `sale-order-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
	    "cash": [
	        "This field is required."
	    ],
	    "card": [
	        "This field is required."
	    ],
	    "bank_transfer": [
	        "This field is required."
	    ],
	    "discount": [
	        "This field is required."
	    ],
	    "cashbox": [
	        "This field is required."
	    ],
	    "product_order": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```
	Also you can add client field in request body     
	**Input data**     
	```json  
	{
	    "organization":1,
	    "cash":"30.00",
	    "card":0,
	    "bank_transfer":0,
	    "discount":"0",
	    "cashbox":1,
	    "service":1,
	    "product_order":9
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "cash": "30.00",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "organization": 1,
	    "cashbox": 1,
	    "product_order": 9,
	    "service": 1
	}
	```  
* **GET** `sale-order-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "cash": "30.00",
	        "card": "0.00",
	        "bank_transfer": "0.00",
	        "discount": "0.00",
	        "client": null,
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "cashbox": {
	            "id": 1,
	            "name": "Cashbox",
	            "cash": "53.00",
	            "account_money": "10.00",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "created_at": "2021-10-25T09:38:44.934208Z",
	            "updated_at": "2021-10-25T17:34:49.358778Z"
	        },
	        "product_order": {
	            "id": 9,
	            "name": "Test4",
	            "price": "30.00",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "products": [
	                {
	                    "id": 5,
	                    "name": "Org2product",
	                    "code": "574426714052815",
	                    "barcode": "574426714845097",
	                    "purchase_price": "10.00",
	                    "sale_price": "10.00",
	                    "count": 3,
	                    "supplier": "Test2",
	                    "irreducible_balance": "0.00",
	                    "organization": {
	                        "id": 1,
	                        "name": "Test",
	                        "description": "Test",
	                        "address": "Test",
	                        "creator": {
	                            "id": 1,
	                            "surname": "a",
	                            "name": "a",
	                            "second_name": "a",
	                            "address": "a",
	                            "email": "a@gmail.com",
	                            "phone": null,
	                            "image": "../static/Users/default-user-image.jpeg",
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-21T15:38:07.599042Z",
	                            "updated_at": "2021-10-22T10:52:18.483765Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-21T15:45:34.434734Z",
	                        "updated_at": "2021-10-21T15:45:34.434767Z"
	                    },
	                    "service": {
	                        "id": 1,
	                        "name": "Test",
	                        "address": "Test",
	                        "phone": "+79999999999",
	                        "organization": {
	                            "id": 1,
	                            "name": "Test",
	                            "description": "Test",
	                            "address": "Test",
	                            "creator": {
	                                "id": 1,
	                                "surname": "a",
	                                "name": "a",
	                                "second_name": "a",
	                                "address": "a",
	                                "email": "a@gmail.com",
	                                "phone": null,
	                                "image": "../static/Users/default-user-image.jpeg",
	                                "confirmed_email": true,
	                                "confirmed_phone": false,
	                                "created_at": "2021-10-21T15:38:07.599042Z",
	                                "updated_at": "2021-10-22T10:52:18.483765Z"
	                            },
	                            "numbers": null,
	                            "links": null,
	                            "created_at": "2021-10-21T15:45:34.434734Z",
	                            "updated_at": "2021-10-21T15:45:34.434767Z"
	                        },
	                        "created_at": "2021-10-21T15:46:42.682220Z",
	                        "updated_at": "2021-10-21T15:46:42.682258Z"
	                    },
	                    "category": {
	                        "id": 1,
	                        "name": "Phone",
	                        "created_at": "2021-10-25T08:14:57.130029Z",
	                        "updated_at": "2021-10-25T08:14:57.130065Z"
	                    },
	                    "created_at": "2021-10-25T13:26:32.306469Z",
	                    "updated_at": "2021-10-25T16:32:58.474888Z"
	                },
	                {
	                    "id": 9,
	                    "name": "Test item",
	                    "code": "tryukhjbmgftryukmnbg",
	                    "barcode": "wt4eyuiykj",
	                    "purchase_price": "10.00",
	                    "sale_price": "2.00",
	                    "count": 3,
	                    "supplier": "I",
	                    "irreducible_balance": "0.00",
	                    "organization": {
	                        "id": 1,
	                        "name": "Test",
	                        "description": "Test",
	                        "address": "Test",
	                        "creator": {
	                            "id": 1,
	                            "surname": "a",
	                            "name": "a",
	                            "second_name": "a",
	                            "address": "a",
	                            "email": "a@gmail.com",
	                            "phone": null,
	                            "image": "../static/Users/default-user-image.jpeg",
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-21T15:38:07.599042Z",
	                            "updated_at": "2021-10-22T10:52:18.483765Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-21T15:45:34.434734Z",
	                        "updated_at": "2021-10-21T15:45:34.434767Z"
	                    },
	                    "service": {
	                        "id": 1,
	                        "name": "Test",
	                        "address": "Test",
	                        "phone": "+79999999999",
	                        "organization": {
	                            "id": 1,
	                            "name": "Test",
	                            "description": "Test",
	                            "address": "Test",
	                            "creator": {
	                                "id": 1,
	                                "surname": "a",
	                                "name": "a",
	                                "second_name": "a",
	                                "address": "a",
	                                "email": "a@gmail.com",
	                                "phone": null,
	                                "image": "../static/Users/default-user-image.jpeg",
	                                "confirmed_email": true,
	                                "confirmed_phone": false,
	                                "created_at": "2021-10-21T15:38:07.599042Z",
	                                "updated_at": "2021-10-22T10:52:18.483765Z"
	                            },
	                            "numbers": null,
	                            "links": null,
	                            "created_at": "2021-10-21T15:45:34.434734Z",
	                            "updated_at": "2021-10-21T15:45:34.434767Z"
	                        },
	                        "created_at": "2021-10-21T15:46:42.682220Z",
	                        "updated_at": "2021-10-21T15:46:42.682258Z"
	                    },
	                    "category": {
	                        "id": 1,
	                        "name": "Phone",
	                        "created_at": "2021-10-25T08:14:57.130029Z",
	                        "updated_at": "2021-10-25T08:14:57.130065Z"
	                    },
	                    "created_at": "2021-10-25T16:17:57.120771Z",
	                    "updated_at": "2021-10-25T16:32:58.473126Z"
	                }
	            ],
	            "order": {
	                "id": 1,
	                "order_code": "eawtt",
	                "description": "retw4bt54t43",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "executor": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "client": 1,
	                "done": false,
	                "service": {
	                    "id": 1,
	                    "name": "Test",
	                    "address": "Test",
	                    "phone": "+79999999999",
	                    "organization": {
	                        "id": 1,
	                        "name": "Test",
	                        "description": "Test",
	                        "address": "Test",
	                        "creator": {
	                            "id": 1,
	                            "surname": "a",
	                            "name": "a",
	                            "second_name": "a",
	                            "address": "a",
	                            "email": "a@gmail.com",
	                            "phone": null,
	                            "image": "../static/Users/default-user-image.jpeg",
	                            "confirmed_email": true,
	                            "confirmed_phone": false,
	                            "created_at": "2021-10-21T15:38:07.599042Z",
	                            "updated_at": "2021-10-22T10:52:18.483765Z"
	                        },
	                        "numbers": null,
	                        "links": null,
	                        "created_at": "2021-10-21T15:45:34.434734Z",
	                        "updated_at": "2021-10-21T15:45:34.434767Z"
	                    },
	                    "created_at": "2021-10-21T15:46:42.682220Z",
	                    "updated_at": "2021-10-21T15:46:42.682258Z"
	                },
	                "order_status": 1,
	                "created_at": "2021-10-21T15:54:30.332013Z",
	                "updated_at": "2021-10-21T15:54:30.332050Z",
	                "device_type": "rer",
	                "device_maker": "werwer",
	                "device_model": "werwerewrwe",
	                "device_kit": "",
	                "device_appearance": "",
	                "device_defect": ""
	            },
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "created_at": "2021-10-25T17:22:07.109240Z",
	            "updated_at": "2021-10-25T17:22:07.109277Z"
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "created_at": "2021-10-25T17:34:49.339012Z",
	        "updated_at": "2021-10-25T17:34:49.362932Z"
	    }
	]
	```   
* **PUT** `sale-order-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "cash": [
	        "This field is required."
	    ],
	    "card": [
	        "This field is required."
	    ],
	    "bank_transfer": [
	        "This field is required."
	    ],
	    "discount": [
	        "This field is required."
	    ],
	    "cashbox": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	Also you can add client field in request body     
	**Input data**      
	```json   
	{
	    "organization":1,
	    "cash":"20.00",
	    "card":0,
	    "bank_transfer":0,
	    "discount":"0",
	    "cashbox":1,
	    "service":1,
	    "product_order":9
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "cash":"20.00",
	    "card":0,
	    "bank_transfer":0,
	    "discount":"0",
	    "cashbox":1,
	    "service":1,
	    "product_order":9
	}
	```  
* **PATCH** `sale-order-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "cash": "20.00",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "cashbox": 1,
	    "service": 1
	}
	```   
	**Input data**      
	```json  
	{
	    "cash": "30.00",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "cashbox": 1,
	    "service": 1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "cash": "30.00",
	    "card": "0.00",
	    "bank_transfer": "0.00",
	    "discount": "0.00",
	    "client": null,
	    "cashbox": 1,
	    "service": 1
	}
	```  
* **DELETE** `sale-order-ud/1/`  
	**Input data**  
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `sale-product-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
	{
        "id": 1,
        "cash": "30.00",
        "card": "0.00",
        "bank_transfer": "0.00",
        "discount": "0.00",
        "client": null,
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "cashbox": {
            "id": 1,
            "name": "Cashbox",
            "cash": "53.00",
            "account_money": "10.00",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "created_at": "2021-10-25T09:38:44.934208Z",
            "updated_at": "2021-10-25T17:34:49.358778Z"
        },
        "product_order": {
            "id": 9,
            "name": "Test4",
            "price": "30.00",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "products": [
                {
                    "id": 5,
                    "name": "Org2product",
                    "code": "574426714052815",
                    "barcode": "574426714845097",
                    "purchase_price": "10.00",
                    "sale_price": "10.00",
                    "count": 3,
                    "supplier": "Test2",
                    "irreducible_balance": "0.00",
                    "organization": {
                        "id": 1,
                        "name": "Test",
                        "description": "Test",
                        "address": "Test",
                        "creator": {
                            "id": 1,
                            "surname": "a",
                            "name": "a",
                            "second_name": "a",
                            "address": "a",
                            "email": "a@gmail.com",
                            "phone": null,
                            "image": "../static/Users/default-user-image.jpeg",
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-21T15:38:07.599042Z",
                            "updated_at": "2021-10-22T10:52:18.483765Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-21T15:45:34.434734Z",
                        "updated_at": "2021-10-21T15:45:34.434767Z"
                    },
                    "service": {
                        "id": 1,
                        "name": "Test",
                        "address": "Test",
                        "phone": "+79999999999",
                        "organization": {
                            "id": 1,
                            "name": "Test",
                            "description": "Test",
                            "address": "Test",
                            "creator": {
                                "id": 1,
                                "surname": "a",
                                "name": "a",
                                "second_name": "a",
                                "address": "a",
                                "email": "a@gmail.com",
                                "phone": null,
                                "image": "../static/Users/default-user-image.jpeg",
                                "confirmed_email": true,
                                "confirmed_phone": false,
                                "created_at": "2021-10-21T15:38:07.599042Z",
                                "updated_at": "2021-10-22T10:52:18.483765Z"
                            },
                            "numbers": null,
                            "links": null,
                            "created_at": "2021-10-21T15:45:34.434734Z",
                            "updated_at": "2021-10-21T15:45:34.434767Z"
                        },
                        "created_at": "2021-10-21T15:46:42.682220Z",
                        "updated_at": "2021-10-21T15:46:42.682258Z"
                    },
                    "category": {
                        "id": 1,
                        "name": "Phone",
                        "created_at": "2021-10-25T08:14:57.130029Z",
                        "updated_at": "2021-10-25T08:14:57.130065Z"
                    },
                    "created_at": "2021-10-25T13:26:32.306469Z",
                    "updated_at": "2021-10-25T16:32:58.474888Z"
                },
                {
                    "id": 9,
                    "name": "Test item",
                    "code": "tryukhjbmgftryukmnbg",
                    "barcode": "wt4eyuiykj",
                    "purchase_price": "10.00",
                    "sale_price": "2.00",
                    "count": 3,
                    "supplier": "I",
                    "irreducible_balance": "0.00",
                    "organization": {
                        "id": 1,
                        "name": "Test",
                        "description": "Test",
                        "address": "Test",
                        "creator": {
                            "id": 1,
                            "surname": "a",
                            "name": "a",
                            "second_name": "a",
                            "address": "a",
                            "email": "a@gmail.com",
                            "phone": null,
                            "image": "../static/Users/default-user-image.jpeg",
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-21T15:38:07.599042Z",
                            "updated_at": "2021-10-22T10:52:18.483765Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-21T15:45:34.434734Z",
                        "updated_at": "2021-10-21T15:45:34.434767Z"
                    },
                    "service": {
                        "id": 1,
                        "name": "Test",
                        "address": "Test",
                        "phone": "+79999999999",
                        "organization": {
                            "id": 1,
                            "name": "Test",
                            "description": "Test",
                            "address": "Test",
                            "creator": {
                                "id": 1,
                                "surname": "a",
                                "name": "a",
                                "second_name": "a",
                                "address": "a",
                                "email": "a@gmail.com",
                                "phone": null,
                                "image": "../static/Users/default-user-image.jpeg",
                                "confirmed_email": true,
                                "confirmed_phone": false,
                                "created_at": "2021-10-21T15:38:07.599042Z",
                                "updated_at": "2021-10-22T10:52:18.483765Z"
                            },
                            "numbers": null,
                            "links": null,
                            "created_at": "2021-10-21T15:45:34.434734Z",
                            "updated_at": "2021-10-21T15:45:34.434767Z"
                        },
                        "created_at": "2021-10-21T15:46:42.682220Z",
                        "updated_at": "2021-10-21T15:46:42.682258Z"
                    },
                    "category": {
                        "id": 1,
                        "name": "Phone",
                        "created_at": "2021-10-25T08:14:57.130029Z",
                        "updated_at": "2021-10-25T08:14:57.130065Z"
                    },
                    "created_at": "2021-10-25T16:17:57.120771Z",
                    "updated_at": "2021-10-25T16:32:58.473126Z"
                }
            ],
            "order": {
                "id": 1,
                "order_code": "eawtt",
                "description": "retw4bt54t43",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "executor": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "client": 1,
                "done": false,
                "service": {
                    "id": 1,
                    "name": "Test",
                    "address": "Test",
                    "phone": "+79999999999",
                    "organization": {
                        "id": 1,
                        "name": "Test",
                        "description": "Test",
                        "address": "Test",
                        "creator": {
                            "id": 1,
                            "surname": "a",
                            "name": "a",
                            "second_name": "a",
                            "address": "a",
                            "email": "a@gmail.com",
                            "phone": null,
                            "image": "../static/Users/default-user-image.jpeg",
                            "confirmed_email": true,
                            "confirmed_phone": false,
                            "created_at": "2021-10-21T15:38:07.599042Z",
                            "updated_at": "2021-10-22T10:52:18.483765Z"
                        },
                        "numbers": null,
                        "links": null,
                        "created_at": "2021-10-21T15:45:34.434734Z",
                        "updated_at": "2021-10-21T15:45:34.434767Z"
                    },
                    "created_at": "2021-10-21T15:46:42.682220Z",
                    "updated_at": "2021-10-21T15:46:42.682258Z"
                },
                "order_status": 1,
                "created_at": "2021-10-21T15:54:30.332013Z",
                "updated_at": "2021-10-21T15:54:30.332050Z",
                "device_type": "rer",
                "device_maker": "werwer",
                "device_model": "werwerewrwe",
                "device_kit": "",
                "device_appearance": "",
                "device_defect": ""
            },
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "created_at": "2021-10-25T17:22:07.109240Z",
            "updated_at": "2021-10-25T17:22:07.109277Z"
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "created_at": "2021-10-25T17:34:49.339012Z",
        "updated_at": "2021-10-25T17:34:49.362932Z"
    }
	```    
## **WorkDone**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `work-done-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
	    "name": [
	        "This field is required."
	    ],
	    "price": [
	        "This field is required."
	    ],
	    "user": [
	        "This field is required."
	    ],
	    "order": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```
	Also you can add service_price field in request body     
	**Input data**     
	```json  
	{
	    "organization":1,
	    "name":"TestOrder",
	    "price":30.0,
	    "user":1,
	    "order":1,
	    "service":1
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "organization":1,
	    "name":"TestOrder",
	    "price":30.0,
	    "user":1,
	    "order":1,
	    "service":1,
	    "service_price": null,
	}
	```  
* **GET** `work-done-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "TestOrder",
	        "price": "30.00",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "numbers": null,
	            "links": null,
	            "created_at": "2021-10-21T15:45:34.434734Z",
	            "updated_at": "2021-10-21T15:45:34.434767Z"
	        },
	        "service_price": null,
	        "user": {
	            "id": 1,
	            "surname": "a",
	            "name": "a",
	            "second_name": "a",
	            "address": "a",
	            "email": "a@gmail.com",
	            "phone": null,
	            "image": "../static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-10-21T15:38:07.599042Z",
	            "updated_at": "2021-10-22T10:52:18.483765Z"
	        },
	        "order": {
	            "id": 1,
	            "order_code": "eawtt",
	            "description": "retw4bt54t43",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "executor": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "../static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-10-21T15:38:07.599042Z",
	                "updated_at": "2021-10-22T10:52:18.483765Z"
	            },
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "client": 1,
	            "done": false,
	            "service": {
	                "id": 1,
	                "name": "Test",
	                "address": "Test",
	                "phone": "+79999999999",
	                "organization": {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "image": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                },
	                "created_at": "2021-10-21T15:46:42.682220Z",
	                "updated_at": "2021-10-21T15:46:42.682258Z"
	            },
	            "order_status": 1,
	            "created_at": "2021-10-21T15:54:30.332013Z",
	            "updated_at": "2021-10-21T15:54:30.332050Z",
	            "device_type": "rer",
	            "device_maker": "werwer",
	            "device_model": "werwerewrwe",
	            "device_kit": "",
	            "device_appearance": "",
	            "device_defect": ""
	        },
	        "service": {
	            "id": 1,
	            "name": "Test",
	            "address": "Test",
	            "phone": "+79999999999",
	            "organization": {
	                "id": 1,
	                "name": "Test",
	                "description": "Test",
	                "address": "Test",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "second_name": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "../static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-10-21T15:38:07.599042Z",
	                    "updated_at": "2021-10-22T10:52:18.483765Z"
	                },
	                "numbers": null,
	                "links": null,
	                "created_at": "2021-10-21T15:45:34.434734Z",
	                "updated_at": "2021-10-21T15:45:34.434767Z"
	            },
	            "created_at": "2021-10-21T15:46:42.682220Z",
	            "updated_at": "2021-10-21T15:46:42.682258Z"
	        },
	        "created_at": "2021-10-25T18:02:35.783255Z",
	        "updated_at": "2021-10-25T18:02:35.783296Z"
	    }
	]
	```   
* **PUT** `work-done-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	    "price": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	Also you can add service_price field in request body     
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"ChangedName",
	    "price":35.00,
	    "service":1
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "ChangedName",
	    "price": "35.00",
	    "service_price": null,
	    "service": 1
	}
	```  
* **PATCH** `work-done-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "ChangedName",
	    "price": "35.00",
	    "service_price": null,
	    "service": 1
	}
	```   
	**Input data**      
	```json  
	{
		"organization":1,
	    "name": "Name",
	    "price": "35.00",
	    "service_price": null,
	    "service": 1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "Name",
	    "price": "35.00",
	    "service_price": null,
	    "service": 1
	}
	```  
* **DELETE** `work-done-ud/1/`  
	**Input data**  
	```json   
	{     
		"organization":1
	}  
	```     
	**Response**    
	*`Response 204`*   
	```json   
	{
	}
	```  
* **GET** `work-done-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "TestOrder",
        "price": "30.00",
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "numbers": null,
            "links": null,
            "created_at": "2021-10-21T15:45:34.434734Z",
            "updated_at": "2021-10-21T15:45:34.434767Z"
        },
        "service_price": null,
        "user": {
            "id": 1,
            "surname": "a",
            "name": "a",
            "second_name": "a",
            "address": "a",
            "email": "a@gmail.com",
            "phone": null,
            "image": "../static/Users/default-user-image.jpeg",
            "confirmed_email": true,
            "confirmed_phone": false,
            "created_at": "2021-10-21T15:38:07.599042Z",
            "updated_at": "2021-10-22T10:52:18.483765Z"
        },
        "order": {
            "id": 1,
            "order_code": "eawtt",
            "description": "retw4bt54t43",
            "creator": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "executor": {
                "id": 1,
                "surname": "a",
                "name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "image": "../static/Users/default-user-image.jpeg",
                "confirmed_email": true,
                "confirmed_phone": false,
                "created_at": "2021-10-21T15:38:07.599042Z",
                "updated_at": "2021-10-22T10:52:18.483765Z"
            },
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "client": 1,
            "done": false,
            "service": {
                "id": 1,
                "name": "Test",
                "address": "Test",
                "phone": "+79999999999",
                "organization": {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "image": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                },
                "created_at": "2021-10-21T15:46:42.682220Z",
                "updated_at": "2021-10-21T15:46:42.682258Z"
            },
            "order_status": 1,
            "created_at": "2021-10-21T15:54:30.332013Z",
            "updated_at": "2021-10-21T15:54:30.332050Z",
            "device_type": "rer",
            "device_maker": "werwer",
            "device_model": "werwerewrwe",
            "device_kit": "",
            "device_appearance": "",
            "device_defect": ""
        },
        "service": {
            "id": 1,
            "name": "Test",
            "address": "Test",
            "phone": "+79999999999",
            "organization": {
                "id": 1,
                "name": "Test",
                "description": "Test",
                "address": "Test",
                "creator": {
                    "id": 1,
                    "surname": "a",
                    "name": "a",
                    "second_name": "a",
                    "address": "a",
                    "email": "a@gmail.com",
                    "phone": null,
                    "image": "../static/Users/default-user-image.jpeg",
                    "confirmed_email": true,
                    "confirmed_phone": false,
                    "created_at": "2021-10-21T15:38:07.599042Z",
                    "updated_at": "2021-10-22T10:52:18.483765Z"
                },
                "numbers": null,
                "links": null,
                "created_at": "2021-10-21T15:45:34.434734Z",
                "updated_at": "2021-10-21T15:45:34.434767Z"
            },
            "created_at": "2021-10-21T15:46:42.682220Z",
            "updated_at": "2021-10-21T15:46:42.682258Z"
        },
        "created_at": "2021-10-25T18:02:35.783255Z",
        "updated_at": "2021-10-25T18:02:35.783296Z"
    }
	```    