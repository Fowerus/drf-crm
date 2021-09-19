# **Sessions API documentation** - **`/sessions/`**   


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

## **Sessions user**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **GET** `session-user-l/1/`    
	**Response**  
	*`Response 200`*  
	```json   
	[
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
	            "image": "host/sessions/session-user-l/5/static/Users/default-user-image.jpeg",
	            "confirmed_email": true,
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "device": "PostmanRuntime/7.28.3"
	    }
	]
	```   
* **DELETE** `session-user-d/1/`    
	**Response**  
	*`Response 204`*  
	```json   
	{
	}
	```   
## **Sessions client**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOjEsInN1cm5hbWUiOiJDbGllbnQxIiwiZmlyc3RfbmFtZSI6IkNsaWVudDEiLCJwYXRyb255bWljIjoiQ2xpZW50MSIsInBob25lIjoiKzc5OTY3NDg2Mjk0In0.gbODpQyaaenDkgDTL2kM-JMaLnoW7YzTrXdoiVCL1Bg"
}
``` 
* **GET** `session-client-l/1/`    
	**Response**  
	*`Response 200`*  
	```json   
	[
	    {
	        "id": 1,
	        "client": {
	            "id": 1,
	            "surname": "Client1",
	            "name": "Client1",
	            "patronymic": "Client1",
	            "address": "Client1",
	            "phone": "+79137779135",
	            "image": "host/sessions/session-user-l/5/static/Users/default-user-image.jpeg",
	            "confirmed_phone": false,
	            "created_at": "2021-09-08T12:22:26.072030Z",
	            "updated_at": "2021-09-08T15:11:20.864802Z"
	        },
	        "device": "PostmanRuntime/7.28.3"
	    }
	]
	```   
* **DELETE** `session-client-d/1/`    
	**Response**  
	*`Response 204`*  
	```json   
	{
	}
	```   
