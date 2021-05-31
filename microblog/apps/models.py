from apps.app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    """
    Класс User имеет новое поле сообщений, которое инициализируется db.relationship. 
    Это не фактическое поле базы данных, а высокоуровневое представление о взаимоотношениях между users и posts, 
    и по этой причине оно не находится в диаграмме базы данных. Для отношения «один ко многим» поле db.relationship обычно 
    определяется на стороне «один» и используется как удобный способ получить доступ к «многим». Так, например, если 
    у меня есть пользователь, хранящийся в u, выражение u.posts будет запускать запрос базы данных, который возвращает все записи, 
    написанные этим пользователем. Первый аргумент db.relationship указывает класс, который представляет сторону отношения «много». 
    Аргумент backref определяет имя поля, которое будет добавлено к объектам класса «много», который указывает на объект «один». Это добавит 
    выражение post.author, которое вернет автора сообщения. Аргумент lazy определяет, как будет выполняться запрос базы данных для связи, 
    о чем я расскажу позже. Не беспокойтесь, если эти детали не имеют для вас смысла, я покажу примеры в конце этой статьи.
    """
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.text)

