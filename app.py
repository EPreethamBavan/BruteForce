from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

correct_codes = {
    "level1": "a31",
    "level2": ["y7i", "ce2"]
}

@app.route('/')
def choose_level():
    return render_template('choose_level.html')

@app.route('/level1_submit', methods=['POST'])
def level1_submit():
    submitted_code = request.form['code']
    if submitted_code == correct_codes['level1']:
        return redirect(url_for('level2'))
    return render_template('level1.html', wrong=True)

@app.route('/level2_submit', methods=['POST'])
def level2_submit():
    submitted_code1 = request.form['code1']
    submitted_code2 = request.form['code2']
    
    correct_code1 = correct_codes['level2'][0]
    correct_code2 = correct_codes['level2'][1]

    if submitted_code1 == correct_code1 and submitted_code2 == correct_code2:
        return "Congratulations! You've completed Level 2."
    elif submitted_code1 != correct_code1 and submitted_code2 != correct_code2:
        return render_template('level2.html', both_wrong=True)
    elif submitted_code1 != correct_code1:
        return render_template('level2.html', code1_wrong=True)
    elif submitted_code2 != correct_code2:
        return render_template('level2.html', code2_wrong=True)

@app.route('/level1')
def level1():
    return render_template('level1.html', wrong=False)

@app.route('/level2')
def level2():
    return render_template('level2.html', both_wrong=False, code1_wrong=False, code2_wrong=False)

if __name__ == '__main__':
    app.run(debug=True)
