from flask import Blueprint

admin = Blueprint('admin_blueprint', __name__)


@admin.route('/admin/login')
def admin_login():
    return "Halaman login admin"


@admin.route('/admin/kosakata')
def kosakata():
    """
    Function description:
        1. Admin will GET all Data from database]
    """
    pass

@admin.route('/admin/kosakata/<kosakata_id>')
def add_new_example(kosakata_id):
    """
    The Function used by admin to POST example of a specific data filtered by kosakata_id (Akan mengembalikan form)
    Params:
            kosakata_id(Int): ID of a word in Database
    """
    pass
