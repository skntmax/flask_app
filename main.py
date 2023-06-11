from flask import Flask,render_template, request
from  flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 
app = Flask(__name__)

databaseName ="todo"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sknt987'
app.config['MYSQL_DB'] = databaseName

mysql = MySQL(app)
print('mysql connected  to {todo} databse ')
 



@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/employee')
def init_employee():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  
    cursor.execute('''  create table employee (id int not Null  PRIMARY key AUTO_INCREMENT  ,  username  varchar(200) , password varchar(100) ) ; 
  ''')
    return ' empployee created'





# @app.route('/get-data' , methods=['GET', 'POST'])
# def send_employee():
    
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  
#     cursor.execute('''  create table employee (id int not Null  PRIMARY key AUTO_INCREMENT  ,  username  varchar(200) , password varchar(100) ) ; 
#   ''')
#     return ' empployee created'








@app.route('/get-blog')
def getBlog():
    try:   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('''  create table IF NOT EXISTS category(cat_id int not Null  PRIMARY key   ,  category_name  varchar(200) ) ; 
                        ''' )
         
        cursor.execute ('''  INSERT into category( `cat_id` , `category_name` ) values( 334 , 'men' ); 
                        ''' )
        
        cursor.execute ('''   INSERT into category( `cat_id` , `category_name` ) values( 23 , 'women' ) ;   
                        ''' )
                         
        cursor.execute ('''   INSERT into category( `cat_id` , `category_name` ) values( 34 , 'tshirts' )  ;  
                        ''' )
    

 
        return 'my blog'
    except Exception as err:
         return err





if __name__== "__main__":
    app.run(debug=True )