

#  User Authentication API  Flask + JWT + MongoDB

This is a RESTful API for user registration, login, and profile retrieval using **Flask**, **JWT**, and **MongoDB**.

---

##  Base URL

```
http://localhost:5000
```

All routes are prefixed with `/auth`.

---

##  Authentication

This API uses **JWT (JSON Web Tokens)** for protected routes. You will receive a token after login and must include it in the `Authorization` header for routes like `/auth/profile`.

---

##  Endpoints

### `POST /auth/register`

Registers a new user.

#### Request Body

```json
{
    "name":"Ayomide",
  "email": "ayomi@gmail.com",
  "password": "ayomi124qyu"
}
```

#### Response

```json
{
  "message": "User registered successfully"
}
```

#### Errors

- `400 Bad Request`: Missing fields or email already exists

---

###  `POST /auth/login`

Authenticates the user and returns a JWT.

#### Request Body

```json
{
  "email": "ayomi@gmail.com",
  "password": "ayomi124qyu"
}
```

#### Response

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDgzNDI5MywianRpIjoiNTUzNzlmMGMtMmJlNS00MzM5LWIyNTUtZTYxMmEzOGNiMGQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY4NWI5NWE0ZWY3Y2E2ZmVkNWZjNjU1MyIsIm5iZiI6MTc1MDgzNDI5MywiY3NyZiI6ImEwZDU0YzNiLTZiOTQtNDQ4NC05MDg0LWEyNGViNTBlZmRiNiIsImV4cCI6MTc1MDgzNTE5M30.niuTh7Uu5HLnauKepTys9q0-7C-fjCpWO-mk84vIS0Q"
}
```

#### Errors

- `401 Unauthorized`: Invalid credentials

---

### `GET /auth/profile`

Returns the authenticated user's profile.

#### Headers

```
Authorization: Bearer <{eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDgzNDI5MywianRpIjoiNTUzNzlmMGMtMmJlNS00MzM5LWIyNTUtZTYxMmEzOGNiMGQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY4NWI5NWE0ZWY3Y2E2ZmVkNWZjNjU1MyIsIm5iZiI6MTc1MDgzNDI5MywiY3NyZiI6ImEwZDU0YzNiLTZiOTQtNDQ4NC05MDg0LWEyNGViNTBlZmRiNiIsImV4cCI6MTc1MDgzNTE5M30.niuTh7Uu5HLnauKepTys9q0-7C-fjCpWO-mk84vIS0Q
}>
```

#### Response

```json
{
    "id": "685b95a4ef7ca6fed5fc6553",
    "name": "Ayomide",
    "email": "ayomi@gmail.com"
}
```

#### Errors

- `401 Unauthorized`: Missing or invalid token
- `404 Not Found`: User not found

---



---

## Environment Variables

I created `.env` file:

```
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
MONGO_URI=mongodb://localhost:27017/user-authentication-db
```

---

##  Technologies

- Flask 3.1.1
- Flask-JWT-Extended 4.7.1
- Flask-PyMongo 2.3.0
- PyMongo 4.13.2
- Python-Dotenv 1.1.1

---