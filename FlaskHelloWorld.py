
from flask import Flask, render_template  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    #print(app.url_map)
    #print('line 17')            # Print statements go to your console
    
    return render_template("index.html")
    

if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp