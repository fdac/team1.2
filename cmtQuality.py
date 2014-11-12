import pymongo,operator
client = pymongo.MongoClient (host="da0.eecs.utk.edu")
db = client ['bitbucket']
coll = db ['deltas']
cmtAll = {}
cmtRepo = {}
cmtAuthor = {}
for r in coll .find ({}, {"commits.comment":1,"commits.author":1,"name":1} ):
  c, n = (r ["commits"], r ["name"]) # name: repo name?
  for cmt in c:
    if "comment" not in cmt:
      continue
    a = cmt ["author"]  #dictionary for authos
    cm = cmt ["comment"] # comments
    if cm not in cmtAll: # check the comment of commit
      cmtAll [cm] = 1   # if this commit is not in the dictionary, add it and set it's value to 1
    else:
      cmtAll [cm] += 1  #duplication of commits
    if n not in cmtRepo:
      cmtRepo [n] = { cm: 1 } # if the name of repo is not in the dictionary, create one - this commit 1
    else:
      if cm not in cmtRepo [n]: #if repo is exist but commit for this repo is not there, put it's value to 1
        cmtRepo [n][cm] = 1
      else:
        cmtRepo [n][cm] = cmtRepo [n][cm] + 1 # if both repo and commit are exist, increase the number of the same commit by 1
    if a not in cmtAuthor: # if author is not exist
      cmtAuthor [a] = { cm: 1 } #create a dictionary of author: commit
    else:
      if  cm not in cmtAuthor [a]: #if author exist but this commit is not in, add the commit in
        cmtAuthor [a][cm] = 1
      else:
        cmtAuthor [a][cm] = cmtAuthor [a][cm] + 1 # if author and commit exist, increase the number of the same commit by 1

for a in cmtAuthor .keys ():
  nCmt, lCmt = 0, 0
  for cm in cmtAuthor [a]:
    nCmt += cmtAuthor [a][cm]  #total number of commits per author
    lCmt += len (cm)  #size of all commits
  print 'a;' + a.encode('utf-8') + ';' + str(len(cmtAuthor [a])) + ';' + str(nCmt) + ';' + str(lCmt)
  #output: a; author; number of unique commits; number of commits; size of commits



for r in cmtRepo .keys ():
  nCmt, lCmt = 0, 0
  for cm in cmtRepo [r]:
    nCmt += cmtRepo [r][cm]
    lCmt += len (cm)
  print 'r;' + r + ';' + str(len(cmtRepo [r])) + ';' + str(nCmt) + ';' + str(lCmt)
  #output: r; repo; number of commits; size of commits
