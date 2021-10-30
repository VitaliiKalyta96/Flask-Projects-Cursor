from app import app
from flask import render_template, jsonify


@app.route('/todos')
def todos_list():
    return render_template('todo.html')

@app.route('/add-todo')
def add_todo():
    return render_template('add-todo.html')
    
    
# Чи варто зачіпати цю todo.py цей блок для вирішення 1 завдання з додаванням методу апдейт і деліт ??

# @app.route('/update-todo/<string:title>/<string:text>/', methods=['PUT'])
# def update_todo(title, text):
#     return jsonify({title=title, text=text})

# @app.route('/delete-todo/<string:title>/<string:text>/', methods=['DELETE'])
# def delete_todo(title, text):
#    todos.remove(title[0], text[1])
#    return None, 404