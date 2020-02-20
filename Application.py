#ZZUjksb自动填写 Ver 1.4
ver = 1.4
#By Clok Much
'''
0 说明
    0.0 此仅供参考学习，请在执行代码前仔细检查是否合理，如认为
        不合理，请不要运行.

    0.1 此内容由 Clok Much 编写，如有修改，请在修改后的副本内
        添加原作者（我 qwq）.

    0.2 用于每次开机自动填报jksb健康上报，以免忘记或错过时间.

    0.3 当自动上报中断，手动操作时，浏览器提示安全证书有问题，
        不能继续时，请暂时换用你原来的上报方式，这个问题似乎是
        网站本身证书的问题，主要需要校方解决，或者你可以自行查
        找解决方法.

    0.4 请仔细阅读附带的说明文档.


1 准备使用
    1.1 下载安装 Mozilla Firefox
            请在此网站下载 Mozilla Firefox：
                https://www.firefox.com.cn/
            然后安装（安装步骤略）.
    
    1.2 将 Mozilla Firefox 所在目录添加到系统环境变量 PATH 中，
        安装目录一般为：
            C:\Program Files\Mozilla Firefox
        具体步骤略（以后的版本再加个 Word 文档详细说明吧 qwq）.

    1.3 将本安装包内附带的 geckodriver.exe 文件拷贝至 Mozilla 
        Firefox 的安装目录（见1.2）.

    1.4 使用 pip 安装 selenium 库，为提升安装体验，建议在 pip 
        所在目录执行如下安装命令（使用清华大学的源，安装比较快
         qwq）：
            pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
        具体步骤略（以后的版本再说吧 qwq）.

    1.5 至此，你已经可以运行 jksb 了，后续将介绍如何配置 jksb .

2 配置 jksb
    2.1 打开 py 源码，找到“用户信息配置”，然后按提示填写学号
        、密码及指示文件目录.

    2.2（可选） 创建 Application.py 的快捷方式，并将其移动到启
    动目录，或添加到计划任务，以实现每次开机自动运行.

    2.3 再次检查指示文件目录是否存在、学号密码是否正确.

    2.4 至此，你已经完成了 jksb 的配置，后续将介绍 jksb 的其他
        信息.

3 jksb
    3.1 更新历史
            1.1
                项目启动.

            1.2
                增加可靠性：可人工检查是否上报完成（未来设计为自
                动检查）.

            1.3
                简化流程，便于修改；
                程序启动时判断今日是否已经上报.

            1.4
                重写说明文档；
                优化逻辑.

    3.2 联系作者
            如果此程序出现问题，或有其他改进方案，或者想要和我一
            起打游戏（QwQ），可通过以下电邮联系我：
                1831158739@qq.com
'''

#用户信息配置
uid = ""  #在双引号间输入学号
upw = ""  #在双引号间输入密码，当密码包含引号时，请自行更改最外层引号
inct_dir = "V:\\1\\"  #输入工作文件夹，斜杠使用双斜杠代替，以斜杠结尾，请注意运行用户有此目录的读写权限






#导入所需库
#from selenium import webdriver  #（导入与简化不放在开头，以提高运行效率）
import time
from time import sleep
from os import path
#简化
#fx = webdriver.Firefox()  #（导入与简化不放在开头，以提高运行效率）
#简述版本情况
print("jksb.Ver" + str(ver) + '\n')
#判断指示文件目录是否存在
if path.exists(inct_dir):
    print("当前指示文件目录为：")
    print(inct_dir)
else:
    print("请检查是否已设置指示目录，以及配置是否正确，程序即将退出，再次运行前请检查是否配置正确！")
    input()
    exit()


###以下为函数体部分###

#函数体：获取当前日期，返回指示文件的文件名
def get_name():
    name = time.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')  #直接生成带有中文的名称会报错，似乎是模块自建编码的问题，故使用间接生成
    return name

#函数体：生成指示文件
def creat_inct(name):
    tmp = inct_dir + name
    open(tmp, 'w').write('SUCCEED')

#函数体：进行上报与确认
def jksb(check=False):
    #准备webdriver（导入与简化不放在开头，以提高运行效率）
    from selenium import webdriver
    fx = webdriver.Firefox()

    fx.get('http://jksb.zzu.edu.cn')  #开启网页
    fx.switch_to.frame("my_toprr")  #切换框架到登录
    fx.find_element_by_name("uid").clear()  #清除原有学号
    fx.find_element_by_name("uid").send_keys(uid)  #填入学号
    fx.find_element_by_name("upw").clear()  #清除原有密码
    fx.find_element_by_name("upw").send_keys(upw)  #填入密码
    fx.find_element_by_name("smbtn").click()  #点击登录
    if check != True:
        sleep(5)  #等待加载，若出现错误可增加等待时间
        fx.switch_to.default_content()  #回到原始框架
        fx.switch_to.frame("zzj_top_6s")  #切入新的框架
        fx.find_element_by_xpath("/html/body/form/div[1]/div[15]/div[4]/span").click()  #点击下一步
        sleep(5)  #等待加载，若出现错误可增加等待时间
        fx.find_element_by_xpath("/html/body/form/div[1]/div[14]/div[4]/span").click()  #点击上报
        sleep(5)  #等待加载，若出现错误可增加等待时间
        #fx.quit()  #不再关闭浏览器，等待查看是否上报成功

###以上为函数体部分###

###以下为运行部分###

#检查今日是否已运行
if path.exists(inct_dir + get_name() + 'a'):
    print("\n今天已运行本工具，并且二次确认已上报成功！")
    input()
    exit()
elif path.exists(inct_dir + get_name()):
    print("你今天已经上报，还需要再次确定吗？输入y表示确认，否则请直接退出.")
    tmp = input()
    while tmp != 'y':
        print("你输入了其他内容，如果需要再次检查请输入y，否则请直接退出.")
        tmp = input()
    #开始再次检查
    print("开始二次确认...\n\n")
    jksb(check=True)
    print("上报是否成功？若成功，请输入y，否则请自行上报，然后直接退出.\n")
    tmp = input()
    while tmp != 'y':
        print("你输入了其他内容，如果成功上报请输入y，否则自行上报，然后直接退出.")
        tmp = input()
    creat_inct(get_name() + 'a')
    exit()


#没有上报时的流程
print("\n今天没有运行 jksb ，正在准备上报...")
jksb()
creat_inct(get_name())


#说明
print("\n\n\n运行结束！您可以直接关闭本窗口和一同打开的浏览器.")
input()