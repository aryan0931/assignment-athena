async function convertNumber() {
    const number = document.getElementById('inputNumber').value;
    const system = document.getElementById('systemSelect').value;
    const resultContainer = document.getElementById('resultContainer');
    const convertedValue = document.getElementById('convertedValue');
    const explanationList = document.getElementById('explanationList');

    if (!number) {
        alert('Please enter a number');
        return;
    }

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ number: parseInt(number), system: system }),
        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        resultContainer.style.display = 'block';
        explanationList.innerHTML = '';

        // Handle different return types
        if (system === 'mayan') {
            // Mayan returns a list of position objects
            let html = '<div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">';
            data.converted.forEach(pos => {
                // Simple visual representation
                let symbolHtml = '<div class="mayan-symbol" style="border: 1px solid #555; padding: 10px; width: 60px; text-align: center;">';
                if (pos.is_zero) {
                    symbolHtml += '<span>(Shell)</span>';
                } else {
                    // Dots
                    symbolHtml += '<div style="letter-spacing: 5px; font-size: 1.5rem;">' + '•'.repeat(pos.dots) + '</div>';
                    // Bars
                    symbolHtml += '<div style="display: flex; flex-direction: column; gap: 2px;">';
                    for (let i = 0; i < pos.bars; i++) {
                        symbolHtml += '<div style="width: 40px; height: 5px; background: white; margin: 0 auto;"></div>';
                    }
                    symbolHtml += '</div>';
                }
                symbolHtml += '</div>';
                html += symbolHtml;
            });
            html += '</div>';
            convertedValue.innerHTML = html;
        } else if (system === 'babylonian') {
            // Babylonian returns a list
            let html = '<div style="display: flex; gap: 10px; font-size: 2rem;">';
            data.converted.forEach(pos => {
                let symbol = '';
                if (pos.value === 0) symbol = 'Wait'; // Placeholder
                else {
                    // Tens (Corner wedges - <)
                    symbol += '&lt;'.repeat(pos.tens);
                    // Ones (Vertical wedges - Y)
                    symbol += 'Y'.repeat(pos.ones);
                }
                html += `<span>${symbol}</span>`;
            });
            html += '</div>';
            convertedValue.innerHTML = html;
        } else {
            // Roman and Chinese are strings
            convertedValue.textContent = data.converted;
        }

        // Explanation
        data.explanation.forEach(step => {
            const li = document.createElement('li');
            li.textContent = step;
            li.style.marginBottom = '0.5rem';
            explanationList.appendChild(li);
        });

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during conversion.');
    }
}

let currentPuzzle = null;

async function loadPuzzle() {
    const questionEl = document.getElementById('puzzleQuestion');
    const optionsContainer = document.getElementById('optionsContainer');
    const feedback = document.getElementById('feedback');

    questionEl.textContent = "Loading...";
    optionsContainer.innerHTML = '';
    feedback.style.display = 'none';

    try {
        const response = await fetch('/api/puzzle');
        const data = await response.json();
        currentPuzzle = data;

        questionEl.textContent = data.question;

        data.options.forEach(option => {
            const btn = document.createElement('button');
            btn.textContent = option;
            btn.className = 'btn btn-outline';
            btn.style.width = '100%';
            btn.onclick = () => checkAnswer(option);
            optionsContainer.appendChild(btn);
        });

    } catch (error) {
        console.error('Error:', error);
        questionEl.textContent = "Failed to load puzzle.";
    }
}

function checkAnswer(selected) {
    const feedback = document.getElementById('feedback');
    feedback.style.display = 'block';

    if (selected === currentPuzzle.answer) {
        feedback.style.background = 'rgba(0, 255, 0, 0.2)';
        feedback.style.border = '1px solid #00ff00';
        feedback.innerHTML = `<strong>Correct!</strong> <br> ${currentPuzzle.explanation}`;
    } else {
        feedback.style.background = 'rgba(255, 0, 0, 0.2)';
        feedback.style.border = '1px solid #ff0000';
        feedback.innerHTML = `<strong>Incorrect.</strong> Try again!`;
    }
}
