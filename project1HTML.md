<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker</title>
    <style>
        /* Minimal CSS - bas readable ho */
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 50px auto;
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        input, select {
            padding: 8px;
            margin: 5px 0;
            width: 200px;
        }
        button {
            padding: 10px 20px;
            margin: 10px 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Expense Tracker</h1>
    
    <!-- Monthly Total -->
    <h3>This Month Total: ₹{{ "%.2f"|format(monthly_total) }}</h3>
    
    <hr>
    
    <!-- Add Expense Form -->
    <h2>Add New Expense</h2>
    <form action="/add" method="POST">
        <div>
            <label>Amount:</label>
            <input type="number" name="amount" step="0.01" required>
        </div>
        
        <div>
            <label>Category:</label>
            <select name="category" required>
                <option value="">Select</option>
                <option value="Food">Food</option>
                <option value="Transport">Transport</option>
                <option value="Shopping">Shopping</option>
                <option value="Bills">Bills</option>
                <option value="Entertainment">Entertainment</option>
                <option value="Health">Health</option>
                <option value="Education">Education</option>
                <option value="Other">Other</option>
            </select>
        </div>
        
        <div>
            <label>Description:</label>
            <input type="text" name="description">
        </div>
        
        <button type="submit">Add Expense</button>
    </form>
    
    <hr>
    
    <!-- Category Totals -->
    {% if category_totals %}
    <h2>Category-wise Total</h2>
    <ul>
        {% for cat in category_totals %}
        <li><strong>{{ cat.category }}:</strong> ₹{{ "%.2f"|format(cat.total) }}</li>
        {% endfor %}
    </ul>
    <hr>
    {% endif %}
    
    <!-- Expenses List -->
    <h2>All Expenses</h2>
    
    {% if expenses %}
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Category</th>
                <th>Amount</th>
                <th>Description</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            {% for expense in expenses %}
            <tr>
                <td>{{ expense.date }}</td>
                <td>{{ expense.category }}</td>
                <td>₹{{ "%.2f"|format(expense.amount) }}</td>
                <td>{{ expense.description or '-' }}</td>
                <td>
                    <a href="/delete/{{ expense.id }}" 
                       onclick="return confirm('Delete this expense?')">
                        <button>Delete</button>
                    </a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% else %}
    <p>No expenses yet. Add one above!</p>
    {% endif %}
    
</body>
</html>
