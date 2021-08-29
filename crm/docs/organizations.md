# **Organizations API** - **`/organizations/`**   
    
## **Organizations**    
* **POST** `organization/`    
  INPUT    
  ```json  
  {  
    "name":"Organization",
    "description":"The description",
    "address":"ulitsa",
    "creator":1 
  }  
  ```    
  OUTPUT    
  *`Response 201`*    
  ```json  
  {  
    "name":"Organization",
    "description":"The description",
    "address":"ulitsa",
    "creator":1 
  }
  ```    
* **GET** `organization/`    
  OUTPUT    
  *`Response 200`*    
  ```json  
  [  
    { 
      "name":"Organization",
      "description":"The description",
      "address":"ulitsa",
      "creator":1 
    }
  ]
  ```    
  This view method need the access token in Authorization key in headers in format like this(Bearer access or Token access)    
* **PATCH** `organization/`    
  INPUT    
  ```json  
  {  
    "name":"OrganizationChanged",
    "description":"The descriptionChanged",
    "address":"ulitsaChanged",
    "creator":1 
  }  
  ```    
  OUTPUT    
  *`Response 200`*  
  ```json  
  {  
    "success":{
      "Name":"Name successfully changed", 
      "Description":"Description successfully changed",
      "...":"",
    },
    "error":{}
  }  
  ```  
  This view method need the access token in Authorization key in headers in format like this(Bearer access or Token access)  
* **DELETE** `organization/`    
  INPUT    
  ```json  
  {  
    "organization":1
  }  
  ```    
  OUTPUT    
  *`Response 200`*  
    
## **Organization numbers**  
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)     
* **POST** `number/`    
  INPUT    
  ```json   
  {  
    "number":"+79999999999",    
    "organization":1  
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "number":"+79999999999",    
    "organization":1  
  }  
  ```  
* **GET** `number/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1 ,
      "number":"+79999999999",
      "organization":1
    }
  ]
  ```    
* **GET** `number-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1 ,
      "number":"+79999999999",
      "organization":1
    }
  ]
  ```  
* **PATCH** `number/`    
  INPUT    
  ```json   
  {  
    "number":1,
    "new_number":"+79999999998",
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":"Number successfully changed"
  },
  ```  
* **DELETE** `number/`    
  INPUT    
  ```json   
  {  
    "number":1,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
    
## **Organization links**    
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)     
* **POST** `link/`    
  INPUT    
  ```json   
  {  
    "name":"vk",
    "link":"http://vk.com",    
    "organization":1  
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "name":"vk",
    "link":"http://vk.com",    
    "organization":1  
  }  
  ```  
* **GET** `link/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1,
      "name":"vk",
      "link":"http://vk.com",    
      "organization":1  
    }
  ]
  ```    
* **GET** `link-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1,
      "name":"vk",
      "link":"http://vk.com",    
      "organization":1  
    },
    { 
      "id":2,
      "name":"vkreverse",
      "link":"http://vkrev.com",    
      "organization":1  
    }
  ]
  ```    
* **PATCH** `link/`    
  INPUT    
  ```json   
  {  
    "link":1,    
    "organization":1,
    "new_link":"https://vk.comChanged"
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":"Link successfully changed"
  },
  ```  
* **DELETE** `link/`    
  INPUT    
  ```json   
  {  
    "link":1,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   

## **Members**
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)         
* **POST** `member/`    
  INPUT    
  ```json   
  {  
    "user":2,
    "role":2,    
    "organization":1  
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "user":2,
    "role":2,    
    "organization":1  
  }  
  ```  
* **GET** `member/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1,
      "user":2,
      "role":2,    
      "organization":1  
    }
  ]
  ```    
* **GET** `member-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1,
      "user":2,
      "role":2,    
      "organization":1  
    },
  ]
  ```    
* **PATCH** `member/`    
  INPUT    
  ```json   
  {  
    "member":2,    
    "role":3,
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":"Role successfully changed"
  },
  ```   
* **DELETE** `member/`    
  INPUT    
  ```json   
  {  
    "member":1,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   

## **Roles**
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)         
* **POST** `role/`    
  INPUT    
  ```json   
  {  
    "name":"Test role",
    "permissions":[1,2,3],    
    "organization":1  
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "name":"Test role",
    "permissions":[1,2,3],    
    "organization":1  
  }  
  ```  
* **GET** `role-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
    "id":1,
    "name":"Test role",
    "permissions":[1,2,3],    
    "organization":1  
    },
    { 
    "id":2,
    "name":"Test role2",
    "permissions":[1,3],    
    "organization":1  
    }
  ]
  ```    
* **GET** `perms-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
      "id":1,
      "name":"Cand add client",
      "codename":"client_create",  
    },
  ]
  ```    
* **PATCH** `role/`    
  INPUT    
  ```json   
  {  
    "role":1,    
    "new_permissions":[1],
    "organization":1,
    "name":"RoleNameChanged"
  }  
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":{
      "Name":"Name successfully changed",
      "Permissions":"Permissions successfully changed"
  },
  ```   
* **DELETE** `role/`    
  INPUT    
  ```json   
  {  
    "role":1,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*    

## **Service**
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)         
* **POST** `service/`    
  INPUT    
  ```json   
  {  
    "name":"Test Service",
    "address":"ulitsa",    
    "number":"+79968379274",    
    "organization":1  
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "name":"Test Service",
    "address":"ulitsa",    
    "number":"+79968379274",    
    "organization":1  
  }  
  ```  
* **GET** `service/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
    "id":1,
    "name":"Test Service",
    "address":"ulitsa",    
    "number":"+79968379274",    
    "organization":1  
    },
    { 
    "id":2,
    "name":"Test Service2",
    "address":"ulitsa2",    
    "number":"+79968379275",    
    "organization":2  
    }
  ]
  ```    
* **GET** `service-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
    "id":1,
    "name":"Test Service",
    "address":"ulitsa",    
    "number":"+79968379274",    
    "organization":1  
    },
  ]
  ```    
* **PATCH** `service/`    
  INPUT    
  ```json   
  {  
    "name":"Service Chagned",    
    "number":"+79997775552",
    "address":"ulitsaChanged",
    "organizations":1,
    "service"
  } 
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":{
      "Name":"Name successfully changed",
      "Number":"Number successfully changed",
      "...":""
  },
  ```   
* **DELETE** `service/`    
  INPUT    
  ```json   
  {  
    "service":1,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   

## **Client**
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)         
* **POST** `client/`    
  INPUT    
  ```json   
  {  
    "surname":"client1",   
    "name":"client1@gmail.com",    
    "patronymic":"client1",  
    "address":"uclient11address",
    "email":"client1@gmail.com",
    "number":"+79967344117",
    "password":"client1client1",  
    "organization":1
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "surname":"client1",   
    "name":"client1@gmail.com",    
    "patronymic":"client1",  
    "address":"uclient11address",
    "email":"client1@gmail.com",
    "number":"+79967344117",
    "organization":1
  }  
  ```  

* **GET** `client-all/1/`       
  OUTPUT    
  *`Response 200`*   
  ```json  
  [  
    { 
    "id":1,
    "surname":"client1",   
    "name":"client1@gmail.com",    
    "patronymic":"client1",  
    "address":"uclient11address",
    "email":"client1@gmail.com",
    "number":"+79967344117",
    "organization":1
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
    "address":"uclient11addressChanged",
    "email":"client1Changed@gmail.com",
    "number":"+79963344119",
    "image":"/new/img/",
    "organization":1
  } 
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":{
      "Surname":"Surname successfully changed",
      "Number":"Number successfully changed",
      "...":""
  },
  ```   
* **DELETE** `client/`    
  INPUT    
  ```json   
  {  
    "client":1,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*   

## **Order**
  This view need the access token in Authorization key in headers in format like this(Bearer access or Token access)         
* **POST** `order/`    
  INPUT    
  ```json   
  {  
    "description":"order",    
    "creator":1,  
    "executor":2,
    "client":1,
    "service":1,
  }  
  ```     
  OUTPUT    
  *`Response 201`*   
  ```json  
  {  
    "order_code":1232,
    "description":"order",    
    "creator":1,  
    "executor":2,
    "client":1,
    "service":1,
  }  
  ```  
* **GET** `order-all/1/`       
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
    }  
  ]
  ```    
* **PATCH** `order/`    
  INPUT    
  ```json   
  {  
    "description":"orderChanged",    
    "executor":1,
    "service":2,
  } 
  ```   
  OUTPUT    
  *`Response 200`*   
  ```json  
  {
    "success":{
      "Description":"Description successfully changed",
      "Executor":"Executor successfully changed",
      "...":""
  },
  ```   
* **POST** `order-block/`    
  INPUT    
  ```json   
  {  
    "order_code":1232,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*  

* **DELETE** `order/`    
  INPUT    
  ```json   
  {  
    "order_code":1232,
    "organization":1  
  }  
  ```   
  OUTPUT    
  *`Response 200`*  
