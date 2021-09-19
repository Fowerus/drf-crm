# **Clients API documentation** - **`/clients/`**   


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

## **Clients**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **POST** `client-c/`    
	**Emplty request body**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to create a client, it will return (In this case, you should place *id* in *organization* in an array or set, if there are several *id*, it will be taken at index 0)  
	**Input data**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Response**  
	*`Response 400`*  
	```json   
	{
	    "name": [
	        "This field is required."
	    ],
	    "phone": [
	        "This field is required."
	    ],
	    "password": [
	        "This field is required."
	    ]
	}
	```   
	The correct request    
	**Input data**  
	```json   
	{
		"name":"Client1",
		"organization":[1],
		"phone":"+79517586284",
		"password":"client1client1",
	}
	```  
	**Response**  
	*`Response 201`*  
	```json  
	{
	    "surname": "",
	    "name": "Client1",
	    "patronymic": "",
	    "phone": "+79517586284",
	    "address": "",
	    "organization": [
	        1
	    ]
	}
	```  
* **GET** `client-l/1/`      
	*`Response 200`*  
	```json  
	[
	    {
	        "id": 1,
	        "surname": "",
	        "name": "Client1",
	        "patronymic": "",
	        "phone": "+79517586284",
	        "address": "",
	        "confirmed_phone": false,
	        "organization": [
	            {
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
	                    "image": "host/clients/client-l/1/static/Users/default-user-image.jpeg",
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
	            }
	        ],
	        "created_at": "2021-09-09T04:10:19.375717Z",
	        "updated_at": "2021-09-09T04:10:19.755395Z"
	    }
	]
	```  
* **PUT** `client-u/1/`  
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to create a client, it will return (In this case, you should place *id* in *organization* in an array or set, if there are several *id*, it will be taken at index 0)  
	**Input data**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Response**  
	*`Response 400`*  
	```json   
	{
	    "name": [
	        "This field is required."
	    ],
	    "phone": [
	        "This field is required."
	    ],
	    "password": [
	        "This field is required."
	    ]
	}
	```   
	The correct request  
	At the client, you can change name, surname, patronymic, phone, password, address, links  
	**Input data**  
	```json  
	{
		"name":"Client1Changed",
		"surname":"Client1Changed",
		"patronymic":"Client1Changed",
		"phone":"+79517486294",
		"address":"Client1Changed",
		"links":{"vk":"vk.com"},
		"password":"client1client1changed",
        "organization":[1]
	}
	```  
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "surname": "Client1Changed",
	    "name": "Client1Changed",
	    "patronymic": "Client1Changed",
	    "phone": "+79517486294",
	    "address": "Client1Changed",
	    "links": {
	        "vk": "vk.com"
	    }
	}
	```  
* **PATCH** `client-u/1/`  
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	If you specify the *id* of the organization and your rights allow you to create a client, it will return (In this case, you should place *id* in *organization* in an array or set, if there are several *id*, it will be taken at index 0)  
	**Input data**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Response**  
	*`Response 200`*  
	```json   
	{
	    "surname": "Client1Changed",
	    "name": "Client1Changed",
	    "patronymic": "Client1Changed",
	    "phone": "+79517486294",
	    "address": "Client1Changed",
	    "links": {
	        "vk": "vk.com"
	    }
	}
	```   
	The correct request    
	At the client, you can change name, surname, patronymic, phone, password, address, links  
	**Input data**  
	```json  
	{
		"name":"Client1",
		"surname":"Client1",
		"patronymic":"Client1",
		"phone":"+79967486294",
		"address":"Client1",
		"links":{"vk2":"vk.com"},
		"password":"client1client1",
        "organization":[1]
	}
	```  
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "surname": "Client1",
	    "name": "Client1",
	    "patronymic": "Client1",
	    "phone": "+79967486294",
	    "address": "Client1",
	    "links": {
	        "vk2": "vk.com"
	    }
	}
	```  
* **DELETE** `clients-r/1/1/`  
	**Empty request data**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	If you specify the *id* of the organization and your rights allow you to create a client, it will return (In this case, you should place *id* in *organization* in an array or set, if there are several *id*, it will be taken at index 0)  
	**Input data**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Response**  
	*`Response 204`*  
	```json   
	{
	}
	```  

## **Client Auth**
**Headers**  
```json  
{
	"Content-Type":"application/json"
}
```  
* **POST** `auth/token/`
	**Empty request data**  
	**Response**  
	*`Response 400`*
	```json
	{
	}
	```
	The same answer in case of incorrect data entered   
	The correct request  
	**Input data**  
	```json  
	{
		"phone":"+79967486294",
		"password":"client1client1"
	}
	```  
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOjEsInN1cm5hbWUiOiJDbGllbnQxIiwiZmlyc3RfbmFtZSI6IkNsaWVudDEiLCJwYXRyb255bWljIjoiQ2xpZW50MSIsInBob25lIjoiKzc5OTY3NDg2Mjk0In0.gbODpQyaaenDkgDTL2kM-JMaLnoW7YzTrXdoiVCL1Bg"
	}
	```  
