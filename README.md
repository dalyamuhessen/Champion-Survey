# Dojo Champion Survey

A simple Flask web application that accepts a survey form submission and displays the results on a separate page.

---

## Assignment Objectives

- Practice creating a server with Flask from scratch
- Practice adding routes to a Flask app
- Practice having the client send data to the server via a POST form
- Practice having the server render a template using data provided by the client

---

## Project Structure

```
dojo_survey/
├── app.py
└── templates/
    ├── index.html
    └── result.html
```

---

## Setup & Installation

**1. Make sure Python 3 is installed**

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install Flask**
```bash
pip install flask
```

**4. Run the app**
```bash
python app.py
```

**5. Open your browser and visit**
```
http://localhost:5000
```

---

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays the survey form |
| `/result` | POST | Displays the submitted form data |

---

## Features

- **`/` (index)** — Renders a styled HTML form with:
  - Your Name (text input)
  - Dojo Location (dropdown)
  - Favorite Language (dropdown)
  - Comment — optional (textarea)

- **`/result`** — Receives the POST request, reads the form fields using `request.form.get()`, and renders them on a results page with a **Go Back** button.

---

## How It Works

```python
# app.py — reading form data sent via POST
name     = request.form.get('name', '')
location = request.form.get('location', '')
language = request.form.get('language', '')
comment  = request.form.get('comment', '')
```

> `request.form.get('field_name')` — safely reads a single form field.  
> `print(request.form)` — prints all submitted data to the terminal for debugging.

Form inputs must have a `name` attribute to be accessible from `request.form`.

