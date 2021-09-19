# **Users API documentation** - **`/users/`**   


## **Registration**  
**Заголовки**  
```json  
{
	"Content-Type":"application/json"
}
``` 
* **POST** `auth/registration/`     
	**Пустой запрос**  
	Этот же ответ будет в случае некорректности некоторых данных.   
	**Ответ** 
	*`Response 400`*  
	```json  
	{
		"detail": "Valid phone number or email not provided"
	}
	```  
	Во входных данных можно указать, номер телефона или адрес электронной почты или все вместе   
	**Входные данные**     
	```json  
	{  
		"surname":"user1",   
		"name":"user1",    
		"patronymic":"user1",  
		"address":"user1address",
		"email":"user1@gmail.com",
		"phone":"+79967348137",
		"password":"user1user1"  
	}  
	```  
	Если регистрация происходила, например, по номеру телефона, то в ответе адрес электронной почты указываться не будет(Также и про адрес электронной почты).   Пароль также в ответ от сервера не входит.   
	**Ответ**  
	*`Response 201`*    
	```json  
	{
		"surname": "user1",
		"name": "user1",
		"patronymic": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137"
	}
	```  

## **TokenObtainPair**  
* **POST**  `auth/token/`     
	**Заголовки**  
	```json  
	{
		"Content-Type":"application/json"
	}
	```  
	**Пустой запрос**  
	**Ответ** 
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
	**Некорректные данные**  
	*`Response 400`*  
	```json  
	{
		"detail": "No active account found with the given credentials"
	}
	```   
	В качестве идентификационных полей можно использовать номер телефона или адрес электронной почты. Если укажите сразу два подобных поля, то аутентификация произойдет через адрес электронной почты.   
	**Входные данные**  
	```json  
	{
		"email":"user1@gmail.com",
		"password":"user1user1"
	}
	```  
	Поле *expired_at* выражено в секунда и показывает время жизни *access token*   
	**Ответ**  
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
	**Заголовки**  
	```json  
	{
		"Content-Type":"application/json"
	}
	```  
	**Пустой запрос**  
	**Ответ**  
	*`Response 400`*  
	```json  
	{
		"refresh": [
			"This field is required."
		]
	}
	```   
	**Некорректные данные**  
	**Ответ**  
	*`Response 400`*  
	```json  
	{
		"detail": "Refresh token expired or not exist"
	}
	```   
	**Входные данные**  
	```json  
	{
		"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIyODAwMCwianRpIjoiOTJlMzQ4ODg4ZGIzNGYzZTljZDM4NTFlYjNjNDVkYWEiLCJ1c2VyX2lkIjo1fQ.yyKwQG7ax0cfGP4G6kPEhXucEjX4x_m8LlDRapifji0",
	}
	```  
	**Ответ**  
	*`Response 200`*  
	```json  
	{
		"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIyODQ2MiwianRpIjoiMjZmMGZmODhkYzY2NDE0YThjYTgwMjFhMjYzZmJmOWEiLCJ1c2VyX2lkIjo1fQ.X5w7P3ehd-Jx_TRsFiox7sHy1LfLlh0dvUzP4KjAtIg",
		"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0",
		"expired_at": 0
	}
	```  
	Поле *expired_at* выражено в секунда и показывает время жизни *access token*   

## **User change**  
**Заголовки**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
* **GET**  `user/5/`  
	**Запрос без authorization в заголовках**   
	**Ответ**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**Если у авторизированного юзера *id* не соответствует тому, что в пути**   
	**Ответ**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Корректный юзер**  
	*`Response 200`*  
	```json   
	{
		"id": 5,
		"surname": "user1",
		"name": "user1",
		"patronymic": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137",
		"image": "host/users/user/5/static/Users/default-user-image.jpeg",
		"confirmed_email": false,
		"confirmed_phone": false,
		"created_at": "2021-09-08T12:22:26.072030Z",
		"updated_at": "2021-09-08T12:22:26.072066Z"
	}
	```  
* **PUT**  `user/5/`  
	Можно менять пароль, адрес почты и номер телефона  
	**Пустой запрос**  
	**Ответ**  
	*`Response 400`*  
	```json  
	{
		"surname": [
			"This field is required."
		],
		"name": [
			"This field is required."
		],
		"patronymic": [
			"This field is required."
		],
		"address": [
			"This field is required."
		]
	}
	```   
	**Запрос без authorization в заголовках**  
	**Ответ**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**Если авторизации у юзера, *id* которого не соответствует тому, что в пути**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Входные данные**   
	```json  
	{
		"surname": "user3",
		"name": "user3",
		"patronymic": "user3",
		"address": "user3address",
		"email": "user3@gmail.com",
		"phone": "+79137779135",
		"password":"user3user3"
	}
	```   
	**Ответ**  
	*`Response 200`*  
	```json  
	{
		"surname": "user3",
		"name": "user3",
		"patronymic": "user3",
		"address": "user3address",
		"email": "user3@gmail.com",
		"phone": "+79137779135",
		"image": "http://127.0.0.1:8000/users/user/5/static/Users/default-user-image.jpeg"
	}
	```  
* **PATCH**  `user/5/`  
	Можно менять пароль, адрес почты и номер телефона  
	**Пустой запрос**  
	**Ответ**  
	*`Response 200`*  
	```json   
	{
	    "surname": "user3",
	    "name": "user3",
	    "patronymic": "user3",
	    "address": "user3address",
	    "email": "user3@gmail.com",
	    "phone": "+79137779135",
	    "image": "host/users/user/5/static/Users/default-user-image.jpeg"
	}
	```  
	**Запрос без authorization в заголовках**  
	**Ответ**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**Если авторизации у юзера, *id* которого не соответствует тому, что в пути**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Входные данные**   
	```json  
	{
		"surname": "user1",
		"name": "user1",
		"patronymic": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137",
		"password":"user1user1"
	}
	```   
	Вставка одного из перечисленных полей допускается и по одному   
	**Ответ**  
	*`Response 200`*  
	```json  
	{
		"surname": "user1",
		"name": "user1",
		"patronymic": "user1",
		"address": "user1address",
		"email": "user1@gmail.com",
		"phone": "+79967348137",
		"image": "host/users/user/5/static/Users/default-user-image.jpeg"
	}
	```  
* **DELETE**  `user/5/`     
	**Запрос без authorization в заголовках**  
	**Ответ**  
	*`Response 401`*  
	```json  
	{
		"detail": "Authentication credentials were not provided."
	}
	```   
	**Если авторизации у юзера, *id* которого не соответствует тому, что в пути**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
		"detail": "You do not have permission to perform this action."
	}
	```  
	**Входные данные**  
	```json   
	{
	}
	```   
	**Ответ**  
	*`Response 204`*  
	```json  
	{
	}
	```  

## **User-executor list**  
* **GET** `user/executor/`  
**Заголовки**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
**Запрос без authorization в заголовках**   
**Ответ**  
*`Response 401`*  
```json  
{
	"detail": "Authentication credentials were not provided."
}
```   
**Ответ**  
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
