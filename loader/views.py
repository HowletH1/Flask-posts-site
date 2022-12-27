from flask import Blueprint, render_template, request
import logging
from loader.utils import save_pic
from main.utils import poster

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@loader_blueprint.route('/post')
def new_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def new_post():
    pic = request.files.get('picture')
    content = request.form.get('content')

    if not pic or not content:
        return 'Заполните форму!'

    pic_path = save_pic(pic)
    if not pic_path:
        logging.info('Загрузите изображение в формате png или jpg')
        return 'Загрузите изображение в формате png или jpg'

    pos_ter = poster('posts.json')
    new_post = {'pic': pic_path, 'content': content}
    pos_ter.add_post(new_post)

    return render_template('post_uploaded.html', pic_path=pic_path, content=content)
