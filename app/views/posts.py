from flask import Blueprint, abort, request, Response
from sqlalchemy import exc
from ..models import db
from ..models.WEPPost import WEPPost


bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('<int:post_id>', methods=['GET'])
def read_specific_post(post_id: int) -> Response:
    post = WEPPost.query.get_or_404(post_id)
    return Response(post.text)
