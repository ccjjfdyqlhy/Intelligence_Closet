print('[警告]服务已启动!')
try:
    import tkinter
    import requests
    import time
    import linecache
    import sys
    import os
    from tkinter import ttk
    from tkinter import *
    from tkinter.messagebox import *
except ModuleNotFoundError:
    print('[错误]无法启动服务，因为程序文件不完整。重新安装应用支持库来解决。')
    quit()
print('[信息]正在读取配置文件...')
try:
    path=sys.path[4]
    verify=linecache.getline('\ICconfig\setup', 1)
    first=linecache.getline('\ICconfig\setup', 2)
    target=linecache.getline('\ICconfig\setup',3)
except FileNotFoundError:
    print('[错误]没有侦测到配置文件')
    print('[信息]新窗口已创建')
    root=tkinter.Tk()
    root.title('初始化应用程序')
    root.geometry('500x500')
    label=tkinter.Label(root,text='软件初始化应用程序v1.0 ©Darkstar Software 2021')
    label.pack()
    showerror(title='程序错误',message='程序初始化失败，请尝试重新运行setup.py解决！')
    root.mainloop()
    print('[警告]程序已退出')
    quit()
print('[信息]正在验证程序包...')
if verify == '[ICsetupfile]':
    pass
else:
    print('[警告]配置文件没有被授权，请检查setup.py来源是否可靠')
    input('[等待]若要忽略请回车->')
print('[信息]正在检查运行次数')
if first == '1':
    firstrun=1
    with open(path+'\ICconfig\setup')as fp:
        s = fp.read()#将指定文件读入内存
        fp.close()#关闭该文件
    a = s.split('\n')
    a.insert(1, '0')#在第 LINE+1 行插入
    s = '\n'.join(a)#用'\n'连接各个元素
    with open(path+'\ICconfig\setup', 'w')as fob:
        fp.write(s)
        fob.close()
else:
    firstrun=0
print('[信息]运行前检查已完成，正在启动天气模块')
print('[信息]天气模块已启动，正在获取...')
rep = requests.get('http://www.tianqiapi.com/api?version=v6&appid=99245552&appsecret=RL8NtmPx&city='+target)
rep.encoding = 'utf-8'
city=rep.json()['city']
wea=rep.json()['wea']
temp=rep.json()['tem']+'°C'
wspeed=rep.json()['win_speed']
hum=rep.json()['humidity']
airlevel=rep.json()['air_level']
print('[信息]获取成功')
root=tkinter.Tk()
print('[信息]主窗口已创建')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d" %(w,h))
root.title('[已锁定]智能衣物管理系统')
root.attributes("-fullscreen", 'true')
print('[信息]正在加载启动窗口模块')
w1=tkinter.Label(root,text=city,font='微软雅黑 -30')
w2=tkinter.Label(root,text='天气:'+wea,font='微软雅黑 -20')
w3=tkinter.Label(root,text='温度:'+temp,font='微软雅黑 -20')
w4=tkinter.Label(root,text='湿度:'+hum,font='微软雅黑 -20')
w5=tkinter.Label(root,text='风速:'+wspeed,font='微软雅黑 -20')
w6=tkinter.Label(root,text='空气质量:'+airlevel,font='微软雅黑 -20')
b1=tkinter.Label(root,text=' ',font='微软雅黑 -120')
b2=tkinter.Label(root,text=' ',font='微软雅黑 -20')
print('[信息]正在获取时间信息')
t1=tkinter.Label(compound='center',text=time.strftime('%H:%M',time.localtime(time.time())),font='华文彩云 -120')
def trickit():
    currentTime=time.strftime('%H:%M',time.localtime(time.time()))
    t1.config(text=currentTime)
    root.update()
    t1.after(1000, trickit)
t1.after(1000, trickit)
def unlock():
    def restart_program():
        os.execv(__file__, sys.argv)
    root.destroy()
    main=tkinter.Tk()
    print('[信息]新窗口已创建')
    main.title('智能衣物管理系统')
    main.geometry("%dx%d" %(w,h))
    main.attributes("-fullscreen", 'true')
    t2=tkinter.Label(main,compound='center',text=time.strftime('%H:%M',time.localtime(time.time())),font='微软雅黑 -30')
    def trickit():
        currentTime=time.strftime('%H:%M',time.localtime(time.time()))
        t2.config(text=currentTime)
        main.update()
        t2.after(1000, trickit)
    t2.after(1000, trickit)
    t2.grid(row=0,column=0)
    l1=tkinter.Label(main,text='                                                   ',font='微软雅黑 -30')
    l1.grid(row=0,column=1)
    l2=tkinter.Label(main,text='智能衣物管理系统',font='微软雅黑 -30')
    l2.grid(row=0,column=2)
    l3=tkinter.Label(main,text='                                               ',font='微软雅黑 -30')
    l3.grid(row=0,column=3)
    bt2=tkinter.Button(main,text='锁定系统',font='微软雅黑 -30',command=restart_program)
    bt2.grid(row=0,column=4)
bt1=ttk.Button(root,text='                                  轻触来解锁                                  ',command=unlock)
print('[信息]正在应用启动窗口模块')
b1.pack()
t1.pack()
w1.pack()
w2.pack()
w3.pack()
w4.pack()
w5.pack()
w6.pack()
b2.pack()
bt1.pack()
root.mainloop()
