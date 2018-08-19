from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ods.db'
db = SQLAlchemy(app)

#This code pulls out the information from the database so we don't have to do it manually
class Od(db.Model):
  __tablename__ = 'ods'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)


@app.route("/")
def hello():
  ods = Od.query.all()
  return render_template("list.html", ods=ods)
  # return 'hello world'


# @app.route("/ods/<dbn>/")
# def school(dbn):
#   school = School.query.filter_by(dbn=dbn).first()
#   return render_template("show.html", school=school)

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   ods = School.query.filter(School.school_name.contains(name)).all()
#   return render_template("list.html", ods=ods)

# If this is running from the command line
# do something

if __name__ == '__main__':
  app.run(debug=True)