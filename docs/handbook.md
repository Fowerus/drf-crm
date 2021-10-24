# **Organizations API documentation** - **`/handbook/`**   


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


## **DeviceType**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **POST** `device-type-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
			"This field is required."
		],
		"description": [
			"This field is required"
		]
	}
	```   
	**Input data**     
	```json  
	{
	    "organization":1,
	    "name":"Iphone",
	    "description":"10"
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Iphone",
	    "description": "10",
	    "organization": 1
	}
	```  
* **GET** `device-type-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Iphone",
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
	        "description": "10",
	        "created_at": "2021-10-24T12:04:18.900775Z",
	        "updated_at": "2021-10-24T12:04:18.900826Z"
	    }
	]
	```   
* **PUT** `device-type-ud/1/`    
	**Empty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
		"name": [
			"This field is required."
		],
		"description": [
			"This field is required."
		]
	}
	```   
	**Input data**      
	```json   
	{
	    "organization":1,
	    "name":"Iphone2",
	    "description":"102"
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Iphone2",
	    "description": "102"
	}
	```  
* **PATCH** `device-type-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "Iphone2",
	    "description": "102"
	}
	```   
	**Input data**      
	```json  
	{
		"organization":1,
	    "name": "Iphone",
	    "description": "10"
	} 
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "Iphone",
	    "description": "10"
	}
	```  
* **DELETE** `device-type-ud/1/`  
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
* **GET** `device-type-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "id": 1,
	    "name": "Iphone",
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
	    "description": "10",
	    "created_at": "2021-10-24T12:04:18.900775Z",
	    "updated_at": "2021-10-24T12:14:35.064056Z"
	}
	```  
## **DeviceMaker**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **POST** `device-maker-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
			"This field is required."
		]	
	}
	```   
	**Input data**     
	```json  
	{
	    "organization":1,
	    "name":"Android",
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Android",

	}
	```  
* **GET** `device-maker-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Android",
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
	        "created_at": "2021-10-24T12:28:45.351884Z",
	        "updated_at": "2021-10-24T12:28:45.351920Z"
	    }
	]
	```   
* **PUT** `device-maker-ud/1/`    
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
	    "name":"Android2",
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Android2",
	}
	```  
* **PATCH** `device-maker-ud/1/`   
	**Empty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
	    "name": "Android2",
	}
	```   
	**Input data**      
	```json  
	{
		"organization":1,
	    "name": "Android",
	} 
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "name": "Android",
	}
	```  
* **DELETE** `device-maker-ud/1/`  
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
* **GET** `device-maker-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Android",
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
        "created_at": "2021-10-24T12:28:45.351884Z",
        "updated_at": "2021-10-24T12:28:45.351920Z"
    }
	```  

## **DeviceMaker**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **POST** `device-model-c/`        
	**Empty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
			"This field is required."
		]	
	}
	```   
	**Input data**     
	```json  
	{
	    "name": "Printer",
	    "organization": 1
	}
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
	    "name": "Printer",
	    "organization": 1
	}
	```  
* **GET** `device-model-l/1/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
	    {
	        "id": 1,
	        "name": "Printer",
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
	        "created_at": "2021-10-24T12:35:32.761255Z",
	        "updated_at": "2021-10-24T12:35:32.761315Z"
	    }
	]
	```   
* **PUT** `device-model-ud/1/`    
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
	    "name":"Printer2",
	}
	```   
	**Response**   
	*`Response 200`*  
	```json  
	{
	    "name": "Printer2",
	}
	```  
* **PATCH** `device-model-ud/1/`   
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
* **GET** `device-model-r/1/1/`   
	**Response**  
	*`Response 200`*  
	```json  
    {
        "id": 1,
        "name": "Printer",
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
        "created_at": "2021-10-24T12:35:32.761255Z",
        "updated_at": "2021-10-24T12:35:32.761315Z"
    }
	```  
## **DeviceKit**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
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
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
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
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
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
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
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