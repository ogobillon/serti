from bottle import route, run, static_file, error, template
import mysql.connector




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1942",
  database="ogobillon$serti_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM servicios")

myresult = mycursor.fetchall()

mycursor.close()
mydb.close()

# mydb = mysql.connector.connect(
#   host="ogobillon.mysql.pythonanywhere-services.com",
#   user="ogobillon",
#   password="m7121941",
#   database="ogobillon$serti_db"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM servicios")
#
# myresult = mycursor.fetchall()
#
# mycursor.close()
# mydb.close()

#pythonanywhere.com
#root_ = '/home/ogobillon/mysite/'

#local
root_ = ''

root_html = root_ + 'static/html'
root_img = root_ + 'static/img'
root_css = root_ + 'static/css'
root_views = root_ + 'views'


@route(['/', '/index.html'])
def index():
    return static_file('index.html', root=root_html)


@route('/ventas.html')
def ventas():
    return static_file('ventas.html', root = root_html)

# @route('/servicios.html')
# def servicios():
#     return static_file('servicios.html', root = root_html)

@route('/img/<filepath:path>')
def imagenes(filepath):
    return static_file(filepath, root = root_img)

@route('/css/<filepath:path>')
def estilos(filepath):
    return static_file(filepath, root = root_css)

@error(404)
def error404(error):
    return 'Nothing here, jsorry'

datos = {'f':myresult}


@route('/servicios.html')
def hello(name='World'):
    return template(root_views + '/servicios.html', data=datos)


run(host='localhost', port=8080)