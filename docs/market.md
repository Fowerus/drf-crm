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
	    "account_money":"50.00",
	    "service":1
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Cashbox",
	    "cash": "3.00",
	    "account_money": "50.00",
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
	    "cash":"1.00",
	    "account_money":"30.00",
	    "service":1,
	    "prefix":"-"
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Cashbox2",
	    "cash": "0.00",
	    "account_money": "10.00",
	    "service": 1,
	    "prefix": "-"
	}
	```  
	**Transaction**   
	*`Response 200`*  
	```json  
	{
	    "cashbox": 1,
	    "organization":1,
	    "sale_product":null,
	    "sale_order":null,
	    "purcahse": null,
	    "data": {
	    	"cash": "-3.0", 
	    	"user": {"name": "a2", "email": "a2@gmail.com", "phone": null, "surname": "a2", "user_id": 2, "second_name": "a2"},
	    	"account_money": "-10.0"
	    }
	}
	```  
* **PATCH** `cashbox-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "Printer2",
	}
	```   
	**Input data**      
	```json  
	{
		"organization":1,
	    "name": "Printer",
	} 
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "Printer",
	}
	```  
* **DELETE** `device-model-ud/1/`  
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
        "updated_at": "2021-10-25T09:38:44.934246Z"
    }
	```  
## **DeviceKit**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `device-kit-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
		    "This field is required."
		],
		"device_type": [
		    "This field is required."
		]	
	}
	```   
	**Input data**     
	```json  
	{
	    "name": "Kit",
	    "organization": 1,
	    "device_type": 2
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Kit",
	    "organization": 1,
	    "device_type": 2
	}
	```  
* **GET** `device-kit-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Kit",
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
	        "device_type": {
	            "id": 2,
	            "name": "ForKit",
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
	            "description": "ForKit",
	            "created_at": "2021-10-24T12:38:56.867071Z",
	            "updated_at": "2021-10-24T12:38:56.867107Z"
	        },
	        "created_at": "2021-10-24T12:53:48.685192Z",
	        "updated_at": "2021-10-24T12:53:48.685229Z"
	    }
	]
	```   
* **PUT** `device-kit-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	    "devicetype": [
	        "This field is required."
	    ]
	}
	```   
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"Kit2",
	    "devicetype":2
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "organization":1,
	    "name":"Kit2",
	    "devicetype":2
	}
	```  
* **PATCH** `device-kit-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "Kit2",
	    "devicetype": 2
	}
	```   
	**Input data**      
	```json  
	{
	    "organization":1,
	    "name":"Kit",
	    "devicetype":2
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name":"Kit",
	    "devicetype":2
	}
	```  
* **DELETE** `device-kit-ud/1/`  
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
* **GET** `device-kit-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Kit",
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
        "device_type": {
            "id": 2,
            "name": "ForKit",
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
            "description": "ForKit",
            "created_at": "2021-10-24T12:38:56.867071Z",
            "updated_at": "2021-10-24T12:38:56.867107Z"
        },
        "created_at": "2021-10-24T12:53:48.685192Z",
        "updated_at": "2021-10-24T12:53:48.685229Z"
    }
	```  
## **DeviceAppearance**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `device-appearance-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
		    "This field is required."
		],
	}
	```   
	**Input data**     
	```json  
	{
	    "name": "Appearance",
	    "organization": 1,
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Appearance",
	}
	```  
* **GET** `device-appearance-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Appearance",
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
	        "created_at": "2021-10-24T13:38:34.216266Z",
	        "updated_at": "2021-10-24T13:38:34.216302Z"
	    }
	]
	```   
* **PUT** `device-appearance-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	}
	```   
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"Appearance2",
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name":"Appearance2",
	}
	```  
* **PATCH** `device-appearance-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
		"name":"Appearance2",
	}
	```   
	**Input data**      
	```json  
	{
 		"name":"Appearance",
 		"organization":1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name":"Appearance2"
	}
	```  
* **DELETE** `device-appearance-ud/1/`  
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
* **GET** `device-appearance-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Appearance",
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
        "created_at": "2021-10-24T13:38:34.216266Z",
        "updated_at": "2021-10-24T13:38:34.216302Z"
    }
	```  
## **DeviceDefect**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `device-defect-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
		    "This field is required."
		],
	}
	```   
	**Input data**     
	```json  
	{
	    "name": "Defect",
	    "organization": 1,
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Defect",
	}
	```  
* **GET** `device-defect-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Defect",
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
	        "created_at": "2021-10-24T14:10:41.272535Z",
	        "updated_at": "2021-10-24T14:10:41.272578Z"
	    }
	]
	```   
* **PUT** `device-defect-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
	    "name": [
	        "This field is required."
	    ],
	}
	```   
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"Defect2"
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "organization":1,
	    "name":"Defect2"
	}
	```  
* **PATCH** `device-defect-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
		"name":"Defect2",
	}
	```   
	**Input data**      
	```json  
	{
 		"name":"Defect",
 		"organization":1
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name":"Defect"
	}
	```  
* **DELETE** `device-defect-ud/1/`  
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
* **GET** `device-defect-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Defect",
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
        "created_at": "2021-10-24T14:10:41.272535Z",
        "updated_at": "2021-10-24T14:10:41.272578Z"
    }
	```

## **ServicePrice**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTk5MjY4LCJqdGkiOiI1NmUwNjk2Yjc1MGE0MTI2YTNkZmM1ODUyMmMyMDJhOSIsInVzZXJfaWQiOjIsIm5hbWUiOiJhMiIsInN1cm5hbWUiOiJhMiIsInNlY29uZF9uYW1lIjoiYTIiLCJlbWFpbCI6ImEyQGdtYWlsLmNvbSIsInBob25lIjpudWxsfQ.pe7Khwh-kMwXx9uOZ5esoAJf4Bi-vUhsr-GE800UApc"
}
```  
* **POST** `service-price-c/`        
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
	    ]
	}
	```   
	**Input data**     
	```json  
	{
	    "name": "ServicePrice",
	    "organization": 1,
	    "price": 20.0
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "ServicePrice",
	    "organization": 1,
	    "price": 20.0
	}
	```  
* **GET** `service-price-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "ServicePrice",
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
	        "price": 20.0,
	        "created_at": "2021-10-24T14:31:50.294391Z",
	        "updated_at": "2021-10-24T14:31:50.294443Z"
	    }
	]
	```   
* **PUT** `service-price-ud/1/`    
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
	    ]
	}
	```   
	**Input data**      
	```json   
	{
	    "name": "ServicePrice2",
	    "organization": 1,
	    "price": 20.02
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
* **PATCH** `service-price-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "ServicePrice2",
	    "price": 20.02
	}
	```   
	**Input data**      
	```json  
	{
		"organization":1,
	    "name": "ServicePrice",
	    "price": 20.02
	}
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "ServicePrice",
	    "price": 20.0
	}
	```  
* **DELETE** `service-price-ud/1/`  
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
* **GET** `service-price-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "ServicePrice",
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
        "price": 20.0,
        "created_at": "2021-10-24T14:31:50.294391Z",
        "updated_at": "2021-10-24T14:31:50.294443Z"
    }

	```    