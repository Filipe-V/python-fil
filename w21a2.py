import sqlite3
import urllib

conn = sqlite3.connect('bd1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# sql debug
cur.execute ('insert into Counts (email, count) values (?, ?)', ('START', 1))
conn.commit ()
#sql debug end

fname = raw_input('Enter file name: ')
#if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = urllib.urlopen (fname)
print "filename: ", fname
#fh = open(fname)
for line in fh:
#    print "loop for", line.strip()
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    print email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES ( ?, 1 )''', ( email, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?',
            (email, ))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY email'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
