from flask import Flask, render_template, request, redirect, url_for
import psycopg2

conn = psycopg2.connect("postgres://schvhdcq:Y-XSNQytxv0xcsoHD7xbab3S_vIsvoKX@john.db.elephantsql.com/schvhdcq")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    # Get the input username from the form
    username = request.form.get('username')

    # Connect to the database and execute the query using parameterized queries
    cursor = conn.cursor()
    cursor.execute(f"SELECT password FROM users WHERE password = '{username}';")
    result = cursor.fetchone()
    print(result)
    # Check if the password matches and return the appropriate response
    if result:
        return redirect(url_for('correct'))
    else:
        return redirect(url_for('verify'))

@app.route('/correct')
def correct():
    return "raft_rum{d0ct0r'$ 0rc|3r5}"

if __name__ == '__main__':
    app.run(debug=True)