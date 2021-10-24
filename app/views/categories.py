from flask import Blueprint, abort, request, jsonify, Response
from ..models import db
from ..models.WEPCategory import WEPCategory


bp = Blueprint('categories', __name__, url_prefix='/categories')


@bp.route('/<int:cat_id>/json', methods=['GET'])
def read_specific_category(cat_id: int) -> Response:
    category = WEPCategory.query.get_or_404(cat_id)
    return jsonify(category.json_serialize())
