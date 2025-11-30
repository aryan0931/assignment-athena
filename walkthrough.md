
# **📘 Project Walkthrough — Chronos Global Numeral Explorer**

The **Chronos Global Numeral Explorer** is an interactive learning platform designed to help users explore and understand four ancient numeral systems—**Roman, Mayan, Babylonian, and Chinese**. This walkthrough explains how the project works end-to-end, covering the UI flow, backend structure, logic modules, and testing strategy.

---

## **1️⃣ Overview**

This application combines historical numerals with modern web design. It allows users to:

* Learn about each numeral system
* Convert numbers interactively
* Practice through timed or random puzzles
* Understand the logic behind symbolic representations

The project is built using **Flask**, **modular Python logic**, and a **responsive UI**.

---

## **2️⃣ Project Flow**

Below is the general user flow of the application:

1. **Landing Page**
   Users start at a modern, animated homepage with navigation options.

2. **Numeral Systems Library**
   Provides background, rules, and examples for each numeral system.

3. **Interactive Converter**
   Converts Arabic numbers into Roman, Mayan, Babylonian, or Chinese numerals.

4. **Practice Zone**
   Lets users test their learning through quizzes and symbol-identification tasks.

5. **Results Display**
   Shows symbolic breakdowns and explanations for better understanding.

---

## **3️⃣ Frontend Walkthrough**

The frontend is structured using HTML templates and styled with a dark, cosmic-themed CSS design.

### **Templates**

```
templates/
├── base.html
├── index.html
├── library.html
├── converter.html
└── practice.html
```

### **Key UI Features**

* Glassmorphic navigation bar
* Smooth transitions and fade-in effects
* Responsive layout for mobile and desktop
* Dynamic content updates via JavaScript

The **main.js** file handles user input, fetch requests, and DOM updates for conversions and quizzes.

---

## **4️⃣ Backend Walkthrough**

The backend uses Flask to route pages and handle API calls.

### **Routes**

* `/` → Landing page
* `/library` → Numeral library
* `/convert` (POST) → Returns converted numeral output
* `/practice` → Quiz interface

### **Core Backend File**

`app.py`
Handles:

* Routing
* Loading logic modules
* Processing conversion requests
* Sending JSON responses to the frontend

---

## **5️⃣ Logic Modules (numeral_logic/)**

Each numeral system is implemented in its own file, making the architecture highly modular.

```
numeral_logic/
├── converter.py
├── roman.py
├── mayan.py
├── babylonian.py
└── chinese.py
```

### **Role of Each Module**

* **roman.py** → Implements additive/subtractive Roman rules
* **mayan.py** → Base-20 positional conversion using bars & dots
* **babylonian.py** → Base-60 cuneiform-inspired grouping
* **chinese.py** → Hierarchical character composition

`converter.py` serves as the unified interface that selects the appropriate conversion logic.

---

## **6️⃣ Practice Zone Walkthrough**

The Practice Zone generates random questions to reinforce learning.

It includes:

* Symbol recognition
* Quick conversions
* Multiple-choice challenges

The logic ensures variation so that users do not repeat identical problems.

---

## **7️⃣ Testing**

The project includes automated tests located in:

```
test_logic.py
```

These tests verify:

* Correct Roman numeral generation
* Accurate base-20 Mayan representation
* Proper Babylonian base-60 positional output
* Valid Chinese numeral formation

Testing ensures historical correctness and predictable output across systems.

---

## **8️⃣ Running the Application**

```bash
git clone <repository-url>
cd assignment-athena
pip install -r requirements.txt
python app.py
```

Access the app at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## **9️⃣ Key Takeaways**

* Fully modular architecture
* Clear separation of logic and presentation
* Accurate mathematical representation of ancient numeral systems
* Strong UI/UX focus for learning and exploration
* Expandable design for future numeral systems or gamified features

---
