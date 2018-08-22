from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///murders.db'
db = SQLAlchemy(app)

#Pulls out the information from the database columns so we don't have to do it manually
class Murder(db.Model):
  __tablename__ = 'murders'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  uid = db.Column(db.String, primary_key=True)


@app.route("/")
def hello():
  murders = Murder.query.all()
  return render_template("list.html", murders=murders)

# @app.route("/murders/")
# def murders():
#   murders = School.query.all()
#   return render_template("list.html", murders=murders)

@app.route("/murders/<uid>/")
def murder(uid):
  murder = Murder.query.filter_by(uid=uid).first()
  return render_template("show.html", murder=murder)

# # @app.route("/search")
# # def search():
# #   name = request.args.get('query')
# #   murders = School.query.filter(School.school_name.contains(name)).all()
# #   return render_template("list.html", murders=murders)

# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)