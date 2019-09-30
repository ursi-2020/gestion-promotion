[Sommaire](https://ursi-2020.github.io/Documentation/)

# CRM-app

This application manage all data to create promotions.

It includes:
    - isFlat : Boolean in order to know if the promotion is an absolute reduction or a percentage
    - flat : Absolute promotion (Null if it's percentage)
    - percent : Percentage promotion (Null if it's absolute)
    - productId : Product id concerned by promotion

# Home Page

The gestion-promotion home page contains following elements :
- A table registering all promotions
- A table registering all clients given by CRM
- A table registering all products given by catalogue-produit


# JSON API

## Show all promotions

Get the details of all promotions registered in the gestion-promotions db named djandoapp_promotions

**Service name** : `gestion-promotion`

**URL** : `promo`

**Method** : `GET`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
[
  {
    "isFlat": true,
    "flat": 5.50,
    "percent": 0,
    "productId": 42,
  },
  {
    "isFlat": false,
    "flat": 0,
    "percent": 50,
    "productId": 69,
  }
]
```

## Create a promotion

Create a promotion registered in the gestion-promotions db named djandoapp_promotions

**Service name** : `gestion-promotion`

**URL** : `promo`

**Method** : `POST`

**Auth required** : NO


**Success Response code:** `200 OK`

## Put a promotion

Patch a promotion registered in the gestion-promotions db named djandoapp_promotions

**Service name** : `gestion-promotion`

**URL** : `promo`

**Method** : `PATCH`

**Auth required** : NO


**Success Response code:** `200 OK`

## Delete a promotion

Delete a promotion registered in the gestion-promotions db named djandoapp_promotions

**Service name** : `gestion-promotion`

**URL** : `promo`

**Method** : `DELETE`

**Auth required** : NO


**Success Response code:** `200 OK`


## Show all customers

Get the details of all customers registered in the gestion-promotions db named djandoapp_customers

**Service name** : `gestion-promotion`

**URL** : `admin/crm/indexcrm`

**Method** : `GET`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
[
  {
    "idClient": "a14e39ce-e29e-11e9-a8cb-08002751d198",
    "firstName": "Jacquie",
    "lastName": "Bloggs",
    "fidelityPoint": 42,
    "payment": 0,
    "account": "BKN1CST53"
  },
  {
    "idClient": "a14f4a08-e29e-11e9-a8cb-08002751d198",
    "firstName": "Michelle",
    "lastName": "Bigoudi",
    "fidelityPoint": 69,
    "payment": 3,
    "account": "BKN1BNT53"
  }
]
```

## Load customers

Load all customers from crm into gestion-promotion app.

**Service name** : `gestion-promotion`

**URL** : `admin/crm/loadcrm`

**Method** : `POST`

**Auth required** : NO

## Load customer by Id

Load a customer by Id from crm into gestion-promotion app.

**Service name** : `gestion-promotion`

**URL** : `admin/crm/loadcrmbyid`

**Method** : `POST`

**Auth required** : NO



## Show all products

Get the details of all products registered in the gestion-promotions db named djandoapp_products


**Success Response code:** `200 OK`**Service name** : `gestion-promotion`

**URL** : `admin/products/indexproducts`

**Method** : `GET`

**Auth required** : NO


**Success Response code:** `200 OK`

**Content examples:**


```json
[
  {
    "codeProduit": "a14f4a08",
    "familleProduit": "Kitchen",
    "descriptionProduit": "A knife",
    "quantiteMin": 5,
    "packaging": 4,
    "prix": 20,
  },
  {
    "codeProduit": "a1sdfsdfssdfdsf8",
    "familleProduit": "Kitchen",
    "descriptionProduit": "A knife",
    "quantiteMin": 5,
    "packaging": 4,
    "prix": 20,
  }
]
```

## Load products

Load all products from catalogue-produit into gestion-promotion app.

**Service name** : `gestion-promotion`

**URL** : `admin/products/loadproducts`

**Method** : `POST`

**Auth required** : NO


**Success Response code:** `200 OK`


## Refresh all the databases by the scheduler

Refresh all products & customers from catalogue-produit into gestion-promotion app.

**Service name** : `gestion-promotion`

**URL** : `admin/refresh`

**Method** : `POST`

**Auth required** : NO


**Success Response code:** `200 OK`


## Clear all the databases

Clear all products & customers & promotions in databases.

**Service name** : `gestion-promotion`

**URL** : `admin/clear`

**Method** : `POST`

**Auth required** : NO


**Success Response code:** `200 OK`
