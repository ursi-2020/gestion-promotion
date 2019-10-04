[Sommaire](https://ursi-2020.github.io/Documentation/)

# Gestion-promotions-app

This application manage all data to create promotions.

# Home Page

The gestion-promotion home page contains following elements :
- Tables registering all promotions
    - one for ecommerce promotions
    - one for magasin promotions
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

**Content examples:**

```json
{
  "produits": [
    {
      "id": 3291,
      "codeProduit": "X1-1",
      "familleProduit": "Console",
      "descriptionProduit": "Console:P3-1",
      "quantiteMin": 5,
      "packaging": 1,
      "prix": 154,
    },
    {
      "id": 3290,
      "codeProduit": "X1-0",
      "familleProduit": "Frigos",
      "descriptionProduit": "Frigos:P1-0",
      "quantiteMin": 15,
      "packaging": 2,
      "prix": 424,
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

**Content examples:**

```json
{
  "produits": [
    {
      "id": 3291,
      "codeProduit": "X1-1",
      "familleProduit": "Console",
      "descriptionProduit": "Console:P3-1",
      "quantiteMin": 5,
      "packaging": 1,
      "prix": 154,
    },
    {
      "id": 3290,
      "codeProduit": "X1-0",
      "familleProduit": "Frigos",
      "descriptionProduit": "Frigos:P1-0",
      "quantiteMin": 15,
      "packaging": 2,
      "prix": 424,
    },
  ]
}
```

