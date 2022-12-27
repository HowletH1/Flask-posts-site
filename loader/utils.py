def save_pic(picture):
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ('jpg', 'PNG'):
        return

    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'
