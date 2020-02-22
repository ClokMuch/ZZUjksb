###以下为函数体部分###

##用户配置信息相关##
#函数体：创建配置
def creat_config():
    from os import mkdir
    uid = input('输入你的学号（12位）：\n')
    while len(uid) != 12:
        uid = input('你的输入长度有误，请再次输入：\n')
    upw = input('输入你的密码：\n')
    open('uid','w').write(uid)
    open('upw','w').write(upw)
    mkdir(get_config() + '\\')

#函数体：读取配置
def get_config(config_name='inct_dir'):
    '''默认返回指示文件目录'''
    if config_name == 'uid':
        uid = open('uid','r').read()
        return uid
    elif config_name == 'upw':
        upw = open('upw','r').read()
        return upw
    else:
        import sys
        inct_dir = sys.path[0] + '\\inct\\'
        return inct_dir

#函数体：判断配置是否存在，存在返回 True，否则创建
def chk_config():
    from os import path
    if path.exists('uid') and path.exists('upw') and path.exists(get_config()):
        print("检查到存在配置文件，正在载入...")
        return True
        
    else:
        print("没有创建配置文件，请根据提示进行创建.")
        creat_config()
##用户配置信息结束##

#函数体：获取当前日期，返回指示文件的文件名
def get_name(checked=False):
    import time
    if checked == True:
        name = time.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日') + 'a'  #直接生成带有中文的名称会报错，似乎是模块自建编码的问题，故使用间接生成
    else:
        name = time.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')  #直接生成带有中文的名称会报错，似乎是模块自建编码的问题，故使用间接生成
    return name

#函数体：生成指示文件
def creat_inct(name):
    tmp = get_config() + name
    open(tmp, 'w').write('SUCCEED')

#函数体：进行上报与确认
def jksb(check=False):
    #准备webdriver（导入与简化不放在开头，以提高运行效率）
    from selenium import webdriver
    from time import sleep
    fx = webdriver.Firefox()

    fx.get('http:\\\\jksb.zzu.edu.cn')  #开启网页
    fx.switch_to.frame("my_toprr")  #切换框架到登录
    fx.find_element_by_name("uid").clear()  #清除原有学号
    fx.find_element_by_name("uid").send_keys(get_config('uid'))  #填入学号
    fx.find_element_by_name("upw").clear()  #清除原有密码
    fx.find_element_by_name("upw").send_keys(get_config('upw'))  #填入密码
    fx.find_element_by_name("smbtn").click()  #点击登录
    if check != True:
        sleep(5)  #等待加载，若出现错误可增加等待时间
        fx.switch_to.default_content()  #回到原始框架
        fx.switch_to.frame("zzj_top_6s")  #切入新的框架
        fx.find_element_by_xpath("/html/body/form/div[1]/div[17]/div[4]/span").click()  #点击下一步
        sleep(5)  #等待加载，若出现错误可增加等待时间
        fx.find_element_by_xpath("/html/body/form/div[1]/div[13]/div[4]/span").click()  #点击上报
        sleep(5)  #等待加载，若出现错误可增加等待时间
        #fx.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[2]/div[4]/div[2]").click()  #上报完成，点击确认
        fx.get('http:\\\\jksb.zzu.edu.cn')  #开启网页
        fx.switch_to.frame("my_toprr")  #切换框架到登录
        fx.find_element_by_name("uid").clear()  #清除原有学号
        fx.find_element_by_name("uid").send_keys(get_config('uid'))  #填入学号
        fx.find_element_by_name("upw").clear()  #清除原有密码
        fx.find_element_by_name("upw").send_keys(get_config('upw'))  #填入密码
        fx.find_element_by_name("smbtn").click()  #点击登录
        #fx.quit()  #不再关闭浏览器，等待查看是否上报成功

#函数体：判断运行情况
def run():
    '''
    检查运行情况，根据不同情况进行操作，未运行时无操作
    '''
    from os import path
    if path.exists(get_config() + get_name(checked=True)):
        print("\n今天已运行本工具，并且二次确认已上报成功！")
        input()
        exit()
    elif path.exists(get_config() + get_name()):
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
        creat_inct(get_name(checked=True))
        exit()


###以上为函数体部分###
