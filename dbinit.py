import sqlite3
# the reason i choice to use sqlite3 is because i have found easier to upload a lot of data at once also i have used more than sqlalchemy 
#connecting to database
conn = sqlite3.connect('Sales.db')
#creating a cursor 
c = conn.cursor()

many_product = [
    ('Hobgoblin', 'Cake',4,388,1),
  ('Green Goblin', 'Cake',4,312,1),
  ('Forest Sprite', 'Canned Drink',0.8,97,1),
  ('Redcap', 'Cake',3.5,605,1),
  ('Imp', 'Cake',2,162,1),

  ('Hobgoblin', 'Cake',4,482,2),
  ('Green Goblin', 'Cake',4,312,2),
  ('Forest Sprite', 'Canned Drink',0.8,123,2),
  ('Redcap', 'Cake',4,401,2),
  ('Imp', 'Cake',1.5,540,2),
  ('Filthy Hobbit', 'Cookie',1,325,2),

  ('Hobgoblin', 'Cake',4,389,3),
  ('Green Goblin', 'Cake',4,302,3),
  ('Forest Sprite', 'Canned Drink',0.8,168,3),
  ('Redcap', 'Cake',4,433,3),
  ('Imp', 'Cake',2,486,3),
  ('Filthy Hobbit', 'Cookie',1,164,3),
  ('Wretched Elf', 'Cookie',1,212,3),
  ('Foul Dwarf', 'Cookie',1,168,3),
  ('Vile Human', 'Cookie',1,92,3),

  ('Hobgoblin', 'Cake',4,369,4),
  ('Green Goblin', 'Cake',4,333,4),
  ('Forest Sprite', 'Canned Drink',0.8,168,4),
  ('Redcap', 'Cake',4,462,4),
  ('Imp', 'Cake',2,501,4),
  ('Filthy Hobbit', 'Cookie',1,125,4),
  ('Wretched Elf', 'Cookie',1,201,4),
  ('Foul Dwarf', 'Cookie',1,162,4),
  ('Vile Human', 'Cookie',1,143,4),
  ('Wizard Spit', 'Hot Drink',3.5,455,4),
  ('Brownie', 'Cake',1.5,666,4)
]
# creating table if there isn't name it as GoblinCakeSales
c.execute ("CREATE TABLE IF NOT EXISTS GoblinCakeSales (ID integer primary key autoincrement, Product nvarchar,Product_Type nvarchar,Price_Per int,Units_Sold int, Quarter int)")
#import all the data back to db 
c.executemany ("INSERT INTO   GoblinCakeSales (Product, Product_Type, Price_Per, Units_Sold, Quarter) VALUES (?,?,?,?,?)", many_product)
# finally copy all the data to the database
conn.commit()
# close the connection 
conn.close()