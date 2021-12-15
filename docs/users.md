# **Users API documentation** - **`/users/`**   


## **Registration**  
**Headers**  
```json  
{
	"Content-Type":"application/json"
}
``` 
* **POST** `auth/registration/`     
	**Empty request data**  
	The same Response will be in case of some data incorrectness  
	**Response** 
	*`Response 400`*  
	```json  
	{
		"detail": "Valid phone number or email not provided"
	}
	```  
	In the input data, you can specify a phone number or email address, or all together   
	**Input data**     
	```json  
	{  
		"surname":"user1",   
		"first_name":"user1",    
		"second_name":"user1",  
		"address":"user1address",
		"email":"user1@gmail.com",
		"phone":"+79967348137",
		"password":"user1user1"  
	}  
	```  
	If the registration took place, for example, by a phone number, then the e-mail address will not be indicated in the Response (Also about the e-mail address). The password is also not included in the Response from the server   
	**Response**  
	*`Response 201`*    
	```json  
	{
		"surname": "user1",
		"first_name": "user1",
		"second_name": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137"
	}
	```  

## **TokenObtainPair**  
* **POST**  `auth/token/`     
	**Headers**  
	```json  
	{
		"Content-Type":"application/json",
		"User-Agent":"test"
	}
	```  
	**Empty request data**  
	**Response**  
	*`Response 400`*  
	```json  
	{
		"password": [
			"This field is required."
		],
		"phone": [
			"This field is required."
		]
	}
	```   
	**Incorrect request data**  
	*`Response 400`*  
	```json  
	{
		"detail": "No active account found with the given credentials"
	}
	```   
	Phone number or email address can be used as identification fields. If you specify two such fields at once, then authentication will occur through the  email address  
	**Input data**  
	```json  
	{
		"email":"user1@gmail.com",
		"password":"user1user1"
	}
	```  
	The *expired_at* field is expressed in seconds and indicates the lifetime of the *access token*     
	**Response**  
	*`Response 200`*  
	```json  
	{
		"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIyODAwMCwianRpIjoiOTJlMzQ4ODg4ZGIzNGYzZTljZDM4NTFlYjNjNDVkYWEiLCJ1c2VyX2lkIjo1fQ.yyKwQG7ax0cfGP4G6kPEhXucEjX4x_m8LlDRapifji0",
		"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4MDAwLCJqdGkiOiI1Y2EwNTlkYTk1MDY0YjdiYjMzMTEyYzE2MDdmMWQ0ZCIsInVzZXJfaWQiOjV9._97nAZzZ_7PQ7O6125_uIrM6DUbtCzhyMP85eD8B3Gc",
		"expired_at": 180
	}
	```  

## **TokenRefresh**  
* **POST**  `auth/token/refresh/`  
	**Headers**  
	```json  
	{
		"Content-Type":"application/json"
	}
	```  
	**Empty request data**  
	**Response**  
	*`Response 400`*  
	```json  
	{
		"refresh": [
			"This field is required."
		]
	}
	```   
	**Incorrect request data**  
	**Response**   
	*`Response 400`*  
	```json  
	{
		"detail": "Refresh token expired or not exist"
	}
	```   
	**Input data**  
	```json  
	{
		"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIyODAwMCwianRpIjoiOTJlMzQ4ODg4ZGIzNGYzZTljZDM4NTFlYjNjNDVkYWEiLCJ1c2VyX2lkIjo1fQ.yyKwQG7ax0cfGP4G6kPEhXucEjX4x_m8LlDRapifji0",
	}
	```  
	**Response**   
	*`Response 200`*  
	```json  
	{
		"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIyODQ2MiwianRpIjoiMjZmMGZmODhkYzY2NDE0YThjYTgwMjFhMjYzZmJmOWEiLCJ1c2VyX2lkIjo1fQ.X5w7P3ehd-Jx_TRsFiox7sHy1LfLlh0dvUzP4KjAtIg",
		"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0",
		"expired_at": 0
	}
	```  
	The *expired_at* field is expressed in seconds and indicates the lifetime of the *access token*  

## **User change**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **GET**  `user/`  
	**Request without authorization in headers**   
	**Response**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**If an authorized user has an *id* that does not match what is on the way**   
	**Response**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**The right user**  
	*`Response 200`*  
	```json   
	{
		"id": 5,
		"surname": "user1",
		"first_name": "user1",
		"second_name": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137",
		"avatar": "host/users/user/5/static/Users/default-user-image.jpeg",
		"confirmed_email": false,
		"confirmed_phone": false,
		"created_at": "2021-09-08T12:22:26.072030Z",
		"updated_at": "2021-09-08T12:22:26.072066Z"
	}
	```  
* **PUT**  `user/`  
	You can change your password, email address and phone number  
	**Empty request data**  
	**Response**  
	*`Response 400`*  
	```json  
	{
	    "surname": [
	        "This field is required."
	    ],
	    "first_name": [
	        "This field is required."
	    ],
	    "second_name": [
	        "This field is required."
	    ],
	    "address": [
	        "This field is required."
	    ],
	    "email": [
	        "This field is required."
	    ],
	    "phone": [
	        "This field is required."
	    ],
	    "avatar": [
	        "This field is required."
	    ],
	    "password": [
	        "This field is required."
	    ]
	}
	```   
	**Request without authorization in headers**  
	**Response**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**If the user has authorization, *id* of which does not match what is on the link** 
	**Response**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Input data**   
	```json  
	{
		"surname": "user3",
		"first_name": "user3",
		"second_name": "user3",
		"address": "user3address",
		"email": "user3@gmail.com",
		"phone": "+79137779135",
		"password":"user3user3"
	}
	```   
	**Response**  
	*`Response 200`*  
	```json  
	{
		"surname": "user3",
		"first_name": "user3",
		"second_name": "user3",
		"address": "user3address",
		"email": "user3@gmail.com",
		"phone": "+79137779135",
		"avatar": "http://127.0.0.1:8000/users/user/5/static/Users/default-user-image.jpeg"
	}
	```  
* **PATCH**  `user/`  
	You can change your password, email address and phone number  
	**Empty request data**  
	**Response**  
	*`Response 200`*  
	```json   
	{
	    "surname": "user3",
	    "first_name": "user3",
	    "second_name": "user3",
	    "address": "user3address",
	    "email": "user3@gmail.com",
	    "phone": "+79137779135",
	    "avatar": "host/users/user/5/static/Users/default-user-image.jpeg"
	}
	```  
	**Request without authorization in headers**  
	**Response**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**If the authorization is with a user whose *id* does not match what is on the link**   
	**Response**   
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Input data**     
	```json  
	{
		"surname": "user1",
		"first_name": "user1",
		"second_name": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137",
		"password":"user1user1"
	}
	```   
	Inserting one of the listed fields is allowed one at a time   
	**Response**   
	*`Response 200`*  
	```json  
	{
		"surname": "user1",
		"first_name": "user1",
		"second_name": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137",
		"avatar": "host/users/user/5/static/Users/default-user-image.jpeg"
	}
	```  
* **DELETE**  `user/`     
	**Request without authorization in headers**  
	**Response**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**If the authorization is with a user whose *id* does not correspond to what is on the link**      
	**Response**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Input data**  
	```json   
	{
	}
	```   
	**Response**  
	*`Response 204`*  
	```json  
	{
	}
	```  