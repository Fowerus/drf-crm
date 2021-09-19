# **Verify-Info API documentation** - **`/verify-info/`**   


## **Verify User email**  
**Заголовки**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **POST** `verify-user-email/`    
  	Если в заголовках неверный токен   
  	**Ответ**   
  	*`Response 401`*   
	```json     
	{
	    "detail": "No active account found with the given credentials"
	}
	```   
	**Входные данные**        
	```json   
	{
	}
	```   
	Если почта уже подтверждена   
	**Ответ**   
	*`Response 200`*  
	```json   
	{
		"detail":"Already confirmed"
	}
	```   
	Если возникли проблемы с парсингом токена из заголовка  
	**Ответ**   
	*`Response 400`*  
	```json   
	{
		"detail":"Invalid token or not exist"
	}
	```  
	Если возникли проблемы с отправкой сообщения  
	**Ответ**   
	*`Response 500`*   
	```json   
	{
		"detail":"Cannot send the mail"
	}
	```  
	Если все удачно то   
	**Ответ**   
	*`Response 200`*   
	```json   
	{
	}
	```   	

## **Accept User info**
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
```  
*	**POST** `accept-user-info/`  
	**Входные данные**  
	```json  
	{
		"type_code":"email",
		"code":281343
	}
	```  
	Если во входных данных есть неточность  
	**Ответ**  
	```json
	{
	    "detail":"Invalid code or not exist"
	}
	```   
	Если *code* и *type_code* верные  
	**Ответ**  
	```json
	{
	    "detail": "Successfully confirmed"
	}
	```   