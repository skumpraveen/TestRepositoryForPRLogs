class Calculator {
    constructor(previousOperandElement, currentOperandElement) {
        this.previousOperandElement = previousOperandElement;
        this.currentOperandElement = currentOperandElement;
        this.history = [];
        this.clear();
    }

    clear() {
        this.currentOperand = '0';
        this.previousOperand = '';
        this.operation = undefined;
        this.updateDisplay();
    }

    delete() {
        if (this.currentOperand === '0') return;
        if (this.currentOperand.length === 1) {
            this.currentOperand = '0';
        } else {
            this.currentOperand = this.currentOperand.slice(0, -1);
        }
        this.updateDisplay();
    }

    appendNumber(number) {
        if (number === '.' && this.currentOperand.includes('.')) return;
        if (this.currentOperand === '0' && number !== '.') {
            this.currentOperand = number;
        } else {
            this.currentOperand = this.currentOperand + number;
        }
        this.updateDisplay();
    }

    chooseOperation(operation) {
        if (this.currentOperand === '') return;
        if (this.previousOperand !== '') {
            this.compute();
        }
        this.operation = operation;
        this.previousOperand = this.currentOperand;
        this.currentOperand = '0';
        this.updateDisplay();
    }

    compute() {
        let computation;
        const prev = parseFloat(this.previousOperand);
        const current = parseFloat(this.currentOperand);
        if (isNaN(prev) || isNaN(current)) return;

        // Map operation symbols for display in history
        const operationSymbols = {
            '+': '+',
            '-': '-',
            '*': '×',
            '/': '÷'
        };
        const operationSymbol = operationSymbols[this.operation] || this.operation;

        switch (this.operation) {
            case '+':
                computation = prev + current;
                break;
            case '-':
                computation = prev - current;
                break;
            case '*':
                computation = prev * current;
                break;
            case '/':
                if (current === 0) {
                    this.history.push(`${prev} ${operationSymbol} ${current} = Error: Division by zero`);
                    updateHistoryDisplay();
                    this.currentOperand = 'Error';
                    this.operation = undefined;
                    this.previousOperand = '';
                    this.updateDisplay();
                    setTimeout(() => this.clear(), 1500);
                    return;
                }
                computation = prev / current;
                break;
            default:
                return;
        }

        // Add to history
        this.history.push(`${prev} ${operationSymbol} ${current} = ${computation}`);
        updateHistoryDisplay();
        
        this.currentOperand = computation.toString();
        this.operation = undefined;
        this.previousOperand = '';
        this.updateDisplay();
    }

    getDisplayNumber(number) {
        const stringNumber = number.toString();
        const integerDigits = parseFloat(stringNumber.split('.')[0]);
        const decimalDigits = stringNumber.split('.')[1];
        let integerDisplay;

        if (isNaN(integerDigits)) {
            integerDisplay = '';
        } else {
            integerDisplay = integerDigits.toLocaleString('en', {
                maximumFractionDigits: 0
            });
        }

        if (decimalDigits !== undefined) {
            return `${integerDisplay}.${decimalDigits}`;
        } else {
            return integerDisplay;
        }
    }

    updateDisplay() {
        this.currentOperandElement.textContent = this.getDisplayNumber(this.currentOperand);
        if (this.operation !== undefined) {
            this.previousOperandElement.textContent = 
                `${this.getDisplayNumber(this.previousOperand)} ${this.operation}`;
        } else {
            this.previousOperandElement.textContent = '';
        }
    }
    
    getHistory() {
        return this.history.slice();
    }
    
    clearHistory() {
        this.history = [];
        updateHistoryDisplay();
    }
}

// Initialize calculator
const previousOperandElement = document.getElementById('previous-operand');
const currentOperandElement = document.getElementById('current-operand');
const calculator = new Calculator(previousOperandElement, currentOperandElement);

// History display functions
function updateHistoryDisplay() {
    const historyList = document.getElementById('history-list');
    const history = calculator.getHistory();
    
    if (history.length === 0) {
        historyList.innerHTML = '<div class="history-empty">No calculations yet</div>';
    } else {
        historyList.innerHTML = history.map((entry, index) => 
            `<div class="history-item">${index + 1}. ${entry}</div>`
        ).join('');
    }
}

function toggleHistory() {
    const historyPanel = document.getElementById('history-panel');
    const historyBtn = document.getElementById('history-btn');
    
    historyPanel.classList.toggle('visible');
    
    if (historyPanel.classList.contains('visible')) {
        historyBtn.textContent = '📊 Hide History';
        updateHistoryDisplay();
    } else {
        historyBtn.textContent = '📊 Show History';
    }
}

function clearCalculatorHistory() {
    calculator.clearHistory();
}

// Orientation toggle function
function toggleOrientation() {
    const calculatorElement = document.getElementById('calculator');
    const orientationBtn = document.getElementById('orientation-btn');
    
    calculatorElement.classList.toggle('landscape');
    
    if (calculatorElement.classList.contains('landscape')) {
        orientationBtn.textContent = '🔄 Switch to Portrait';
    } else {
        orientationBtn.textContent = '🔄 Switch to Landscape';
    }
}
