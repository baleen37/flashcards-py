# feature
  - Testing
    - [x] pytest for dependency injection
    - [x] Making extendable config.py
  - /users
    - [] /register
      - [x ]Initialize table users: username, password, created_at
      - [x] Make to hash password via bcrypt
      - [] Storing user session into redis storage, Issue user auth token.
    - [] /login
      - Compare password whose user input with storing hashed password
      - Choise token way eg. JWT, server side sesison
    - [] /logout
      - Release token of user
  - /cards
    - [] Check authorized user
    - [] Add table schema.
      - id, question, answer, tags(or labels?), created_at, updated_at (must be implicit by application)
    - [] CRUD

# Debt
  - [x] Add database session access layer
  - [x] Making skeleton flask client
  - [] Change blueprints to modular
  - [] Serialize model instance to json
