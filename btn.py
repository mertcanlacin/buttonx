from flask import Flask, render_template, request, redirect, url_for
from time import sleep
from threading import Thread
import serial
import time
from pyfirmata2 import Arduino


PIN = 13


board = Arduino('/dev/ttyACM0')



app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def hello_world():
    if request.method == 'POST':
        if request.form['submit'] == 'Turn on':
            print ('TURN ON')
        elif request.form['submit'] == 'Turn Off':
            print ('TURN OFF')
        else:
            pass

    return render_template('index.html')


@app.route('/turnon', methods=['GET','POST'] )
def turn_on():
    board.digital[PIN].write(1)
    return redirect( url_for('status') )


@app.route('/turnoff', methods=['GET','POST'] )
def turn_off():
    board.digital[PIN].write(0)
    return redirect( url_for('hello_world') )




if __name__ == '__main__':

    app.run(port=5000, host='localhost', debug = True)
