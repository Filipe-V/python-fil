import urllib

filename = raw_input ("Enter filename: ")

fh = open (filename)
line_counter = 0
for line in fh:
  try:
    line_counter = line_counter + 1
    print line.strip()
  except:
    print ("wrong page")
    quit ()
print ("Linhas lidas: "), line_counter
