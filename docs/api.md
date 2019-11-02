[Sommaire](https://ursi-2020.github.io/Documentation/)

*[Go back](index.md)*

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

The price "prix" given in the json, is the price with the promotion already applied.

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
  "produits": [
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

Get all magasins promotions

**Service name** : `gestion-promotion`

**URL** : `promo/customers`

**Method** : `GET`

**Auth required** : NO

**Success Response code:** `200 OK`

The reduction is the one to applied for the shopphing cart in percent. All the other fields are provided by CRM.

**Content examples:**

```json
[
  {
    "IdClient": "a14e39ce-e29e-11e9-a8cb-08002751d198",
    "Nom": "Jacquie",
    "Prenom": "Bloggs",
    "Credit": "42,00",
    "Paiement": 0,
    "NbRefus": 5,
    "Arembourser": 0,
    "Compte": "BKN1CST53",
    "Age": 29,
    "Sexe": "F",
    "Email": "bibalou@wanadoo.fr",
    "carteFid": 33,
    "reduction": 5
  },
  {
    "IdClient": "a14f4a08-e29e-11e9-a8cb-08002751d198",
    "Nom": "Michelle",
    "Prenom": "Bigoudi",
    "Credit": "69,00",
    "Paiement": 3,
    "NbRefus": 5,
    "Arembourser": 0,
    "Compte": "",
    "Age": 54,
    "Sexe": "H",
    "Email": "lalaland@gmail.com",
    "carteFid": 42,
    "reduction": 20
  }
]
```
