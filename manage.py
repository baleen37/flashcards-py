import sys
from flashcards.application import create_app


def runserver():
    app = create_app('config.py')
    app.run('0.0.0.0', debug=True)


if __name__ == '__main__':
    if sys.argv[1] == 'runserver':
        runserver()
