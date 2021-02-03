import pathlib
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    file_ext = pathlib.Path(form_picture.filename).suffix
    image_filename = random_hex + file_ext
    picture_path = pathlib.Path(current_app.root_path).joinpath(
        "static", "profile_pics", image_filename
    )
    output_size = (128, 128)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return image_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email]
    )
    msg.body = f"""To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, then simply ignore this email and no changes will be made."""
    mail.send(msg)