import sqlite3

conn = sqlite3.connect('bd1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

try:
  cur.execute('''
  CREATE TABLE Counts (email TEXT, count INTEGER)''')
except:  
  print 'BD ja existe'
  quit ()

#----------------------------------------------------------------------------
#cur.execute ('INSERT INTO Counts (email, count) VALUES (?,?)',('XPTO',100))
#conn.commit ()

#cur.close ()
#quit ()
#-----------------------------------------------------------------------------

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
#-------------------------------------------------------------------------
    print email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES ( ?, 1 )''', ( email, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?',
            (email, ))
#-------------------------------------------------------------------------

#    try:
#      count = cur.fetchone()
#      cur.execute ('update Counts set count=count+1 where email = ?', (email, ))
#      print "estou no update"
#    except:
#      cur.execute('''INSERT INTO Counts (email, count) 
#                VALUES ( ?, 1 )''', ( email, ) )
#      print 'estou no insert'
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY email'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
