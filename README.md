# 🍔 Foodie Crush - Premium Food Delivery SPA

Foodie Crush is a modern, high-performance Food Delivery Single Page Application (SPA) built with a Django REST Framework backend and a Vanilla JS/CSS frontend. It features a stunning "Orange & White" premium design, user-scoped data persistence, and a fully functional recipe marketplace.

## 🚀 Live Deployment (Vercel)
This project is configured for seamless deployment on **Vercel**.

### 🛠️ One-Click Setup for Vercel:
1. **Environment Variables**: You must add the following variables in your Vercel Dashboard:
   - `SECRET_KEY`: (A random 50-character string)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `.vercel.app`
2. **Build Settings**: Vercel will automatically detect the `vercel.json` and `build.sh` files provided in this repo.

## ✨ Key Features
- **Premium UI**: Vibrant "Orange & White" theme with glassmorphism and smooth animations.
- **User Accounts**: Full Login/Signup flow powered by Django Knox tokens.
- **Personalized Experience**: Cart, Favourites, and Addresses are private to each logged-in user.
- **Smart Menu**: Categorized food items (Delivery, Dining, Nightlife) with accurate imagery.
- **Instant Search**: Debounced real-time search across hundreds of recipes.
- **Mobile First**: Fully responsive design for iOS and Android browsers.

## 📦 Tech Stack
- **Backend**: Python, Django, Django REST Framework, WhiteNoise.
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), JavaScript (ES6+).
- **Storage**: LocalStorage (Client State) + SQLite (Backend Data).

## 🛠️ Local Development
1. Clone the repo: `git clone https://github.com/Ananmai/Food-Recipe.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

---
*Created with ❤️ by Ananmai*
