from flask_frozen import Freezer
from app import app, Murder

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def murder():
    for murder in Murder.query.all():
        yield { 'uid': murder.uid }

if __name__ == '__main__':
    freezer.freeze()