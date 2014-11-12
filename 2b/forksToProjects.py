import pymongo,re
client = pymongo.MongoClient (host="da0.eecs.utk.edu")
db = client ['bitbucket']
coll = db ['forks']
fws = {}
for r in coll .find ({}, { "url":1, "values" : 1, "_id":0 } ):  
  l, v = (r ["url"], r ["values"])
  l = re.sub ("https://bitbucket.org/api/2.0/repositories/", "", l)
  l = re.sub ("/forks", "", l)
  for n in v:
    f = n ["uuid"]
    if l in fws:
      fws [l] .add (f)
    else:
      fws [l] = { f }

fwsC = []
for f in fws:
   fwsC .append ((f, len (fws[f])))
srt = sorted (fwsC, key = lambda x: x[1], reverse=True)[0:10]
for f in srt:
  print f[0] + ' has ' + str (f[1]) + " forks" 
