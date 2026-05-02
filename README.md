# Recipe API

A robust, production-ready Django REST Framework backend for managing recipes, ingredients, and tags.

## How to Run the Project

Follow these steps to run the API locally on your Windows machine.

### 1. Activate the Virtual Environment
Open your command prompt or PowerShell and navigate to the project folder (`c:\Users\Dell\Desktop\Food recepi`). Then run:
```powershell
.\venv\Scripts\activate
```

### 2. Verify Environment Variables
Ensure the `.env` file exists in the root directory (alongside `manage.py`). It should contain:
```env
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 3. Apply Migrations
If you haven't already, apply the database schema:
```powershell
python manage.py migrate
```

### 4. Create a Superuser (Optional but Recommended)
To access the Django Admin Panel, create an admin account:
```powershell
python manage.py createsuperuser
```
*(It will prompt you for an email, name, and password).*

### 5. Start the Server
Run the local development server:
```powershell
python manage.py runserver
```

---

## How to Get Output & Test the API

Once the server is running, it will be accessible at **http://127.0.0.1:8000/**.

### Method A: The Django Browsable API (Easiest)
Because we are using Django REST Framework, you can test the API directly in your web browser!
1. Open your browser and go to: `http://127.0.0.1:8000/api/recipe/recipes/`
2. You will see a web interface where you can view data and even submit JSON payloads.

### Method B: Using Postman
Postman is highly recommended for testing authenticated endpoints.

**Step 1: Create a User**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/user/create/`
- **Body** (Raw JSON):
  ```json
  {
      "email": "test@example.com",
      "password": "password123",
      "name": "Test User"
  }
  ```

**Step 2: Get your Token**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/user/token/`
- **Body** (Raw JSON):
  ```json
  {
      "email": "test@example.com",
      "password": "password123"
  }
  ```
- *Copy the `token` string returned in the response.*

**Step 3: Access Authenticated Endpoints**
- **Method**: `GET` or `POST`
- **URL**: `http://127.0.0.1:8000/api/recipe/recipes/`
- **Headers**:
  - Key: `Authorization`
  - Value: `Token <paste-your-token-here>`
  
Now you can fully interact with the recipes, tags, and ingredients!

### Key Endpoints
- **POST** `/api/user/create/` - Register a user
- **POST** `/api/user/token/` - Get an auth token
- **GET/PATCH** `/api/user/me/` - Manage your profile
- **GET/POST/PATCH/DELETE** `/api/recipe/recipes/` - Manage recipes
- **GET/POST/PATCH/DELETE** `/api/recipe/tags/` - Manage tags
- **GET/POST/PATCH/DELETE** `/api/recipe/ingredients/` - Manage ingredients
- **POST** `/api/recipe/recipes/{id}/upload-image/` - Upload a recipe image
