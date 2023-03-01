from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'Статья 1',
        'text': 'Текст статьи 1',
        'author': {
            'name': 'Mark',
            'id': 1
        }
    },
    2: {
        'title': 'Статья 2',
        'text': 'Текст статьи 2',
        'author': {
            'name': 'Eugene',
            'id': 2
        }
    },
    3: {
        'title': 'Статья 3',
        'text': 'Текст статьи 3',
        'author': {
            'name': 'Karl',
            'id': 3
        }
    }
}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def content_article(pk: int):
    try:
        text_article = ARTICLES[pk]['text']
    except KeyError:
        raise NotFound(f'Article id = {pk} not found')
    return render_template('articles/content_article.html', text_content_article=[text_article, pk],
                           articles=ARTICLES[pk])
