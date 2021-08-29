# **Clients API** - **`/clients/`**   
    
## **Sessions**    
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)   
* **GET** `client/`    
  OUTPUT    
  *`Response 200`*  
  ```json  
  [
    {
      "order_code":1232,
      "description":"order",    
      "creator":1,  
      "executor":2,
      "client":1,
      "service":1,
    },
  ]  
  ```    
* **PATCH** `client/`                               
  INPUT    
  ```json  
  {  
    "surname":"client1Changed",   
    "name":"client1Changed@gmail.com",    
    "patronymic":"client1Changed",  
    "address":"client1Changedaddress",
    "email":"user1Changed@gmail.com",
    "image":"/new/",
    "number":"+79957348130",
    "password":"client1client1Changed"  
  }  
  ```    
  OUTPUT    
  *`Response 200`*  
  ```json  
  {  
    "success":{
      "Surname":"Surname successfully changed",
      "Name":"Name successfully changed", 
      "Patronymic":"Patronymic successfully changed",
      "...":"",
    },
    "error":{}
  }  
  ```  
  OUTPUT   
  *`Response 200`*   