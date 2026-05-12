from flask import Flask, render_template, request, redirect
from models import db, Task


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

    
    
with app.app_context():
    db.create_all()
    
    

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks) 



@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('task')
    if title:
        new_task = Task(description=title)
        db.session.add(new_task)
        db.session.commit()
        
    return redirect('/')



@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    
    if task:
        db.session.delete(task)
        db.session.commit()
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
 