from bottle import Bottle, request, template

app = Bottle()

# Define routes
@app.route('/')
def index():
    return template('index')

@app.route('/submit', method='POST')
def submit():
    # Get data from the form
    data = request.forms.get('data')

    # TODO: Write code to interact with Google Spreadsheet

    return "Data submitted successfully!"

if __name__ == '__main__':
    # Run the Bottle app
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
