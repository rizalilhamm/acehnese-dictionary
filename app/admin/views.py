from flask import Blueprint

admin = Blueprint('admin_blueprint', __name__)

@admin.route('/admin/login')
def admin_login():
    return "Halaman login admin"


@admin.route('/admin/kosakata')
def kosakata():
    return "halaman list data, method POST, GET"


@admin.route('/admin/kosakata/<index_kosakata>')
def detail_kosakata():
    return "Halaman detail kosakata"