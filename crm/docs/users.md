# **Users API** - **`/users/`**   
      
    
## **Authentication and similar functions**
    
### **Registration**    
* **POST** `auth/registration/`    
  INPUT    
  ```json  
  {  
    "surname":"user1",   
    "name":"user1@gmail.com",    
    "patronymic":"user1",  
    "address":"user1address",
    "email":"user1@gmail.com",
    "number":"+79967348137",
    "password":"user1user1"  
  }  
  ```    
  OUTPUT    
  *`Response 201`*    
  ```json  
  {  
    "surname":"user1",   
    "name":"user1@gmail.com",    
    "patronymic":"user1",  
    "address":"user1address",
    "email":"user1@gmail.com",
    "number":"+79967348137", 
  }
  ```    
    
### **AccessToken**    
* **POST** `auth/token/`    
  INPUT    
  ```json   
  {  
    "email":"user1@gmail.com",    
    "password":"user1user1"  
  }  
  ```   
  You also can   
  ```json   
  {  
    "number":"+79967348137",    
    "password":"user1user1"  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {  
    "refresh":"refresh",  
    "access":"access",
    "expired_at":"seconds"
  }  
  ```  

### **RefreshToken**    
* **POST** `auth/token/refresh`    
  INPUT    
  ```json   
  {  
    "refresh":"refresh"  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {  
    "refresh":"refresh",  
    "access":"access",
    "expired_at":"seconds"
  }  
  ```  
    
### **Retrieve, Update, Destroy a user**   
##### This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)  
* **GET** `user/`    
  OUTPUT    
  *`Response 200`*  
  ```json    
  {  
    "id":1,
    "surname":"user1",   
    "name":"user1@gmail.com",    
    "patronymic":"user1",  
    "address":"user1address",
    "email":"user1@gmail.com",
    "number":"+79967348137", 
    "confirmed_email":"Boolean",
    "confirmed_number":"Boolean",
    "created_at":"time", 
    "updated_at":"time"
  }
  ```  
* **GET** `user/executor/`   
  OUTPUT   
  *`Response 200`*   
  ```json   
  [
    {
      "id":1,
      "...":""
    }
  ]
  ```      
* **PATCH** `user/`                               
  INPUT    
  ```json  
  {  
    "surname":"user1",   
    "name":"user1Changed@gmail.com",    
    "patronymic":"user1Changed",  
    "address":"user1Changedaddress",
    "email":"user1Changed@gmail.com",
    "number":"+79967348130",
    "password":"user1user1Changed"  
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
* **DELETE** `user/`    
  OUTPUT    
  *`Response 200`*   

### **VerifyEmail**    
* **POST** `verify-email/`     
  OUTPUT    
  *`Response 200`*    
     
* **POST** `accept-email/`    
  INPUT     
  ```json  
  {  
    "code":000000,
  }  
  ```   
  OUTPUT   
  *`Response 200`*  
  ```json   
  {    
    "detail":"Successfully confirmed" 
  }  
  ```   
