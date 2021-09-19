# **Organizations API documentation** - **`/organizations/`**   


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


## **Organizations Create/List**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **POST** `organization-lc/`        
	**Emplty request body**     
	**Response**  
	*`Response 400`*    
	```json  
	{
		"name": [
			"This field is required."
		],
		"address": [
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
		"name":"Organization1",    
		"description":"Organization1",  
		"address":"Organization1",
		"creator":5, 
	}  
	```  
	**Response**  
	*`Response 201`*    
	```json  
	{
		"name": "Organization1",
		"description": "Organization1",
		"address": "Organization1",
		"links": null,
		"numbers": null,
		"creator": 5
	}
	```  
* **GET** `organization-lc/`    
	**Response**  
	*`Response 200`*    
	```json   
	[
		{
			"id": 1,
			"name": "Organization1",
			"description": "Organization1",
			"address": "Organization1",
			"creator": {
				"id": 5,
				"surname": "user3",
				"name": "user3",
				"patronymic": "user3",
				"address": "user3address",
				"email": "user3@gmail.com",
				"phone": "+79137779135",
				"image": "host/organizations/organization-lc/static/Users/default-user-image.jpeg",
				"confirmed_email": true,
				"confirmed_phone": false,
				"created_at": "2021-09-08T12:22:26.072030Z",
				"updated_at": "2021-09-08T15:11:20.864802Z"
			},
			"created_at": "2021-09-08T15:13:41.218868Z",
			"numbers": null,
			"links": null,
			"updated_at": "2021-09-08T15:13:41.219003Z"
		}
	]
	```   

## **Organizations Retrieve/Update/Destroy**  
**Headers**   
```json   
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **GET** `organization-rud/1/`   
	**Response**   
	*`Response 200`*   
	```json   
	{
		"id": 1,
		"name": "Organization1",
		"description": "Organization1",
		"address": "Organization1",
		"creator": {
			"id": 5,
			"surname": "user3",
			"name": "user3",
			"patronymic": "user3",
			"address": "user3address",
			"email": "user3@gmail.com",
			"phone": "+79137779135",
			"image": "host/organizations/organization-rud/1/static/Users/default-user-image.jpeg",
			"confirmed_email": true,
			"confirmed_phone": false,
			"created_at": "2021-09-08T12:22:26.072030Z",
			"updated_at": "2021-09-08T15:11:20.864802Z"
		},
		"created_at": "2021-09-08T15:13:41.218868Z",
		"numbers": null,
		"links": null,
		"updated_at": "2021-09-08T15:13:41.219003Z"
	}
	```   
* **PUT** `organization-rud/1/`    
	**Emplty request body**     
	**Response**    
	*`Response 400`*   
	```json    
	{
		"name": [
			"This field is required."
		],
		"description": [
			"This field is required."
		],
		"address": [
			"This field is required."
		]
	}
	```   
	Можно изменить *name*, *description*, *address*, *links*, *numbers*   
	**Input data**      
	```json   
	{     
		"name":"Organization2",    
		"description":"Organization2",  
		"address":"Organization2",
		"links":{"vk":"vk.com"},
		"numbers":{"main":"+79999999999"}
	}  
	```    
	**Response**   
	*`Response 200`*  
	```json  
	{
		"name": "Organization2",
		"description": "Organization2",
		"address": "Organization2",
		"links": {
			"vk": "vk.com"
		},
		"numbers": {
			"main": "+79999999999"
		}
	}
	```  
* **PATCH** `organization-rud/1/`   
	**Emplty request body**    
	**Response**   
	*`Response 200`*  
	```json   
	{
		"name": "Organization2",
		"description": "Organization2",
		"address": "Organization2",
		"links": {
			"vk": "vk.com"
		},
		"numbers": {
			"main": "+79999999999"
		}
	}
	```   
	**Input data**      
	```json  
	{     
		"name":"Organization1",    
		"description":"Organization1",  
		"address":"Organization1",
		"links":{"vk":"vk.com"},
		"numbers":{"main":"+79999999999"}
	}  
	```   
	**Response**  
	*`Response 200`*   
	```json   
	{
		"name": "Organization1",
		"description": "Organization1",
		"address": "Organization1",
		"links": {
			"vk": "vk.com"
		},
		"numbers": {
			"main": "+79999999999"
		}
	}
	```   
* **DELETE** `organization-rud/1/`  
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

## **Members**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
*	**POST** `member-c/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json   
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	The same answer will be in case of conflicts of permissions from the fields *organization*, *user*, *role*  
	*user* must be verified, role must belong to the organization and you must have the appropriate rights  
	**Input data**  
	```json  
	{
	    "organization":1,
	    "role":1,
	    "user":2
	}
	```  
	**Response**  
	*`Response 201`*   
	```json   
	{
	    "user": 2,
	    "role": 1,
	    "organization": 1
	}
	```  
* **GET** `member-l/1/`  
	The list can be seen by the authorized person   
	**Response**   
	*`Reponse 200`*  
	```json  
	[
	    {
	        "id": 2,
	        "user": {
	            "id": 2,
	            "surname": "b",
	            "name": "b",
	            "patronymic": "b",
	            "address": "b",
	            "email": "b@gmail.com",
	            "phone": null,
	            "image": "host/organizations/member-l/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:04:11.916592Z",
	            "updated_at": "2021-09-09T02:31:17.945129Z"
	        },
	        "role": {
	            "id": 1,
	            "name": "Role 1",
	            "permissions": [
	                {
	                    "id": 2,
	                    "name": "Can change role",
	                    "codename": "role_change"
	                },
	                {
	                    "id": 1,
	                    "name": "Can add role",
	                    "codename": "role_create"
	                }
	            ],
	            "organization": {
	                "id": 1,
	                "name": "Organization2",
	                "description": "Organization2",
	                "address": "Organization2",
	                "creator": {
	                    "id": 5,
	                    "surname": "user3",
	                    "name": "user3",
	                    "patronymic": "user3",
	                    "address": "user3address",
	                    "email": "user3@gmail.com",
	                    "phone": "+79137779135",
	                    "image": "host/organizations/member-l/1/static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-09-08T12:22:26.072030Z",
	                    "updated_at": "2021-09-08T15:11:20.864802Z"
	                },
	                "created_at": "2021-09-08T15:13:41.218868Z",
	                "numbers": {
	                    "main": "+79999999999"
	                },
	                "links": {
	                    "vk": "vk.com"
	                },
	                "updated_at": "2021-09-08T15:29:06.832419Z"
	            },
	            "created_at": "2021-09-08T15:48:56.955471Z",
	            "updated_at": "2021-09-08T15:48:56.955508Z"
	        },
	        "organization": {
	            "id": 1,
	            "name": "Organization2",
	            "description": "Organization2",
	            "address": "Organization2",
	            "creator": {
	                "id": 5,
	                "surname": "user3",
	                "name": "user3",
	                "patronymic": "user3",
	                "address": "user3address",
	                "email": "user3@gmail.com",
	                "phone": "+79137779135",
	                "image": "host/organizations/member-l/1/static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-09-08T12:22:26.072030Z",
	                "updated_at": "2021-09-08T15:11:20.864802Z"
	            },
	            "created_at": "2021-09-08T15:13:41.218868Z",
	            "numbers": {
	                "main": "+79999999999"
	            },
	            "links": {
	                "vk": "vk.com"
	            },
	            "updated_at": "2021-09-08T15:29:06.832419Z"
	        },
	        "created_at": "2021-09-09T02:31:20.672805Z",
	        "updated_at": "2021-09-09T02:31:20.672841Z"
	    },
	    {
	        "id": 1,
	        "user": {
	            "id": 5,
	            "surname": "user3",
	            "name": "user3",
	            "patronymic": "user3",
	            "address": "user3address",
	            "email": "user3@gmail.com",
	            "phone": "+79137779135",
	            "image": "host/organizations/member-l/1/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "role": {
	            "id": 2,
	            "name": "Role for user3",
	            "permissions": [
	                {
	                    "id": 8,
	                    "name": "Can delete member",
	                    "codename": "organization_member_delete"
	                },
	                {
	                    "id": 7,
	                    "name": "Can change member",
	                    "codename": "organization_member_change"
	                },
	                {
	                    "id": 6,
	                    "name": "Can add member",
	                    "codename": "organization_member_create"
	                }
	            ],
	            "organization": {
	                "id": 1,
	                "name": "Organization2",
	                "description": "Organization2",
	                "address": "Organization2",
	                "creator": {
	                    "id": 5,
	                    "surname": "user3",
	                    "name": "user3",
	                    "patronymic": "user3",
	                    "address": "user3address",
	                    "email": "user3@gmail.com",
	                    "phone": "+79137779135",
	                    "image": "host/organizations/member-l/1/static/Users/default-user-image.jpeg",
	                    "confirmed_email": true,
	                    "confirmed_phone": false,
	                    "created_at": "2021-09-08T12:22:26.072030Z",
	                    "updated_at": "2021-09-08T15:11:20.864802Z"
	                },
	                "created_at": "2021-09-08T15:13:41.218868Z",
	                "numbers": {
	                    "main": "+79999999999"
	                },
	                "links": {
	                    "vk": "vk.com"
	                },
	                "updated_at": "2021-09-08T15:29:06.832419Z"
	            },
	            "created_at": "2021-09-09T02:30:45.296150Z",
	            "updated_at": "2021-09-09T02:30:45.296194Z"
	        },
	        "organization": {
	            "id": 1,
	            "name": "Organization2",
	            "description": "Organization2",
	            "address": "Organization2",
	            "creator": {
	                "id": 5,
	                "surname": "user3",
	                "name": "user3",
	                "patronymic": "user3",
	                "address": "user3address",
	                "email": "user3@gmail.com",
	                "phone": "+79137779135",
	                "image": "host/organizations/member-l/1/static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-09-08T12:22:26.072030Z",
	                "updated_at": "2021-09-08T15:11:20.864802Z"
	            },
	            "created_at": "2021-09-08T15:13:41.218868Z",
	            "numbers": {
	                "main": "+79999999999"
	            },
	            "links": {
	                "vk": "vk.com"
	            },
	            "updated_at": "2021-09-08T15:29:06.832419Z"
	        },
	        "created_at": "2021-09-09T02:30:54.647877Z",
	        "updated_at": "2021-09-09T02:30:54.647913Z"
	    }
	]
	```   
* **PUT** `member-ud/2/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json   
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	The request must contain *organizations* and *role*   
	**Input data**   
	```json   
	{
		"organization":1,
		"role":2
	}
	```   
	**Response**   
	*`Response 200`*   
	```json   
	{
	    "role": 2
	}
	```   
* **PATCH** `member-ud/2/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json   
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	If you specify only *organizations* and your rights allow you to change the employee, then it will issue    
	**Response**   
	*`Response 200`*    
	```json  
	{
	    "role": 2
	}
	```  
	**Input data**  
	```json   
	{
		"organization":1,
		"role":1
	}
	```  
	**Response**   
	*`Response 200`*   
	```json  
	{
	    "role": 1
	}
	```  
* **DELETE** `member-ud/2/`  
	**Emplty request body**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify only *organizations* and your rights allow you to delete the employee, then it will issue    
	**Response**  
	*`Response 204`*   
	```json  
	{
	}
	```  
* **GET** `member-r/1/`   
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "id": 2,
	    "user": {
	        "id": 2,
	        "surname": "b",
	        "name": "b",
	        "patronymic": "b",
	        "address": "b",
	        "email": "b@gmail.com",
	        "phone": null,
	        "image": "host/organizations/member-r/2/static/Users/default-user-image.jpeg",
	        "confirmed_email": true,
	        "confirmed_phone": false,
	        "created_at": "2021-09-08T12:04:11.916592Z",
	        "updated_at": "2021-09-09T02:31:17.945129Z"
	    },
	    "role": {
	        "id": 2,
	        "name": "Role for user3",
	        "permissions": [
	            {
	                "id": 8,
	                "name": "Can delete member",
	                "codename": "organization_member_delete"
	            },
	            {
	                "id": 7,
	                "name": "Can change member",
	                "codename": "organization_member_change"
	            },
	            {
	                "id": 6,
	                "name": "Can add member",
	                "codename": "organization_member_create"
	            }
	        ],
	        "organization": {
	            "id": 1,
	            "name": "Organization2",
	            "description": "Organization2",
	            "address": "Organization2",
	            "creator": {
	                "id": 5,
	                "surname": "user3",
	                "name": "user3",
	                "patronymic": "user3",
	                "address": "user3address",
	                "email": "user3@gmail.com",
	                "phone": "+79137779135",
	                "image": "host/organizations/member-r/2/static/Users/default-user-image.jpeg",
	                "confirmed_email": true,
	                "confirmed_phone": false,
	                "created_at": "2021-09-08T12:22:26.072030Z",
	                "updated_at": "2021-09-08T15:11:20.864802Z"
	            },
	            "created_at": "2021-09-08T15:13:41.218868Z",
	            "numbers": {
	                "main": "+79999999999"
	            },
	            "links": {
	                "vk": "vk.com"
	            },
	            "updated_at": "2021-09-08T15:29:06.832419Z"
	        },
	        "created_at": "2021-09-09T02:30:45.296150Z",
	        "updated_at": "2021-09-09T02:30:45.296194Z"
	    },
	    "organization": {
	        "id": 1,
	        "name": "Organization2",
	        "description": "Organization2",
	        "address": "Organization2",
	        "creator": {
	            "id": 5,
	            "surname": "user3",
	            "name": "user3",
	            "patronymic": "user3",
	            "address": "user3address",
	            "email": "user3@gmail.com",
	            "phone": "+79137779135",
	            "image": "host/organizations/member-r/2/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "created_at": "2021-09-08T15:13:41.218868Z",
	        "numbers": {
	            "main": "+79999999999"
	        },
	        "links": {
	            "vk": "vk.com"
	        },
	        "updated_at": "2021-09-08T15:29:06.832419Z"
	    },
	    "created_at": "2021-09-09T02:31:20.672805Z",
	    "updated_at": "2021-09-09T02:45:13.232986Z"
	}
	```  

## **Roles and Permissions**
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **POST** `role-c/`  
	**Emplty request body**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify *organization* and the rights allow
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
	    "name": [
	        "This field is required."
	    ],
	    "permissions": [
	        "This field is required."
	    ]
	}
	```    
	Request with all required fields    
	*Permissions* should be an array or set.  
	**Input data**   
	```json  
	{
		"organization":1,
		"name":"Role created in docs",
		"permissions":[1,2,3]
	}
	```  
	**Response**  
	*`Response 200`*  
	```json  
	{
	    "name": "Role created in docs",
	    "permissions": [
	        3,
	        2,
	        1
	    ],
	    "organization": 1
	}
	```    
* **GET** `role-l/1/`  
	**Response**   
	```json   
	[
	    {
	        "id": 2,
	        "name": "Role for user3",
	        "permissions": [
	            {
	                "id": 8,
	                "name": "Can delete member",
	                "codename": "organization_member_delete"
	            },
	            {
	                "id": 7,
	                "name": "Can change member",
	                "codename": "organization_member_change"
	            },
	            {
	                "id": 6,
	                "name": "Can add member",
	                "codename": "organization_member_create"
	            },
	            {
	                "id": 4,
	                "name": "Can view role",
	                "codename": "role_view"
	            },
	            {
	                "id": 1,
	                "name": "Can add role",
	                "codename": "role_create"
	            }
	        ],
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
	                "image": "host/organizations/role-l/1/static/Users/default-user-image.jpeg",
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
	        "created_at": "2021-09-09T02:30:45.296150Z",
	        "updated_at": "2021-09-09T03:03:43.813278Z"
	    },
	    {
	        "id": 3,
	        "name": "Role created in docs",
	        "permissions": [
	            {
	                "id": 3,
	                "name": "Can delete role",
	                "codename": "role_delete"
	            },
	            {
	                "id": 2,
	                "name": "Can change role",
	                "codename": "role_change"
	            },
	            {
	                "id": 1,
	                "name": "Can add role",
	                "codename": "role_create"
	            }
	        ],
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
	                "image": "host/organizations/role-l/1/static/Users/default-user-image.jpeg",
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
	        "created_at": "2021-09-09T03:00:57.668253Z",
	        "updated_at": "2021-09-09T03:00:57.709165Z"
	    },
	    {
	        "id": 1,
	        "name": "Role 1",
	        "permissions": [
	            {
	                "id": 2,
	                "name": "Can change role",
	                "codename": "role_change"
	            },
	            {
	                "id": 1,
	                "name": "Can add role",
	                "codename": "role_create"
	            }
	        ],
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
	                "image": "host/organizations/role-l/1/static/Users/default-user-image.jpeg",
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
	        "created_at": "2021-09-08T15:48:56.955471Z",
	        "updated_at": "2021-09-08T15:48:56.955508Z"
	    }
	]
	```   
* **PUT** `role-ud/1/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json   
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	The same Response if the role does not allow        
	If the role allows   
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
	    "name": [
	        "This field is required."
	    ],
	    "permissions": [
	        "This field is required."
	    ]
	}
	```  
	The correct request   
	The *permissions* field contains an array or set. "Exclusive or" -XOR applies here.  
	This role was previously created with permissions 1,2,3    
	**Input data**    
	```json   
	{
		"organization":1,
		"name":"Changed role name",
		"permissions":[1,2,4,5]
	}
	```   
	**Response**  
	*`Response 400`*  
	```json   
	{
	    "name": "Changed role name",
	    "permissions": [
	        5,
	        4,
	        3
	    ]
	}
	```   
* **PATCH** `role-ud/1/`  
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	The same Response if the role does not allow    

	If the role allows    
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
	    "name": "Changed role name",
	    "permissions": [
	        5,
	        4,
	        3
	    ]
	}
	```  
	The correct request   
	The *permissions* field contains an array or set. "Exclusive or" -XOR applies here.  
	This role has permissions 3,4,5  
	**Input data**   
	```json  
	{
		"organization":1,
		"name":"Changed role name2",
		"permissions":[1,2,4,5]
	}
	```  
	**Response**   
	*`Response 400`*   
	```json  
	{
	    "name": "Changed role name2",
	    "permissions": [
	        3,
	        2,
	        1
	    ]
	}
	```   
* **DELETE** `role-ud/2/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to delete an employee, then it will give  
	**Response**  
	*`Response 204`*  
	```json  
	{
	}
	```  
* **GET** `role-r/1/1/`  
	**Response**  
	*`Response 200`*   
	```json   
	{
	    "id": 1,
	    "name": "Changed role name2",
	    "permissions": [
	        {
	            "id": 3,
	            "name": "Can delete role",
	            "codename": "role_delete"
	        },
	        {
	            "id": 2,
	            "name": "Can change role",
	            "codename": "role_change"
	        },
	        {
	            "id": 1,
	            "name": "Can add role",
	            "codename": "role_create"
	        }
	    ],
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
	            "image": "host/organizations/role-r/1/1/static/Users/default-user-image.jpeg",
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
	    "created_at": "2021-09-08T15:48:56.955471Z",
	    "updated_at": "2021-09-09T03:21:38.596025Z"
	}
	```  
* **GET** `perm-l/1/`  
	**Response**  
	*`Response 200`*  
	```json   
	[
	    {
	        "id": 10,
	        "name": "Can view perm",
	        "codename": "perm_view"
	    },
	    {
	        "id": 9,
	        "name": "Member guru",
	        "codename": "organization_member_guru"
	    },
	    {
	        "id": 8,
	        "name": "Can delete member",
	        "codename": "organization_member_delete"
	    },
	    {
	        "id": 7,
	        "name": "Can change member",
	        "codename": "organization_member_change"
	    },
	    {
	        "id": 6,
	        "name": "Can add member",
	        "codename": "organization_member_create"
	    },
	    {
	        "id": 5,
	        "name": "Role guru",
	        "codename": "role_guru"
	    },
	    {
	        "id": 4,
	        "name": "Can view role",
	        "codename": "role_view"
	    },
	    {
	        "id": 3,
	        "name": "Can delete role",
	        "codename": "role_delete"
	    },
	    {
	        "id": 2,
	        "name": "Can change role",
	        "codename": "role_change"
	    },
	    {
	        "id": 1,
	        "name": "Can add role",
	        "codename": "role_create"
	    }
	]
	```   

## **Services**   
**Headers**   
```json   
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **POST** `service-c/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json   
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	If you specify the *id* of the organization and your rights allow you to create a service, then it will give   
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
	    "name": [
	        "This field is required."
	    ],
	    "address": [
	        "This field is required."
	    ],
	    "phone": [
	        "This field is required."
	    ]
	}
	```   
	The correct request    
	**Input data**   
	```json   
	{
		"name":"Programming",
		"organization":1,
		"address":"Gdeto v rossii",
		"phone":"+79518472961"
	}
	```   
	**Response**   
	*`Response 201`*   
	```json   
	{
	    "name":"Programming",
	    "organization":1,
	    "address":"Gdeto v rossii",
	    "phone":"+79518472961"
	}
	```   
* **PUT** `service-ud/1/`   
	**Emplty request body**   
	**Response**   
	*`Response 403`*   
	```json   
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	If you specify the *id* of the organization and your rights allow you to change the service, then it will give  
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
	    "name": [
	        "This field is required."
	    ],
	    "address": [
	        "This field is required."
	    ],
	    "phone": [
	        "This field is required."
	    ]
	}
	```  
	The correct request     
	**Input data**  
	```json   
	{
		"name":"Programming Changed",
		"organization":1,
		"address":"Gdeto v rossii2",
		"phone":"+79518472962"
	}
	```  
	**Response**  
	*`Response 201`*  
	```json   
	{
	    "name": "Programming Changed",
	    "address": "Gdeto v rossii2",
	    "phone": "+79518472962"
	}
	```  
* **PATCH** `service-ud/1/`  
	**Emplty request body**  
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	If you specify the *id* of the organization and your rights allow you to change the service, then it will give  
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
	    "name": "Programming Changed",
	    "address": "Gdeto v rossii2",
	    "phone": "+79518472962"
	}
	```   
	The correct request  
	**Input data**  
	```json   
	{
		"name":"Programming",
		"organization":1,
		"address":"Gdeto v rossii",
		"phone":"+79518472961"
	}
	```  
	**Response**  
	*`Response 201`*  
	```json  
	{
	    "name": "Programming",
	    "address": "Gdeto v rossii",
	    "phone": "+79518472961"
	}
	```  
* **DELETE** `service-ud/1/`   
	**Emplty request body**   
	**Response**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	If you specify the *id* of the organization and your rights allow you to delete the service, then it will give  
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
* **GET** `service-r/1/1/`  
	**Response**  
	*`Response 200`*  
	```json  
	{
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
	            "image": "http://127.0.0.1:8000/organizations/service-r/1/1/static/Users/default-user-image.jpeg",
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
	}
	```  
