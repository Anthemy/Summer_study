
#简单写入
#fp = open('test.txt','w')
#fp.write("nihao!\n"*10)
#fp.close()

#简单读入
#fp = open('test.txt','r')
#content = fp.read()
#print('%s' % (content))
#fp.close()


#保存对象
import json
class Test:
    a=12
    def __init__(self):
        self.a=0

fp = open("test.txt",'w')
obj = ["list"]
t = json.dumps(obj)
print(t)
fp.write(t)
fp.close()
