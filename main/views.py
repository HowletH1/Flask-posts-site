from flask import Blueprint, render_template, request
from main.utils import poster
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def s_page():
    sub = request.args.get('s')
    logging.info(f'Поиск: {sub}')
    pos_ter = poster('posts.json')
    posts, error = pos_ter.search_posts(sub)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка'
    return render_template('post_list.html', posts=posts, sub=sub)
