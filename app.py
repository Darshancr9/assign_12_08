from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_name():
   return 'Hello this Darshan gowda'

@app.route('/assignment')
def return_name():
   return 'The assignment given on 09/08/2025 is completed'

if __name__ == '__main__':
   app.run(host="0.0.0.0",port="8080")
