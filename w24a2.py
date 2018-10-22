#------------------------------------------------------------------------------------------
#  week 2, assignment 2: count organizations using file mbox.txt as input
#------------------------------------------------------------------------------------------
import sqlite3
import urllib

conn = sqlite3.connect('bd1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
#if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open (fname)
for line in fh:
#    print "loop for", line.strip()
    if not line.startswith('From: ') : continue
    pieces = line.split()
    atpos = pieces [1].find ('@')
    org = pieces[1] [atpos+1:]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org, ))

# https://www.sqlite.org/lang_select.html
conn.commit ()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count desc limit 10'


print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
