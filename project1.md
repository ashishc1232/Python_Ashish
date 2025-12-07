# app.py - Puri application ek hi file mein!

from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime

# Flask app banao
app = Flask(__name__)

# ==================== DATABASE FUNCTIONS ====================

def get_db():
    """Database connection"""
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row  # Dict jaisa result milega
    return conn

def init_db():
    """Database table banao (agar nahi hai to)"""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# App start hote hi database banao
init_db()

# ==================== ROUTES (URLs) ====================

@app.route('/')
def home():
    """
    Home page - Sabse pehle yeh chalega
    URL: http://localhost:5000/
    """
    # Database se sare expenses nikalo
    conn = get_db()
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    
    # Category-wise total nikalo
    category_totals = conn.execute('''
        SELECT category, SUM(amount) as total 
        FROM expenses 
        GROUP BY category 
        ORDER BY total DESC
    ''').fetchall()
    
    # Is mahine ka total
    current_month = datetime.now().strftime("%Y-%m")
    monthly_total = conn.execute('''
        SELECT SUM(amount) as total 
        FROM expenses 
        WHERE date LIKE ?
    ''', (f"{current_month}%",)).fetchone()
    
    conn.close()
    
    # HTML page ko data bhejo
    return render_template('index.html', 
                         expenses=expenses,
                         category_totals=category_totals,
                         monthly_total=monthly_total['total'] if monthly_total['total'] else 0)

@app.route('/add', methods=['POST'])
def add_expense():
    """
    Expense add karo
    Form submit hone par yeh chalega
    """
    # Form se data lo
    amount = request.form.get('amount')
    category = request.form.get('category')
    description = request.form.get('description', '')
    
    # Validate karo
    if not amount or not category:
        return "Amount aur Category zaroori hai!", 400
    
    # Database mein dalo
    conn = get_db()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn.execute('''
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    ''', (float(amount), category, description, current_date))
    
    conn.commit()
    conn.close()
    
    # Wapas home page par jao
    return redirect(url_for('home'))

@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    """
    Expense delete karo
    URL: http://localhost:5000/delete/5
    """
    conn = get_db()
    conn.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home'))

@app.route('/api/expenses')
def api_expenses():
    """
    API - JSON format mein data
    URL: http://localhost:5000/api/expenses
    """
    conn = get_db()
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    conn.close()
    
    # Dict mein convert karo
    expenses_list = []
    for expense in expenses:
        expenses_list.append({
            'id': expense['id'],
            'amount': expense['amount'],
            'category': expense['category'],
            'description': expense['description'],
            'date': expense['date']
        })
    
    return jsonify(expenses_list)

# ==================== RUN APPLICATION ====================

if __name__ == '__main__':
    # Development mode mein chalo
    # debug=True = Code change hone par auto-reload
    app.run(debug=True, host='0.0.0.0', port=5000)
