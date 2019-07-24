# gestion-promotion-app API exposure

This application manage all data from promotions.

It includes:
 - isFlat
 - flat
 - percent
 - productId

# JSON API

## Show all promotions

Get the details of all promotions registered in the promo_db

**Service name** : `gestion-promotion`

**URL** : `api/v1/promo`

**Method** : `GET`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
[
  {
    "id": 1,
    "isFlat": false,
    "flat": 0,
    "percent": 10,
    "productId": 1
  },
  {
    "id": 2,
    "isFlat": true,
    "flat": 10,
    "percent": 0,
    "productId": 2
  }
]
```

## Add a promotion

Register a new promotion in promo_db

**Service name** : `gestion-promotion`

**URL** : `api/v1/promo`

**Method** : `POST`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
arg={
    "isFlat": true,
    "flat": 10,
    "percent": 0,
    "productId": 2
    }
```

## Update a promotion

Update a promotion in promo_db

**Service name** : `gestion-promotion`

**URL** : `api/v1/promo`

**Method** : `PATCH`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
arg={
	"id": 1,
    "isFlat": true,
    "flat": 10,
    "percent": 0,
    "productId": 2
    }
```
## Delete a promotion

Delete a promotion in promo_db

**Service name** : `gestion-promotion`

**URL** : `api/v1/promo`

**Method** : `DELETE`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
arg={
	"id": 1,
    "isFlat": true,
    "flat": 10,
    "percent": 0,
    "productId": 2
    }
```

