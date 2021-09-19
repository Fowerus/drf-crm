# **Orders API documentation** - **`/orders/`**   


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

## **Orders**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **POST** `order-c/`    
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to create the order, it will issue   
	**Input data**  
	```json  
	{
		"organization":1
	}
	```  
	**Response**  
	*`Response 400`*  
	```json   
	{
	    "description": [
	        "This field is required."
	    ],
	    "creator": [
	        "This field is required."
	    ],
	    "executor": [
	        "This field is required."
	    ],
	    "client": [
	        "This field is required."
	    ],
	    "service": [
	        "This field is required."
	    ]
	}
	```   
	The correct request   
	**Input data**  
	```json   
	{
		"description":"New order",
		"organization":1,
		"creator":5,
		"executor":5,
		"client":1,
		"service":1
	}
	```  
	**Response**  
	*`Response 201`*  
	```json  
	{
	    "description": "New order",
	    "creator": 5,
	    "executor": 5,
	    "client": 1,
	    "service": 1,
	    "organization": 1
	}
	```  
* **GET** `order-l/1/`  
	**Response**   
	*`Response 200`*   
	```json  
	[
	    {
	        "id": 1,
	        "order_code": 249119676806814,
	        "description": "New order",
	        "creator": {
	            "id": 5,
	            "surname": "user3",
	            "name": "user3",
	            "patronymic": "user3",
	            "address": "user3address",
	            "email": "user3@gmail.com",
	            "phone": "+79137779135",
	            "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "executor": {
	            "id": 5,
	            "surname": "user3",
	            "name": "user3",
	            "patronymic": "user3",
	            "address": "user3address",
	            "email": "user3@gmail.com",
	            "phone": "+79137779135",
	            "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "organization": {
	            "id": 1,
	            "name": "Organization2",
	            "description": "Organization2",
	            "address": "Organization2",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "patronymic": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	                "confirmed_email": false,
	                "confirmed_phone": false,
	                "created_at": "2021-09-08T12:03:41.729216Z",
	                "updated_at": "2021-09-08T12:03:41.729257Z"
	            },
	            "created_at": "2021-09-08T15:13:41.218868Z",
	            "numbers": {
	                "main": "+79999999999"
	            },
	            "links": {
	                "vk": "vk.com"
	            },
	            "updated_at": "2021-09-09T03:03:04.127339Z"
	        },
	        "client": 1,
	        "done": false,
	        "service": {
	            "id": 1,
	            "name": "Programming",
	            "address": "Gdeto v rossii",
	            "phone": "+79518472961",
	            "organization": {
	                "id": 1,
	                "name": "Organization2",
	                "description": "Organization2",
	                "address": "Organization2",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "patronymic": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	                    "confirmed_email": false,
	                    "confirmed_phone": false,
	                    "created_at": "2021-09-08T12:03:41.729216Z",
	                    "updated_at": "2021-09-08T12:03:41.729257Z"
	                },
	                "created_at": "2021-09-08T15:13:41.218868Z",
	                "numbers": {
	                    "main": "+79999999999"
	                },
	                "links": {
	                    "vk": "vk.com"
	                },
	                "updated_at": "2021-09-09T03:03:04.127339Z"
	            },
	            "created_at": "2021-09-09T03:37:35.341485Z",
	            "updated_at": "2021-09-09T03:40:40.333245Z"
	        },
	        "created_at": "2021-09-09T04:52:27.731903Z",
	        "updated_at": "2021-09-09T04:58:12.789112Z"
	    }
	]
	```  
* **GET** `order-creator-l/1/`  
	**Response**   
	*`Response 200`*   
	```json  
	[
	    {
	        "id": 1,
	        "order_code": 249119676806814,
	        "description": "New order",
	        "creator": {
	            "id": 5,
	            "surname": "user3",
	            "name": "user3",
	            "patronymic": "user3",
	            "address": "user3address",
	            "email": "user3@gmail.com",
	            "phone": "+79137779135",
	            "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "executor": {
	            "id": 5,
	            "surname": "user3",
	            "name": "user3",
	            "patronymic": "user3",
	            "address": "user3address",
	            "email": "user3@gmail.com",
	            "phone": "+79137779135",
	            "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "organization": {
	            "id": 1,
	            "name": "Organization2",
	            "description": "Organization2",
	            "address": "Organization2",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "patronymic": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	                "confirmed_email": false,
	                "confirmed_phone": false,
	                "created_at": "2021-09-08T12:03:41.729216Z",
	                "updated_at": "2021-09-08T12:03:41.729257Z"
	            },
	            "created_at": "2021-09-08T15:13:41.218868Z",
	            "numbers": {
	                "main": "+79999999999"
	            },
	            "links": {
	                "vk": "vk.com"
	            },
	            "updated_at": "2021-09-09T03:03:04.127339Z"
	        },
	        "client": 1,
	        "done": false,
	        "service": {
	            "id": 1,
	            "name": "Programming",
	            "address": "Gdeto v rossii",
	            "phone": "+79518472961",
	            "organization": {
	                "id": 1,
	                "name": "Organization2",
	                "description": "Organization2",
	                "address": "Organization2",
	                "creator": {
	                    "id": 1,
	                    "surname": "a",
	                    "name": "a",
	                    "patronymic": "a",
	                    "address": "a",
	                    "email": "a@gmail.com",
	                    "phone": null,
	                    "image": "host/orders/order-l/1/static/Users/default-user-image.jpeg",
	                    "confirmed_email": false,
	                    "confirmed_phone": false,
	                    "created_at": "2021-09-08T12:03:41.729216Z",
	                    "updated_at": "2021-09-08T12:03:41.729257Z"
	                },
	                "created_at": "2021-09-08T15:13:41.218868Z",
	                "numbers": {
	                    "main": "+79999999999"
	                },
	                "links": {
	                    "vk": "vk.com"
	                },
	                "updated_at": "2021-09-09T03:03:04.127339Z"
	            },
	            "created_at": "2021-09-09T03:37:35.341485Z",
	            "updated_at": "2021-09-09T03:40:40.333245Z"
	        },
	        "created_at": "2021-09-09T04:52:27.731903Z",
	        "updated_at": "2021-09-09T04:58:12.789112Z"
	    }
	]
	```  
* **GET** `order-r/1/`   
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "id": 1,
	    "order_code": 249119676806814,
	    "description": "Description",
	    "creator": {
	        "id": 5,
	        "surname": "user3",
	        "name": "user3",
	        "patronymic": "user3",
	        "address": "user3address",
	        "email": "user3@gmail.com",
	        "phone": "+79137779135",
	        "image": "http://127.0.0.1:8000/orders/order-r/1/1/static/Users/default-user-image.jpeg",
	        "confirmed_email": true,
	        "confirmed_phone": false,
	        "created_at": "2021-09-08T12:22:26.072030Z",
	        "updated_at": "2021-09-08T15:11:20.864802Z"
	    },
	    "executor": {
	        "id": 5,
	        "surname": "user3",
	        "name": "user3",
	        "patronymic": "user3",
	        "address": "user3address",
	        "email": "user3@gmail.com",
	        "phone": "+79137779135",
	        "image": "http://127.0.0.1:8000/orders/order-r/1/1/static/Users/default-user-image.jpeg",
	        "confirmed_email": true,
	        "confirmed_phone": false,
	        "created_at": "2021-09-08T12:22:26.072030Z",
	        "updated_at": "2021-09-08T15:11:20.864802Z"
	    },
	    "organization": {
	        "id": 1,
	        "name": "Organization2",
	        "description": "Organization2",
	        "address": "Organization2",
	        "creator": {
	            "id": 1,
	            "surname": "a",
	            "name": "a",
	            "patronymic": "a",
	            "address": "a",
	            "email": "a@gmail.com",
	            "phone": null,
	            "image": "http://127.0.0.1:8000/orders/order-r/1/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": false,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:03:41.729216Z",
	            "updated_at": "2021-09-08T12:03:41.729257Z"
	        },
	        "created_at": "2021-09-08T15:13:41.218868Z",
	        "numbers": {
	            "main": "+79999999999"
	        },
	        "links": {
	            "vk": "vk.com"
	        },
	        "updated_at": "2021-09-09T03:03:04.127339Z"
	    },
	    "client": 1,
	    "done": false,
	    "service": {
	        "id": 1,
	        "name": "Programming",
	        "address": "Gdeto v rossii",
	        "phone": "+79518472961",
	        "organization": {
	            "id": 1,
	            "name": "Organization2",
	            "description": "Organization2",
	            "address": "Organization2",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "name": "a",
	                "patronymic": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "image": "http://127.0.0.1:8000/orders/order-r/1/1/static/Users/default-user-image.jpeg",
	                "confirmed_email": false,
	                "confirmed_phone": false,
	                "created_at": "2021-09-08T12:03:41.729216Z",
	                "updated_at": "2021-09-08T12:03:41.729257Z"
	            },
	            "created_at": "2021-09-08T15:13:41.218868Z",
	            "numbers": {
	                "main": "+79999999999"
	            },
	            "links": {
	                "vk": "vk.com"
	            },
	            "updated_at": "2021-09-09T03:03:04.127339Z"
	        },
	        "created_at": "2021-09-09T03:37:35.341485Z",
	        "updated_at": "2021-09-09T03:40:40.333245Z"
	    },
	    "created_at": "2021-09-09T04:52:27.731903Z",
	    "updated_at": "2021-09-09T05:07:29.852934Z"
	}
	```  

* **PUT** `order-ud/1/`  
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to change the order, it will issue   
	**Input data**  
	```json  
	{
		"organization":1
	}
	```  
	**Response**  
	*`Response 400`*  
	```json   
	{
	    "description": [
	        "This field is required."
	    ],
	    "executor": [
	        "This field is required."
	    ]
	}
	```   
	The correct request   
	**Input data**  
	```json  
	{
	    "description": "Changed descr",
	    "executor": 2,
	    "organization":1
	}
	```  
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "description": "Changed descr",
	    "executor": 2
	}
	```  
* **PATCH** `order-ud/1/`  
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to change the order, it will issue   

	**Input data**  
	```json  
	{
		"organization":1
	}
	```  
	**Response**  
	*`Response 200`*  
	```json   
	{
	    "description": "Changed descr",
	    "executor": 2
	}
	```   
	The correct request    
	**Input data**  
	```json  
	{
	    "description": "Description",
	    "executor": 5,
	    "organization":1
	}
	```  
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "description": "Description",
	    "executor": 5
	}
	```  
* **DELETE** `order-ud/1/`   
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to delete the order, it will issue  
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