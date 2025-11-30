from flask import Flask, render_template, request, jsonify
from numeral_logic import ConverterEngine

app = Flask(__name__)
converter = ConverterEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/converter')
def converter_page():
    return render_template('converter.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/api/convert', methods=['POST'])
def api_convert():
    data = request.json
    number = data.get('number')
    system = data.get('system')
    
    if not number or not system:
        return jsonify({"error": "Missing number or system parameter"}), 400
    
    result = converter.convert(number, system)
    return jsonify(result)

@app.route('/api/puzzle', methods=['GET'])
def api_puzzle():
    # Simple mock puzzle for now
    puzzle = {
        "question": "If '••' is 2 and '—' is 5 in Mayan, what is '••—'?",
        "options": ["6", "7", "8", "10"],
        "answer": "7",
        "explanation": "Two dots (2) + One bar (5) = 7."
    }
    return jsonify(puzzle)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
