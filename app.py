from flask import Flask, render_template, request, redirect
# making a database:
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno =db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(200), nullable=False)
    desc =db.Column(db.String(500), primary_key=False)
    date_created =db.Column(db.DateTime, default= datetime.utcnow)

    # making th object  like what you want to see when you run the program
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"



@app.route('/index4', methods=['GET', 'POST'])
def hello_world():
    
    if request.method=='POST':
        ti = request.form['title']
        de = request.form['desc']
    
    # making instance of todop
        todo = Todo(title= ti , desc=de)
        db.session.add(todo)
        db.session.commit()
    
    allTodo=Todo.query.all()
    # return 'Hello, World!'
    return render_template('index4.html',allTodo=allTodo)
# allTodo ke naam se hi allTodo variable ko pass kia hain


@app.route('/login')
def products():
    
    
    return render_template('login.html')


@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        tit = request.form['title']
        desc= request.form['desc']
        
        todo=Todo.query.filter_by(sno=sno).first()
        
        todo.title = tit 
        # now your new titile(tit)in the from will be what you have updated which will be added by the command db.session.add()
        todo.desc = desc
        
        db.session.add(todo)
        db.session.commit()
        return redirect('/index4')
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    # read documentation: accessing the data in database- User.query.all() - it will be showed on the show rout of the web page- displaing all the tood in terminal
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/index4')

if __name__== "__main__":
    app.run(debug=True, port=8000)
    
