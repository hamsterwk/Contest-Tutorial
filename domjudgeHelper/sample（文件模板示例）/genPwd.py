import re
import random
temp='''
<div class="card %s">
    <div class="participantName">%s</div>

    <p>
        账号:
        <code>%s</code>
        密码:
        <code>%s</code>
    </p>

    <p>
        比赛网址:
        <code>http://175.27.241.127:12345/</code>
        座位号：
        <code>%s</code>
    </p>
</div>
'''

header='''
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>
    .card {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 28px;
        width: 800px;
        /*background-color: rgb(230, 230, 230);*/
        border: 1px solid gray;
        border-radius: 5px;
        padding: 20px;
        margin: 20px;
    }

    .participantName {
        font-size: 30px;
        font-weight: bold;
		color:black;
    }

    code {
        font-family: "Calibri";
        color: dimgray;
        padding: 0 20px 0 0;
    }

    p {
        margin: 10px 10px 10px 0;
    }

        .break {page-break-after: always;}

    .siteLink {
        font-weight: bold;
        /*background-color: rgb(91, 192, 222);*/
        color: gray;
    }
</style>

</head><body>
'''

tail='''
</div>
</body></html>
'''


def rearrange(stuList):
	while(len(stuList)%6!=0):
		stuList.append("1\t1\t1\t1\t1\t1\t")
	newList=[]
	step = (len(stuList)+5)//6
	for i in range(step):
		for j in range(i,len(stuList),step):
			newList.append(stuList[j])
	return newList

if __name__=='__main__':
	stuList = open('./seatList.tsv','r',encoding='utf8').read().split('\n')
	res=header
	stuList = rearrange(stuList)
	#f1 = open("./seatList.txt","w",encoding="utf8")
	num=0
	for stu in stuList:
		tmp=stu.split('\t')
		try:
			name=tmp[0]
			account=tmp[1]
			pwd = tmp[2]
			id=tmp[3]
		except:
			continue
		if(num==5):
			res+=temp%('break',name,account,pwd,id)
		else:
			res+=temp%('',name,account,pwd,id)
		num=(num+1)%6
		#f1.write("%s\t%s\t%s\t%d\n"%(name,account,pwd,id))
	res+=tail
	#f1.close()
	open('密码条.html','w',encoding='utf8').write(res)