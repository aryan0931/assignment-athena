
# 🌐 Chronos Global Numeral Explorer

An interactive web application to **learn, explore, and convert** ancient numeral systems.  
This project brings together history, mathematics, and modern UI/UX design to help users understand the logic behind four major ancient systems:

- **Roman**
- **Mayan**
- **Babylonian**
- **Chinese**

Users can explore detailed explanations, convert numbers interactively, and test their knowledge through practice puzzles.

---

## ✨ Features

### ✅ **1. Interactive Number Converter**
Convert Arabic numbers into:
- Roman numerals  
- Mayan base-20 symbols  
- Babylonian base-60 wedge notation  
- Chinese character numerals  

Each conversion includes a **symbolic breakdown** for learning.

---

### 📚 **2. Numeral Systems Library**
A clean, well-structured library page explaining:
- Historical background  
- Symbol rules  
- Positional structure  
- Comparisons with modern decimal system  

---

### 🧩 **3. Practice Zone**
A fun, interactive puzzle area to:
- Identify symbols  
- Perform quick conversions  
- Strengthen memory and pattern recognition  

---

### 🎨 **4. Modern UI / UX**
- Dark cosmic theme  
- Cyan + gold accents  
- Glassmorphic navbar  
- Smooth transitions and fade-ins  
- Fully responsive (desktop/tablet/mobile)  

---

## 📁 Project Structure

### **Backend — Flask (Python)**

```

app.py
numeral_logic/
├── converter.py     # Unified interface
├── roman.py         # Roman numeral conversion
├── mayan.py         # Mayan base-20 conversion
├── babylonian.py    # Babylonian base-60 conversion
└── chinese.py       # Chinese numeral conversion

```

- `app.py` handles routes & API endpoints.
- Each numeral system is implemented in a clean, modular Python file.

---

### **Frontend — HTML / CSS / JavaScript**

```

templates/
├── base.html        # Master template
├── index.html       # Landing page
├── library.html     # System catalogue
├── converter.html   # Converter tool
└── practice.html    # Quiz area

static/
├── css/style.css    # Modern dark theme
└── js/main.js       # API handling + DOM updates

````

---

## ✔️ Verification & Testing

### **Automated Tests (`test_logic.py`)**

| System       | Input | Output             | Status |
|--------------|--------|--------------------|--------|
| Roman        | 2024   | `MMXXIV`           | ✔️ |
| Mayan        | 5      | 1 Bar              | ✔️ |
| Babylonian   | 61     | 1 (60s) + 1 (1s)   | ✔️ |
| Chinese      | 123    | `一百二十三`       | ✔️ |

### **Manual Testing**
- All navigation routes behave as expected  
- Converter outputs correct values consistently  
- Responsive on mobile/tablet/desktop  
- Smooth animations and visual consistency validated  

---

## 🛠️ Installation & Usage

### **1. Clone the repository**
```bash
git clone <your-repo-url>
cd chronos-numeral-explorer
````

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

### **3. Run the application**

```bash
python app.py
```

### **4. Open your browser**

```
http://127.0.0.1:5000/
```

---

## 📌 Roadmap / Future Enhancements

* Expand Chinese numeral support for **100,000+** values
* Add more puzzles and gamified learning modules
* Introduce a **Reverse Converter** (Ancient → Arabic)
* Add audio or animation-based learning cues

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests to expand numeral systems, improve UI, or add new features.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

Built with:

* Python & Flask
* HTML5, CSS3, JavaScript
* Passion for mathematics, history, and modern UI design


```
```
