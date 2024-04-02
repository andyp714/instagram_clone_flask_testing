from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

    @app.route('/nested')
    def nested():
        result = ''
        for i in range(5):
            for j in range(3):
                result += f'({i}, {j}) '
        return result

if __name__ == '__main__':
    app.run(debug=True)