from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from calculator import ScientificCalculator
from database import CalculationDatabase
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "REPLACE_THIS_WITH_A_RANDOM_SECRET_KEY"
db = CalculationDatabase()
calc = ScientificCalculator()

# User Authentication
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        if db.user_exists(username):
            return render_template('register.html', error="Username already exists.")
        db.create_user(username, password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        user = db.get_user(username)
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Main Calculator Page
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'])

@app.route('/calculate', methods=['POST'])
def calculate():
    if 'username' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    data = request.get_json()
    expr = data.get('expression', '')
    try:
        result = calc.safe_eval(expr)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/save', methods=['POST'])
def save():
    if 'username' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    data = request.get_json()
    expression = data.get('expression', '')
    result = data.get('result', '')
    if not expression or not result:
        return jsonify({'error': 'Invalid data'}), 400
    db.save_calculation(session['username'], expression, result)
    return jsonify({'status': 'success'})

@app.route('/history')
def history():
    if 'username' not in session:
        return redirect(url_for('login'))
    records = db.fetch_calculations(session['username'], limit=50)
    return render_template('history.html', history=records, username=session['username'])

@app.route('/api/history')
def api_history():
    if 'username' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    records = db.fetch_calculations(session['username'], limit=50)
    return jsonify([
        {'expression': r[2], 'result': r[3], 'timestamp': r[4][:19]}
        for r in records
    ])

if __name__ == '__main__':
    app.run(debug=True)