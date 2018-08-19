from flask_frozen import Freezer
from app import app, School

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def school():
    for school in School.query.all():
        yield { 'dbn': school.dbn }

if __name__ == '__main__':
    freezer.freeze()