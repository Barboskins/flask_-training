from apps.app import app,db
from apps.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

"""
Декоратор app.shell_context_processor регистрирует функцию как функцию контекста оболочки. 
Когда запускается команда flask shell, она будет вызывать эту функцию и регистрировать элементы, возвращаемые 
ею в сеансе оболочки. Причина, по которой функция возвращает словарь, а не список, заключается в том, что для каждого 
элемента вы также должны указывать имя, под которым оно будет ссылаться в оболочке, которое задается индексами словаря.

После того, как вы добавите функцию обработчика flask shell, 
вы можете работать с объектами базы данных, не импортируя их
"""