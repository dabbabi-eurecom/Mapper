# python script for determining the polarity and POS caracteristics
# of an input tweet using SentiWordNet3.0 dictionnary

# load input file in a dictionnary
def loadSentiSimple(filename):
    output={}
    print "Opening SentiWordnet file..."
    fi=open(filename,"r")
    line=fi.readline() # skip the first header line
    line=fi.readline()
    print "Loading..."

    while line:
        l=line.split('\t')
        tag=l[0]
        word=l[1]
        pos=abs(float(l[3]))
        neg=abs(float(l[4]))
        neu=abs(float(l[5]))

        output[word]=[tag,pos,neg,neu]
        line=fi.readline()
    fi.close()
    return output

def loadSentiFull(filename):
    output={}
    print "Opening SentiWordnet file..."
    fi=open(filename,"r")
    line=fi.readline() # skip the first header line
    line=fi.readline()
    print "Loading..."

    while line:
#        print line
        l=line.split('\t')
        try:
            tag=l[0]
            sentence=l[4]
            new = [word for word in sentence.split() if (word[-2] == "#" and word[-1].isdigit())]
            pos=abs(float(l[2]))
            neg=abs(float(l[3]))
            neu=float(1-pos-neg)
        except:
#            print line
            line=fi.readline()
            continue

        for w in new:
            output[w[:-2]]=[tag,pos,neg,neu]
        line=fi.readline()
    fi.close()
    return output

def polarity(tweet,sentDict): # polarity aggregate of a tweet from sentiWordnet dict
    pos=0.0
    neg=0.0
    neu=0.0
    for w in tweet.split():
        if w in sentDict.keys():
#            print sentDict[w]
            pos=pos+sentDict[w][1]
            neg=neg+sentDict[w][2]
            neu=neu+sentDict[w][3]
    return [pos,neg,neu]

def getPos(dict):
    result=[]
    for w in dict.keys():
        if dict[w][0] not in result:
            result.append(dict[w][0])
    return result
# 4 POS : v,n,a,r verb, noun, adj, adverb in SentiWordNet

def posFreq(tweet,dict): # calculates the frequency of apperances of pos in a tweet
    result={}
    result['v']=0
    result['n']=0
    result['a']=0
    result['r']=0

    for w in tweet.split():
        if (w in dict.keys()):
            result[dict[w][0]]=result[dict[w][0]]+1
    return result

#INPUT_FILENAME="../resources/sentiWordnetBig.csv"
#dict=loadSentiFull(INPUT_FILENAME)
#print len(dict.keys())
#print dict.keys()
# still some work to finish and to add some synonyms
# POS tags in a function

#t="I think I love you"
#print polarity(t,dict)
#print t
#print posFreq(t,dict)

