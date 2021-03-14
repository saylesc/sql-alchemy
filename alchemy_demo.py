from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instance of the database
db = SQLAlchemy(app)

# Define some models
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person id: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return "Hey there " + person.name

if __name__ == '__main__':
    app.run()