import time
import string
import operator
def gettime():
    setbedtime='23-00-00'
    HMS=time.strftime('%H-%M-%S',time.localtime(time.time()))
    print(setbedtime)
    print(HMS)
    isbedtime=operator.lt(setbedtime,HMS)
    print(isbedtime)
gettime()