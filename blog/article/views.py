from flask import Blueprint

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def article_list():
    return 'Hello article'
