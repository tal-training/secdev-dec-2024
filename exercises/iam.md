**Exercise: Designing an Identity and Access Management (IAM) System**

**Scenario:** You are the security architect for a large e-commerce company that sells products online. The
company has multiple departments, including sales, marketing, customer support, and finance.

**Requirements:**

1. The system should support multiple authentication protocols (e.g., OAuth 2.0, OpenID Connect).
2. Users can be assigned multiple roles with varying levels of access.
3. Access control mechanisms should be implemented to restrict access to sensitive resources based on user roles
and permissions.
4. The system should provide a self-service password reset feature for users.
5. Audit logs should be maintained to track changes made to user accounts and access permissions.

**Design Exercise:**

Please answer the following questions in 30 minutes:

1. **User Management:** Describe how you would manage user identities, including onboarding, offboarding, and
managing user profiles.
        * How would you store user data (e.g., username, email, password)?
        * What measures would you take to ensure the integrity and authenticity of user data?
2. **Role-Based Access Control:** Design an approach for assigning roles to users with varying levels of access.
        * What types of roles would you create (e.g., admin, sales, customer support)?
        * How would you assign permissions to each role?
3. **Authentication Protocols:** Choose two authentication protocols (e.g., OAuth 2.0, OpenID Connect) and
describe how you would implement them in the IAM system.
        * What benefits do these protocols offer?
        * How would you handle scenarios where users have multiple identities (e.g., Facebook login)?
4. **Self-Service Password Reset:** Design a self-service password reset feature for users.
        * How would you store user passwords securely?
        * What measures would you take to prevent brute-force attacks on the system?
5. **Audit Logs:** Describe a logging mechanism that could be implemented to track changes made to user accounts
and access permissions.
        * What types of logs would you collect (e.g., login attempts, password resets)?
        * How would you store and manage these logs?
