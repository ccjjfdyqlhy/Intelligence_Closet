import time
import sys
print('欢迎使用智能衣柜管理系统\n此工具将配合你对软件系统进行设定\n请按照以下的说明来操作')
time.sleep(1)
o1=input('输入你所在的城市，以便获取天气（输入错误默认北京）>>>')
filename = 'setup'
with open(filename, 'w') as file_object:
    file_object.write(o1)
print('写入成功，即将启动软件.....')
import main
sys.exit()
