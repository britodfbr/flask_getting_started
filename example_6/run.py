# coding: utf8

from app import app


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'),
            port=app.config.get('PORT'))
