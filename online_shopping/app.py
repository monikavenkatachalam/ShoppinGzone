from flask import Flask, render_template,request,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jeans')
def jeanst():
    return render_template('jeans.html')

@app.route('/kurti')
def kurti():
    return render_template('kurti.html')

@app.route('/salwar')
def salwar ():
    return render_template('salwar.html')            

@app.route('/shirts')
def shirts ():
    return render_template('shirts.html')

@app.route('/shoes')
def shoes ():
    return render_template('shoes.html')


@app.route('/contact')
def contact ():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)