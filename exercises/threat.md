
**Exercise: Designing a Threat Model**

**Scenario:** You are a developing a threat model for a RESTful API to manage user accounts, products, and orders.

**Sensitive API Endpoints:**

1. **User Account Management**
        * `POST /users` (create a new user account)
        * `GET /users/{id}` (view a specific user account)
        * `PUT /users/{id}` (update a specific user account)
        * `DELETE /users/{id}` (delete a specific user account)
2. **Product Management**
        * `POST /products` (create a new product)
        * `GET /products/{id}` (view a specific product)
        * `PUT /products/{id}` (update a specific product)
        * `DELETE /products/{id}` (delete a specific product)
3. **Order Management**
        * `POST /orders` (place a new order)
        * `GET /orders/{id}` (view a specific order)
        * `PUT /orders/{id}` (update a specific order)
        * `DELETE /orders/{id}` (cancel a specific order)

*** Steps ***

1. Draw a detaild architecture diagram of all the flows, components and relationships

2. For each component and relationship, identify the threats and mitigations

3. Summarize the model in a table 
