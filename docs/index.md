# **API documentation**


## **Main chapters**
* [User API documentation](./users.md)
* [Organization API documentation](./organizations.md)
* [Session API documentation](./sessions.md)
* [Order API documentation](./orders.md)
* [Client API documentation](./clients.md)
* [Verify-Info API documentation](./verify_info.md)

## **Token error**
Если в заголовке вы вставили некорректный токен или токен с истёкшим сроком службы, то выдаст  
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
