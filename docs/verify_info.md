# **Verify-Info API documentation** - **`/verify-info/`**   


## **Verify User email**  
**Headers**  
```json  
{
	"Content-Type":"application/json",
	"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjI4NDYyLCJqdGkiOiIwZDEwZjNiYzNhM2M0NzdiODQyZWVjNzQ5ZTY5MGI5OSIsInVzZXJfaWQiOjV9.aYGVJfdEXxsp9_ggjdtc6BMYW7qIp7DCH3BPvabllQ0"
}
``` 
* **POST** `verify-user-email/`    
  	If the token is incorrect in the headers   
  	**Response**   
  	*`Response 401`*   
	```json     
	{
	    "detail": "No active account found with the given credentials"
	}
	```   
	**Input data**        
	```json   
	{
	}
	```   
	If the mail is already confirmed    
	**Response**   
	*`Response 200`*  
	```json   
	{
		"detail":"Already confirmed"
	}
	```   
	If you have problems parsing the token from the header   
	**Response**   
	*`Response 400`*  
	```json   
	{
		"detail":"Invalid token or not exist"
	}
	```  
	If you have problems sending your message   
	**Response**   
	*`Response 500`*   
	```json   
	{
		"detail":"Cannot send the mail"
	}
	```  
	If all is well then   
	**Response**   
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
	**Input data**  
	```json  
	{
		"type_code":"email",
		"code":281343
	}
	```  
	If there is an inaccuracy in the input data    
	**Response**  
	```json
	{
	    "detail":"Invalid code or not exist"
	}
	```   
	If *code* and *type_code* are correct    
	**Response**  
	```json
	{
	    "detail": "Successfully confirmed"
	}
	```   