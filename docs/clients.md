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

## **ClientCard**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **POST** `client-card-c/`    
	**Emplty request body**  
	**Response**    
	*`Response 400`*  
	```json   
	{
	    "first_name": [
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
	Surname, second_name, address, image, links, data
	**Input data**  
	```json  
	{
	    "organization":1,
	    "first_name":"TestClient",
	    "phone":"+79517487295",
	    "password":"clientclient"
	}
	```  
	**Response**  
	*`Response 201`*  
	```json  
	{
	    "surname": "",
	    "first_name": "TestClient",
	    "second_name": "",
	    "phone": "+79517487295",
	    "address": "",
	    "organization": 1
	}
	```  
* **GET** `client-card-l/1/`      
	*`Response 200`*  
	```json  
	[
	    {
	        "id": 2,
	        "surname": "",
	        "first_name": "TestClient",
	        "second_name": "",
	        "phone": "+79517487295",
	        "address": "",
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
	                "avatar": "../static/Users/default-user-image.jpeg",
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
	        "client": {
	            "id": 3,
	            "surname": "",
	            "first_name": "TestClient",
	            "second_name": "",
	            "phone": "+79517487295",
	            "address": "",
	            "confirmed_phone": false,
	            "organization": [
	                {
	                    "id": 2,
	                    "name": "Test2",
	                    "description": "Test2",
	                    "address": "Test2",
	                    "creator": {
	                        "id": 2,
	                        "surname": "a2",
	                        "first_name": "a2",
	                        "second_name": "a2",
	                        "address": "a2",
	                        "email": "a2@gmail.com",
	                        "phone": null,
	                        "avatar": null,
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
	                {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "first_name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "avatar": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                }
	            ],
	            "created_at": "2021-10-25T18:49:24.278461Z",
	            "updated_at": "2021-10-25T19:00:47.741996Z"
	        },
	        "created_at": "2021-10-25T18:49:24.549258Z",
	        "updated_at": "2021-10-25T18:49:24.549305Z"
	    }
	]
	```  
* **GET** `client-card-l/1/p=+79517487295/`      
	*`Response 200`*  
	```json  
	[
	    {
	        "id": 2,
	        "surname": "",
	        "first_name": "TestClient",
	        "second_name": "",
	        "phone": "+79517487295",
	        "address": "",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "first_name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "avatar": "../static/Users/default-user-image.jpeg",
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
	        "client": {
	            "id": 3,
	            "surname": "",
	            "first_name": "TestClient",
	            "second_name": "",
	            "phone": "+79517487295",
	            "address": "",
	            "confirmed_phone": false,
	            "organization": [
	                {
	                    "id": 2,
	                    "name": "Test2",
	                    "description": "Test2",
	                    "address": "Test2",
	                    "creator": {
	                        "id": 2,
	                        "surname": "a2",
	                        "first_name": "a2",
	                        "second_name": "a2",
	                        "address": "a2",
	                        "email": "a2@gmail.com",
	                        "phone": null,
	                        "avatar": null,
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
	                {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "first_name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "avatar": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                }
	            ],
	            "created_at": "2021-10-25T18:49:24.278461Z",
	            "updated_at": "2021-10-25T19:00:47.741996Z"
	        },
	        "created_at": "2021-10-25T18:49:24.549258Z",
	        "updated_at": "2021-10-25T18:49:24.549305Z"
	    }
	]
	```  
* **GET** `client-card-l/1/f=TestClient/`      
	*`Response 200`*  
	```json  
	[
	    {
	        "id": 2,
	        "surname": "",
	        "first_name": "TestClient",
	        "second_name": "",
	        "phone": "+79517487295",
	        "address": "",
	        "organization": {
	            "id": 1,
	            "name": "Test",
	            "description": "Test",
	            "address": "Test",
	            "creator": {
	                "id": 1,
	                "surname": "a",
	                "first_name": "a",
	                "second_name": "a",
	                "address": "a",
	                "email": "a@gmail.com",
	                "phone": null,
	                "avatar": "../static/Users/default-user-image.jpeg",
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
	        "client": {
	            "id": 3,
	            "surname": "",
	            "first_name": "TestClient",
	            "second_name": "",
	            "phone": "+79517487295",
	            "address": "",
	            "confirmed_phone": false,
	            "organization": [
	                {
	                    "id": 2,
	                    "name": "Test2",
	                    "description": "Test2",
	                    "address": "Test2",
	                    "creator": {
	                        "id": 2,
	                        "surname": "a2",
	                        "first_name": "a2",
	                        "second_name": "a2",
	                        "address": "a2",
	                        "email": "a2@gmail.com",
	                        "phone": null,
	                        "avatar": null,
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
	                {
	                    "id": 1,
	                    "name": "Test",
	                    "description": "Test",
	                    "address": "Test",
	                    "creator": {
	                        "id": 1,
	                        "surname": "a",
	                        "first_name": "a",
	                        "second_name": "a",
	                        "address": "a",
	                        "email": "a@gmail.com",
	                        "phone": null,
	                        "avatar": "../static/Users/default-user-image.jpeg",
	                        "confirmed_email": true,
	                        "confirmed_phone": false,
	                        "created_at": "2021-10-21T15:38:07.599042Z",
	                        "updated_at": "2021-10-22T10:52:18.483765Z"
	                    },
	                    "numbers": null,
	                    "links": null,
	                    "created_at": "2021-10-21T15:45:34.434734Z",
	                    "updated_at": "2021-10-21T15:45:34.434767Z"
	                }
	            ],
	            "created_at": "2021-10-25T18:49:24.278461Z",
	            "updated_at": "2021-10-25T19:00:47.741996Z"
	        },
	        "created_at": "2021-10-25T18:49:24.549258Z",
	        "updated_at": "2021-10-25T18:49:24.549305Z"
	    }
	]
	```  
* **PUT** `client-card-ud/2/`  
	**Empty request data**  
	**Response**  
	*`Response 400`*  
	```json  
	{
	    "first_name": [
	        "This field is required."
	    ],
	    "phone": [
	        "This field is required."
	    ]
	}
	```  
	Surname, second_name, address, image, links, data 
	**Input data**  
	```json  
	{
	    "organization":1,
	    "first_name":"Test2",
	    "surname":"Surname",
	    "second_name":"Patronymic(-_-)",
	    "address":"gdeto",
	    "phone":"+79992638361"
	}
	```  
	**Response**  
	*`Response 200`*  
	```json   
	{
	    "surname": "Surname",
	    "first_name": "Test2",
	    "second_name": "Patronymic(-_-)",
	    "phone": "+79992638361",
	    "address": "gdeto",
	    "links": null
	}
	```   
* **PATCH** `client-client-card-ud/2/`  
	**Empty request data**  
	**Response**  
	*`Response 400`*  
	```json  
	{
	    "surname": "Surname",
	    "first_name": "Test2",
	    "second_name": "Patronymic(-_-)",
	    "phone": "+79992638361",
	    "address": "gdeto",
	    "links": null
	}
	```  
	Surname, second_name, address, image, links, data 
	**Input data**  
	```json  
	{
	    "organization":1,
	    "first_name":"Test2",
	    "surname":"---",
	    "second_name":"---",
	    "address":"gdeto",
	    "phone":"+79993623361",
	}
	```  
	**Response**  
	*`Response 200`*  
	```json   
	{
	    "first_name":"Test2",
	    "surname":"---",
	    "second_name":"---",
	    "address":"gdeto",
	    "phone":"+79993623361",
	}
	```  
* **DELETE** `client-client-card-ud/2/`
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
* **GET** `client-card-r/2/1/`  
	**Response**  
	*`Response 200`*  
	```json   
    {
        "id": 2,
        "surname": "",
        "first_name": "TestClient",
        "second_name": "",
        "phone": "+79517487295",
        "address": "",
        "organization": {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "address": "Test",
            "creator": {
                "id": 1,
                "surname": "a",
                "first_name": "a",
                "second_name": "a",
                "address": "a",
                "email": "a@gmail.com",
                "phone": null,
                "avatar": "../static/Users/default-user-image.jpeg",
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
        "client": {
            "id": 3,
            "surname": "",
            "first_name": "TestClient",
            "second_name": "",
            "phone": "+79517487295",
            "address": "",
            "confirmed_phone": false,
            "organization": [
                {
                    "id": 2,
                    "name": "Test2",
                    "description": "Test2",
                    "address": "Test2",
                    "creator": {
                        "id": 2,
                        "surname": "a2",
                        "first_name": "a2",
                        "second_name": "a2",
                        "address": "a2",
                        "email": "a2@gmail.com",
                        "phone": null,
                        "avatar": null,
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
                {
                    "id": 1,
                    "name": "Test",
                    "description": "Test",
                    "address": "Test",
                    "creator": {
                        "id": 1,
                        "surname": "a",
                        "first_name": "a",
                        "second_name": "a",
                        "address": "a",
                        "email": "a@gmail.com",
                        "phone": null,
                        "avatar": "../static/Users/default-user-image.jpeg",
                        "confirmed_email": true,
                        "confirmed_phone": false,
                        "created_at": "2021-10-21T15:38:07.599042Z",
                        "updated_at": "2021-10-22T10:52:18.483765Z"
                    },
                    "numbers": null,
                    "links": null,
                    "created_at": "2021-10-21T15:45:34.434734Z",
                    "updated_at": "2021-10-21T15:45:34.434767Z"
                }
            ],
            "created_at": "2021-10-25T18:49:24.278461Z",
            "updated_at": "2021-10-25T19:00:47.741996Z"
        },
        "created_at": "2021-10-25T18:49:24.549258Z",
        "updated_at": "2021-10-25T18:49:24.549305Z"
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
