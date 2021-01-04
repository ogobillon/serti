from bottle import route, run, static_file, error, template, TEMPLATES
import db


#pythonanywhere.com
root_ = '/home/ogobillon/mysite/'
consultas = db.db_get("ogobillon.mysql.pythonanywhere-services.com","ogobillon","m7121941","ogobillon$serti_db")


#local
#root_ = ''
#consultas = db.db_get("localhost","root","1942","ogobillon$serti_db")

root_html = root_ + 'static/html'
root_img = root_ + 'static/img'
root_css = root_ + 'static/css'
root_views = root_ + 'views'

datos = {'f':consultas}

@route(['/', '/index.html'])
def index():
    return static_file('index.html', root=root_html)


@route('/ventas.html')
def ventas():
    return static_file('ventas.html', root = root_html)

@route('/img/<filepath:path>')
def imagenes(filepath):
    return static_file(filepath, root = root_img)

@route('/css/<filepath:path>')
def estilos(filepath):
    return static_file(filepath, root = root_css)

@error(404)
def error404(error):
    return 'Nothing here, jsorry'

@route('/servicios.html')
def hello(name='World'):
    TEMPLATES.clear()
    return template(root_views + '/servicios.html', data=datos)


#run(host='localhost', port=8080)