# **Clients API documentation** - **`/clients/`**   


## **Token error**
Если запрос выполняется без токена  
*`Response 401`*  
```json  
{
	"detail": "Authentication credentials were not provided."
}
```  
Если вам не хватает прав или аккаунт не является подтвержденным  или сессия удалена   
*`Response 403`*
```json  
{
	"detail": "You do not have permission to perform this action."
}
```  

## **Clients**  
**Заголовки**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **POST** `client-c/`    
	**Пустой запрос**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	Если указать *id* организации и ваши права позволяют создать клиента, то выдаст(В данном случае следует помещать *id* в *organization* в массив или множество, если *id* будет несколько, то возьмется по индексу 0)  
	**Входные данные**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Ответ**  
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
	Корректный запрос  
	**Входные данные**  
	```json   
	{
		"name":"Client1",
		"organization":[1],
		"phone":"+79517586284",
		"password":"client1client1",
	}
	```  
	**Ответ**  
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
	**Пустой запрос**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```  
	Если указать *id* организации и ваши права позволяют изменять клиента, то выдаст(В данном случае следует помещать *id* в *organization* в массив или множество, если *id* будет несколько, то возьмется по индексу 0)  
	**Входные данные**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Ответ**  
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
	Корректный запрос.
	У клиента можно изменить name, surname, patronymic, phone, password, address, links  
	**Входные данные**  
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
	**Ответ**  
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
	**Пустой запрос**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	Если указать *id* организации и ваши права позволяют изменять клиента, то выдаст(В данном случае следует помещать *id* в *organization* в массив или  множество, если *id* будет несколько, то возьмется по индексу 0)  
	**Входные данные**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Ответ**  
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
	Корректный запрос.  
	У клиента можно изменить name, surname, patronymic, phone, password, address, links  
	**Входные данные**  
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
	**Ответ**  
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
	**Пустой запрос**  
	**Ответ**  
	*`Response 403`*  
	```json  
	{
	    "detail": "You do not have permission to perform this action."
	}
	```   
	Если указать *id* организации и ваши права позволяют удалять клиента, то выдаст(В данном случае следует помещать *id* в *organization* в массив или  множество, если *id* будет несколько, то возьмется по индексу 0)  
	**Входные данные**  
	```json  
	{
		"organization":[1]
	}
	```  
	**Ответ**  
	*`Response 204`*  
	```json   
	{
	}
	```  

## **Client Auth**
**Заголовки**  
```json  
{
	"Content-Type":"application/json"
}
```  
* **POST** `auth/token/`
	**Пустой запрос**  
	**Ответ**  
	*`Response 400`*
	```json
	{
	}
	```
	Этот же ответ в случае некорректности введенных данных  
	Корректный запрос  
	**Входные данные**  
	```json  
	{
		"phone":"+79967486294",
		"password":"client1client1"
	}
	```  
	**Ответ**  
	*`Response 200`*  
	```json  
	{
	    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOjEsInN1cm5hbWUiOiJDbGllbnQxIiwiZmlyc3RfbmFtZSI6IkNsaWVudDEiLCJwYXRyb255bWljIjoiQ2xpZW50MSIsInBob25lIjoiKzc5OTY3NDg2Mjk0In0.gbODpQyaaenDkgDTL2kM-JMaLnoW7YzTrXdoiVCL1Bg"
	}
	```  
