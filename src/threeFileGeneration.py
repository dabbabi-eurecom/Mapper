f=open('../data/positive_sample.csv','r')
fo=open('../data/positive_processed.csv','w')
line=f.readline()
while line:
    a=line.split(r'","')
    b=a[5][:-1]
    c=preprocessing.processTweet(b,stopWords,slangs)
    fo.write(c+'\n')
    line = f.readline()

f.close()
fo.close()

print "positive samples processed"

f=open('../data/negative_sample.csv','r')
fo=open('../data/negative_processed.csv','w')
line=f.readline()
while line:
    a=line.split(r'","')
    b=a[5][:-1]
    c=preprocessing.processTweet(b,stopWords,slangs)
    fo.write(c+'\n')
    line = f.readline()

f.close()
fo.close()

print "negative sample processed"

f=open('../data/neutral_sample.csv','r')
fo=open('../data/neutral_processed.csv','w')
line=f.readline()
while line:
    a=line.split(r'","')
    b=a[4][:-1]
    c=preprocessing.processTweet(b,stopWords,slangs)
    fo.write(c+'\n')
    line = f.readline()

f.close()
fo.close()

print "neutral sample processed"
