"python.linting.pylintPath": "/path/to/your/virtualenv/bin/pylint"
import os
from flask import Flask,render_template,request
import process

app = Flask(__name__)

app.vars={}

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('about.html')
    else:
        app.vars['ticker'] = request.form['ticker']
        app.vars['column'] = request.form['column']

        process.plot_data(app.vars['ticker'],app.vars['column'])
        ticker = app.vars['ticker']
        column = app.vars['column']

        return render_template('about.html', name = ticker+'_'+ column, name_ticker = ticker, \
            name_column = column, url ='./static/'+ticker+'_'+column+'.png')

for file in os.scandir('./static'):
    if file.name.endswith(".png"):
        os.unlink(file.path)

if __name__ == "__main__":
    app.run(debug=True)
