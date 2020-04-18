import json
def jsCreate(dictObj,filename):
    with open(filename,'w+') as of:
        with open('top.js') as f1:
            for line in f1:
                of.write(line)
    File=open(filename,"a+")
    File.write(json.dumps(dictObj,indent=2))
    with open(filename,'a+') as of:
        with open('bottom.js','r') as f1:
            for line in f1:
                of.write(line)
