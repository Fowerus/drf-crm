# **Sessions API** - **`/sessions/`**   
    
## **Sessions**    
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)   
* **GET** `session/`    
  OUTPUT    
  *`Response 200`* 
  ```json  
  [
    {  
      "id":1,
      "user":1,
      "device":"Etot"
    },
    {  
      "id":2,
      "user":1,
      "device":"Drugoy"
    }
  ]  
  ```    
* **DELETE** `session/`   
  INPUT   
  ```json   
  {
    "session":1
  }
  ```   
  OUTPUT   
  *`Response 200`*   