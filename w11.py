class AnimalDeFesta:
  x=0
  def festa (proprio):
    proprio.x = proprio.x + 1
    print "ate agora", proprio.x

animal = AnimalDeFesta ()
animal.festa ()
animal.festa ()
animal.festa ()

print "Type", type (animal)
print "Dir", dir (animal)
