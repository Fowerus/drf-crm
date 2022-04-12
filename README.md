# **API documentation**


## **Main chapters**
* [User API documentation](/docs/users.md)
* [Organization API documentation](/docs/organizations.md)
* [Order API documentation](/docs/orders.md)
* [Client API documentation](/docs/clients.md)
* [Handbook API documentation](/docs/handbook.md)
* [Market API documentation](/docs/market.md)
* [Marketplace API documentation](/docs/marketplace.md)

## **Token error**
If you inserted an incorrect token or an expired token in the header, it will give    
*`Response 401`*
```json
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```
## **403 error**
You actually need to add an organization field in your request body, except url related with user api functionality.  
If you will not do that the response will be 403 error.   

In the API documentation, the expression "empty request" means that a request with an organization field.   


## **About url variables**
Path-end ratio with necessary variables in path:  
``-l``: *int:organization_id* /  
``-r``: *int:object_id* / *int:organization_id* /  
``-c``: *None*  
``-ud``: *int:object_id* /  
``-u``: *int:object_id* /  
``-rud``: *int:object_id* /   
``-d``: *int:object_id* /

**Exception:**  
``user``: *int:object_id*  

## **Need to do**
* Change the logic of client login to the account  
* Add notification channels with celery    
* Rewrite documentation(Maybe using Swager UI)  
