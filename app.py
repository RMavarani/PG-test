from flask import Flask, render_template
import sqlalchemy as db
# Due to limited time, I had, I tried to use tool I was confided on. For the front end 
# I have got some codes from bootstrap and w3school to speed it up and then updated them after I was finished with the project.
#  The server filter the data and create web page and sends to the front end once it done. On frontend I have added feature which can filter out product on the screen. 
# This could have been done directly on the backend which I have left few hints how I would have done it but because there were few issues,
#  I used the JavaScript to change the method. 
 #I used the sqllite3 library to upload the data into the database and sqlalchemy library to access the db and filter db.  


app = Flask(__name__)
engine = db.create_engine('sqlite:///Sales.db')


# create the route for our website 
@app.route('/')
def base():
  
    return render_template("base.html")
@app.route('/sales/<quarter>')#+<FilterOut>

def sales(quarter ): #+ add filterOut as variable
#  in this method we get access to database and select data from GoblinCakeSales which we filter based on the quarter
    with engine.connect() as con:
       # we can interduce value which need to check product type to remove from list but i used the javascript do the job at frondend 
        #filtering=''
       # if(filterOut != 0):
        # filtering= " AND  NOT Product_Type = '" + filterOut +"'" 
        result = con.execute('SELECT * FROM GoblinCakeSales where GoblinCakeSales.Quarter = '+ quarter)#,+filterOut
        return render_template("table.html", rs=result)


if __name__ == '__main__':
    app.run(debug=True)