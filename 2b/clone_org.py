import  envoy, re, time


start = time .time()
now = start
nmax = DiskCapacity
nused = 0
f  =  open ('oneTrepoSize.csv')
for l in f: 
  ar = l .split(';')
  s = int (ar [0])   	 			# size
  n = ar[5]                                     # owner 
  p = re. sub('/', '_', n)                      # repo              
  vcs = ar [1]                                  # vcs
  if vcs == 'git':
     cmd = 'git clone --mirror https://bitbucket.org/' + n + ' ' + p
  if vcs == 'hg':
     cmd = 'hg clone -U https://bitbucket.org/' + n + ' ' + p
  if (nused + s > DiskCapacity):
     now0 = time .time()
     print str (nused) + ' cloned in ' + str (now0 - now) 
     now = time .time()
     envoy .run ('rsync -ae "ssh -p2200" * kagrawa1@da2.eecs.utk.edu:hg')
     envoy .run ('ls | while read dir; do [[ -d $dir ]] && find $dir -delete; done')
     now = time .time()
     print str (nused) + ' synced in ' + str (now - now0) 
     nused = 0
  nused += s
  envoy .run (cmd)
f .close()


# n  apdavison/nrnutils
# p  apdavison_nrnutils
# hg clone -U https://bitbucket.org/' + n + ' ' + p

