# **Organizations API** - **`/organizations/`**   
    
## **Organization**    
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
    
## **Organization number**    
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
    
## **Organization link**    
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
* **GET** `member-all/1/`       
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

## **Organization link**    
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
* **GET** `member-all/1/`       
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
