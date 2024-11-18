from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        file = request.files['file']
        file.save(f'uploads/{file.filename}')
        return render_template('form.html', submitted_data={'name': name, 'age': age, 'file': file.filename})

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
