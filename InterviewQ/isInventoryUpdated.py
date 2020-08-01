#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:29:07 2020

@author: user
"""
'''

You own a small online store, consisting of its own 
site and a bunch of products presented on it. 
Recently you've made a backup of all the products 
from the database, but it quickly became outdated. 
Your task now is to find out the difference between 
the old outdated backup and the current database of 
products presented on the site.

Both the backup and the current site contain the products 
represented by the following fields:

id - the unique identifier of the product (integer);
name - the name of the product (string);
updated_at - timestamp of the last product update (integer);
price - the price of the product (positive integer);
manufacturer (optional) - the name of the manufacturer. 
This field is optional, and if it is not presented, then the 
product is considered to be produced locally, by yourself.
You are given an old backup of the list of products stored 
in the file /root/data/productsDump.json in JSON format. 
This file contains an array of products, each having the 
format described above.

For example, the JSON below is a valid old backup, where 
the first product is produced by the m2 company, and the 
second product was made locally by yourself.

[
  {
    "updated_at": 1565641893, 
    "price": 107, 
    "manufacturer": "m2", 
    "id": 1, 
    "name": "Product1"
  }, 
  {
    "updated_at": 1565641167, 
    "price": 70, 
    "id": 2, 
    "name": "Product2"
  }
]
To obtain information about the current products from the site, 
you are given an API endpoint. 
Use HTTP requests to obtain information about 
the current products from this endpoint.

API information

The API endpoint serves at http://127.0.0.1:8081.

It has 2 types of requests:

A GET request of the form http://127.0.0.1:8081/products?page=<page_id>, 
where <page_id> is an ID of the page on the site.
The view of the products on your site is paginated, 
so for one HTTP request you can obtain only the products on one page. 
Pages are numbered, starting from 0.

As a response, the JSON array with the list of product ids 
located on the requested page <page_id> is returned. 
If the provided page does not exist, you will receive a response
 with HTTP status code 404, and no products will be returned.

For example, for the request
http://127.0.0.1:8081/products?page=0
the response could look like
[3, 81, 10]

That means that page 0 on the current site contains products 
with ids 3, 81, and 10.

A GET request of the form http://127.0.0.1:8081/product_info?product_id=<product_id>
, where <product_id> is the id of the product for which you 
need detailed information.
This endpoint returns a JSON object, containing the 
information about the product with id <product_id>, with 
the fields described above. If the product with 
the provided id <product_id> does not exist, you will receive 
a response with HTTP status code 404, and no product 
information will be returned.

For example, the response for this endpoint may look like:

{
  "id": 1, 
  "name": "ProductName",
  "updated_at": 150000000, 
  "price": 100,
  "manufacturer": "ManufacturerCompanyName" 
}
It is guaranteed that the current site contains products only on pages 0, 1, ..., k, i.e. the pages represent a consecutive interval of integer values, starting from 0.

Task

Given the outdated backup and the REST API for retrieving information about the current products on the site, your task is to return all products that are presented either in the backup or on the current site, but not in both places. Two products are considered to be the same if they both have the same ids, the same names, and the same manufacturer (or both don't have this field).

For example, the following two products are considered to be the same.

{
  "id": 1, 
  "name": "ProductName",
  "updated_at": 150000001, 
  "price": 100, 
  "manufacturer": "ManufacturerCompanyName"
}
and

{
  "id": 1, 
  "name": "ProductName",
  "updated_at": 250000002,
  "price": 1, 
  "manufacturer": "ManufacturerCompanyName"
}
For the result, print all found products to the standard output, in the following format:

<id>_<productName>_<manufacturer> if manufacturer field is present;
<id>_<productName> if manufacturer field is not present.
Note: The products representations in the output should be sorted lexicographically, otherwise your solution won't pass.

Example

For the following old backup in /root/data/productsDump.json

[
  {
    "updated_at": 1565641893, 
    "price": 107, 
    "manufacturer": "m2", 
    "id": 1, 
    "name": "Product1"},
  {
    "updated_at": 1565641167, 
    "price": 70,
    "id": 2, 
    "name": "Product2"
  }, 
  {
    "updated_at": 1565641530, 
    "price": 39, 
    "id": 3, 
    "name": "Product3"
  }, 
  {
    "updated_at": 1565641764, 
    "price": 56, 
    "manufacturer": "m3", 
    "id": 4, 
    "name": "Product4"
  }
]
And the following responses from the API

page 0, http://127.0.0.1:8081/products?page=0
[1]
page 1, http://127.0.0.1:8081/products?page=1
[3, 5]
page 2, http://127.0.0.1:8081/products?page=2
[6]
page 3, http://127.0.0.1:8081/products?page=3
[4]
page 4, http://127.0.0.1:8081/products?page=4
HTTP status code: 404.

product 1, http://127.0.0.1:8081/product_info?product_id=1

{"updated_at": 1565641075, "price": 110, "manufacturer": "m2", "id": 1, "name": "Product1"}
product 3, http://127.0.0.1:8081/product_info?product_id=3
{"updated_at": 1565641635, "price": 48, "id": 3, "name": "Product3"}
product 4, http://127.0.0.1:8081/product_info?product_id=4
{"updated_at": 1565642015, "price": 28, "manufacturer": "m1", "id": 4, "name": "Product4"}, 
product 5, http://127.0.0.1:8081/product_info?product_id=5
{"updated_at": 1565641485, "price": 91, "id": 5, "name": "Product5"}, 
product 6, http://127.0.0.1:8081/product_info?product_id=6
{"updated_at": 1565641596, "price": 80, "id": 6, "name": "Product6"}
The following should be printed to the standard output:

2_Product2
4_Product4_m1
4_Product4_m3
5_Product5
6_Product6
The product with id = 1 appears in both the backup and the current site with the same id = 1, name = "Product1", and manufacturer = "m2".
The product with id = 2 appears only in the backup. Thus, it needs to be printed to the standard output.
The product with id = 3 appears in both backup and the current site with the same id = 3, name = "Product3" (and no manufacturer field).
The product with id = 4 appears only on the current site (manufacturer = "m1" on the current site and manufacturer = "m3" in the backup). Products are considered to be different, so they both need to be printed to the standard output.
The products with id = 5 and id = 6 appear only on the current site and both need to be printed to the standard output.
The product representations are sorted in lexicographical order and printed to the standard output.

[execution time limit] 12 seconds (py3)
'''