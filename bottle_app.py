from bottle import route, run, static_file, error, template, TEMPLATES, request, post, debug
import db
import corre


TEMPLATES.clear()

#pythonanywhere.com
root_ = '/home/ogobillon/mysite/'
consultas = db.db_get("ogobillon.mysql.pythonanywhere-services.com","ogobillon","m7121941","ogobillon$serti_db")


#local
# root_ = ''
# consultas = db.db_get("localhost","root","1942","ogobillon$serti_db")

root_html = root_ + 'static/html'
root_img = root_ + 'static/img'
root_css = root_ + 'static/css'
root_views = root_ + 'views'

datos = {'f':consultas}

@route(['/', '/index.html'])
def index():
    TEMPLATES.clear()
    return template(root_views + '/index.html')

@route('/ventas.html')
def ventas(name='World'):
    TEMPLATES.clear()
    return template(root_views + '/ventas.html')

@route('/contacto.html')
def ventas(name='World'):
    TEMPLATES.clear()
    return template(root_views + '/contacto.html')

@route('/servicios.html')
def servicios(name='World'):
    TEMPLATES.clear()
    return template(root_views + '/servicios.html', data=datos)

@route('/enviado.html')
def enviado(name='World'):
    TEMPLATES.clear()
    return template(root_views + '/enviado.html')

@route('/img/<filepath:path>')
def imagenes(filepath):
    return static_file(filepath, root = root_img)

@route('/css/<filepath:path>')
def estilos(filepath):
    return static_file(filepath, root = root_css, mimetype='text/css')

@error(404)
def error404(error):
    return template(root_views + '/error404.html')


@post('/c4g') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('user_name')
    u_email = request.forms.get('user_mail')
    mensaje = request.forms.get('user_message')
    corre.send_email(username, u_email, mensaje)

    return template(root_views + '/enviado.html')


# run(host='localhost', port=8080, reloader=True, debug=False)