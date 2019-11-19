[Sommaire](https://ursi-2020.github.io/Documentation/)

*[Go back](index.md)*

# Gestion-promotions-app

This application manage all data to create promotions.

# Home Page

The gestion-promotion home page contains following elements :
- Tables registering all promotions
    - one for ecommerce promotions
    - one for magasin promotions
    - one for targeted clients
    - one for targeted products of clients
- A table registering all clients given by CRM
- Tables registering all products given by catalogue-produit
    - one for all products
    - one for ecommerce products
    - one for magasin products

# JSON API

## Get all promotions for ecommerce

**Service name** : `gestion-promotion`

**URL** : `promo/ecommerce`

**Method** : `GET`

**Auth required** : NO

**Success Response code:** `200 OK`

The price "prix" given in the json, is the price with the promotion already applied.

**Content examples:**

```json
{
  "promo": [
    {
      "id": 3291,
      "codeProduit": "X1-1",
      "familleProduit": "Console",
      "descriptionProduit": "Console:P3-1",
      "quantiteMin": 5,
      "packaging": 1,
      "prix": 225,
      "prixOriginel": 250,
      "reduction": 10,
    },
    {
      "id": 3290,
      "codeProduit": "X1-0",
      "familleProduit": "Frigos",
      "descriptionProduit": "Frigos:P1-0",
      "quantiteMin": 15,
      "packaging": 2,
      "prix": 230,
      "prixOriginel": 250,
      "reduction": 8,
    },
  ]
}
```

## Get all promotions for magasin

Get all magasins promotions

**Service name** : `gestion-promotion`

**URL** : `promo/magasin`

**Method** : `GET`

**Auth required** : NO

**Success Response code:** `200 OK`

The price "prix" given in the json, is the price with the promotion already applied.

**Content examples:**

```json
{
  "promo": [
    {
      "id": 3291,
      "codeProduit": "X1-1",
      "familleProduit": "Console",
      "descriptionProduit": "Console:P3-1",
      "quantiteMin": 5,
      "packaging": 1,
      "prix": 225,
      "prixOriginel": 250,
      "reduction": 10,
    },
    {
      "id": 3290,
      "codeProduit": "X1-0",
      "familleProduit": "Frigos",
      "descriptionProduit": "Frigos:P1-0",
      "quantiteMin": 15,
      "packaging": 2,
      "prix": 230,
      "prixOriginel": 250,
      "reduction": 8,
    },
  ]
}
```


## Get all user targeted promotions

Get all targeted promotions for cients

**Service name** : `gestion-promotion`

**URL** : `promo/customers`

**Method** : `GET`

**Auth required** : NO

**Success Response code:** `200 OK`

The reduction is the one to applied for the shopphing cart in percent. All the other fields are provided by CRM.
'date' represents the date when the promotion was created.
**Content examples:**

```json
{
  "promo": [
        {
          "IdClient": "a14e39ce-e29e-11e9-a8cb-08002751d198",
          "date": "2019-10-09T18:03:45.408701Z",
          "reduction": 5
        },
        {
          "IdClient": "a14f4a08-e29e-11e9-a8cb-08002751d198",
          "date": "2019-10-09T18:03:45.408701Z",
          "reduction": 20
        }
  ]
}
```

## Get all user targeted promotions

Get all targeted products promotions for clients

**Service name** : `gestion-promotion`

**URL** : `promo/customersproducts`

**Method** : `GET`

**Auth required** : NO

**Success Response code:** `200 OK`

The reduction is the one to applied for the specified product for a specified client in percent. All the other fields are provided by CRM.
'date' represents the date when the promotion was created.
**Content examples:**

```json
{
  "promo": [
      {
        "date": "2019-10-09T18:03:45.408701Z",
        "IdClient": "a14e39ce-e29e-11e9-a8cb-08002751d198",
        "codeProduit": "X1-0",
        "quantity": 2,
        "reduction": 5
      },
      {
        "date": "2019-10-09T18:03:45.408701Z",
        "IdClient": "a14f4a08-e29e-11e9-a8cb-08002751d198",
        "codeProduit": "X1-0",
        "quantity": 1,
        "reduction": 20
      }
  ]
}
```

