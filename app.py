from flask import Flask, request, send_from_directory
app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def client():
    return send_from_directory('client/public', 'index.html')

# Route to add static files (CSS and JS)
@app.route("/<path:path>")
def base(path):
    return send_from_directory('client/public', path)

@app.route('/message')
def generate_random():
    args = request.args
    print(args['name'])
    return "Hello " + args['name']

if __name__ == '__main__':
    app.run()