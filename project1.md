# app.py - Simple Flask Expense Tracker

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ========== DATABASE FUNCTIONS ==========

def get_db():
    """Database connection"""
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create table if not exists"""
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

# Initialize database on startup
init_db()

# ========== ROUTES ==========

@app.route('/')
def home():
    """Home page - show all expenses"""
    conn = get_db()
    
    # Get all expenses
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    
    # Get monthly total
    current_month = datetime.now().strftime("%Y-%m")
    result = conn.execute('''
        SELECT SUM(amount) as total 
        FROM expenses 
        WHERE date LIKE ?
    ''', (f"{current_month}%",)).fetchone()
    monthly_total = result['total'] if result['total'] else 0
    
    # Get category totals
    category_totals = conn.execute('''
        SELECT category, SUM(amount) as total 
        FROM expenses 
        GROUP BY category 
        ORDER BY total DESC
    ''').fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         expenses=expenses,
                         monthly_total=monthly_total,
                         category_totals=category_totals)

@app.route('/add', methods=['POST'])
def add_expense():
    """Add new expense"""
    amount = request.form.get('amount')
    category = request.form.get('category')
    description = request.form.get('description', '')
    
    if not amount or not category:
        return "Amount and Category required!", 400
    
    conn = get_db()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn.execute('''
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    ''', (float(amount), category, description, current_date))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    """Delete expense by ID"""
    conn = get_db()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home'))

# ========== RUN APP ==========

if __name__ == '__main__':
    app.run(debug=True)
