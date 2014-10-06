import re

# Extract team 1.2 repos from divided
mainfile = open('divided', 'r')
repofile = open('repoTone', 'w')

team = 1

delimiter = ';'
for line in mainfile:
    split = line.split(delimiter)
    t_file = int(split[0])
#    print t_file
    if team == t_file:
       repofile.write(line)

repofile.close()
mainfile.close()

# match these repos with more detailed file Reposize.csv and get team 1 info.
# we can do this in above step but this would be more efficient
repofile = open('repoTone', 'r')

repos_t1 = {}
# create a dict
for line in repofile:
    split = line.split(delimiter)
    repo = split[2]
    repos_t1[repo] = True

repofile.close()

mainfile2 = open('RepoSize.csv','r')
oneTfile  = open('oneTrepoSize.csv','w')

for line in mainfile2:
    split = line.split(delimiter)
    repo_main = split[5]
    if repo_main in repos_t1:
       oneTfile.write(line)


oneTfile.close()
mainfile2.close()


  





