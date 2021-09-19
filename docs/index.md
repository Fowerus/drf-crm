# **API documentation**


## **Main chapters**
* [User API documentation](./users.md)
* [Organization API documentation](./organizations.md)
* [Session API documentation](./sessions.md)
* [Order API documentation](./orders.md)
* [Client API documentation](./clients.md)
* [Verify-Info API documentation](./verify_info.md)

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
