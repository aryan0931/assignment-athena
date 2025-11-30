Global Numeral Systems Explorer

I have successfully built the **Chronos Global Numeral Explorer**, an interactive web application that teaches users about Roman, Mayan, Babylonian, and Chinese numeral systems.

## Changes

### Backend (Flask & Python)
- **[app.py](file:///Users/aryanyadav/Assignment az/app.py)**: The main Flask application handling routes and API endpoints.
- **[numeral_logic/](file:///Users/aryanyadav/Assignment az/numeral_logic/)**: A package containing the conversion logic for all supported systems.
    - `roman.py`: Handles Roman numeral conversion.
    - `mayan.py`: Handles Base-20 Mayan conversion (dots/bars).
    - `babylonian.py`: Handles Base-60 Babylonian conversion (wedges).
    - `chinese.py`: Handles Chinese character numerals.
    - `converter.py`: A unified interface for easy access.

### Frontend (HTML/CSS/JS)
- **[templates/](file:///Users/aryanyadav/Assignment az/templates/)**:
    - `base.html`: The master template with a responsive navigation bar and footer.
    - `index.html`: A premium landing page with a "Wow" factor hero section.
    - `library.html`: A catalog of the numeral systems with historical context.
    - `converter.html`: An interactive tool to convert numbers and see the breakdown.
    - `practice.html`: A puzzle zone to test knowledge.
- **[static/](file:///Users/aryanyadav/Assignment az/static/)**:
    - `css/style.css`: Contains the "Cosmic/History" theme with dark mode, gradients, and animations.
    - `js/main.js`: Handles the API communication and dynamic DOM updates.

## Verification Results

### Automated Logic Tests
I ran a test script `test_logic.py` to verify the core algorithms:
- **Roman**: `2024` -> `MMXXIV` (Correct)
- **Mayan**: `5` -> 1 Bar (Correct)
- **Babylonian**: `61` -> 1 (60s place) + 1 (1s place) (Correct)
- **Chinese**: `123` -> `一百二十三` (Correct)

### Manual Verification
- **Navigation**: Links between Home, Library, Converter, and Practice work as expected.
- **Responsiveness**: The CSS uses `flex` and `grid` to adapt to different screen sizes.
- **Aesthetics**: The application features a dark theme with gold/cyan accents, glassmorphism effects on the navbar, and smooth fade-in animations.

## Next Steps
- Expand the Chinese converter to handle larger numbers (e.g., 100,000+).
- Add more puzzles to the Practice Zone.
- Implement a "Reverse Converter" (Ancient -> Arabic).
