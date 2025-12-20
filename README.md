# Building a Modular and Scalable Flask Blueprint Architecture

**A modular and scalable mini “production-ready” Flask skeleton for any project**

---

## Set up enviroment & requirements

```
$ cd project_folder
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install Flask
(venv) $ flask run
```

---

## 📁 **Project Structure**

```
project_folder/
|
+-- app.py                               # Main entry point (creates Flask app, registers blueprints, runs server)
|
+-- config.py                            # Global configuration (DEBUG, SECRET_KEY, database paths, etc.)
|
+-- core/                                # App-wide global infrastructure (app factory, error handling, extensions)
|   +-- __init__.py                      # Marks core as a package
|   +-- app_factory.py                   # Application factory (create_app) and blueprint registration
|   +-- extensions.py                    # Initialize shared extensions (db, login manager, etc.)
|   +-- errors.py                        # Global error handlers (404, 500)
|
+-- apps/                                # Modular isolated feature blueprints (home, addition)
|   |
|   +-- home/
|   |   +-- __init__.py                  # Home blueprint definition
|   |   +-- routes.py                    # Home routes (views)
|   |   +-- templates/home/
|   |       +-- view.html                # Home page template
|   |
|   +-- addition/
|   |   +-- __init__.py                  # Addition blueprint definition
|   |   +-- routes.py                    # Addition logic and routes
|   |   +-- templates/addition/
|   |       +-- view.html                # Addition page template
|   |
|   +-- <other-modules>/                 # Future blueprints (subtraction, multiplication, etc.)
|
+-- templates/                           # Global/shared templates
|   +-- base.html                        # Main layout (navbar, footer) with dynamic {{ title }}
|   +-- 404.html                         # Global 404 error page
|
+-- static/                              # Static assets
    +-- css/
    |   +-- style.css                    # Global styles
    +-- img/
        +-- favicon.png                  # Site favicon
```

---

### 1️⃣ **Separation of concerns**

* `core/` → global infrastructure (app factory, error handling, extensions).
* `apps/<module>/` → isolated feature blueprints (`home`, `addition`).
* `templates/` → global layouts (`base.html`) with dynamic `{{ title }}` and error pages (`404.html`).
* `static/` → CSS, JS, images.

Everything has a **clear place** — no spaghetti code in `app.py`.

---

### 2️⃣ **Scalability**

* Adding a new module is **copy + rename + register**.
* Blueprints allow you to **group related routes and templates**.
* You can have dozens of features without cluttering the main app.

---

### 3️⃣ **Maintainability**

* Routes, templates, and logic are isolated — easier to debug.
* Global things (like error pages or extensions) are centralized in `core/`.
* Team collaboration becomes much simpler.

---

### 4️⃣ **Flexibility**

* You can easily add databases, login systems, or APIs via `core/extensions.py`.
* URL structure is clean and configurable via `url_prefix`.
* Templates and static files can be organized per module or globally.
* Dynamic page titles supported via `{{ title }}` in `base.html`.

---

### ✅ Summary

This is **exactly the approach used in professional Flask projects**:

* Minimal `app.py` as entry point
* Core infrastructure separated
* Modular blueprints for features
* Clean template and static structure
* Dynamic titles with `{{ title }}` in templates

This setup is **fully correct for web development** — small, clean, and scales nicely, which is the whole advantage of Flask over “everything in one file” frameworks.

---

## 📄 License

This project is for **learning and educational use**.
Feel free to explore, extend, and build upon it.
