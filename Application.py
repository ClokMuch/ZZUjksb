#ZZUjksb自动填写 Ver 1.10
ver = '1.10'  ###施工中！！！
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
    2.1 运行 Application.py ，按提示填写你的学号和密码.

    2.2（可选） 为 Application.py 创建快捷方式，以快速运行.

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
                
            1.5
                更新元素位置.

            1.6
                优化逻辑,分离部分函数体；
                将配置保存为文件，以便升级后免再次配置.

            1.7
                完成后保存网页.

            1.8
                修复网页保存问题；
                优化代码.

            1.9
                更新元素位置.

            1.10
                更换部分逻辑，从而避免切换框架;
                同时保存截图.

    3.2 联系作者
            如果此程序出现问题，或有其他改进方案，或者想要和我一
            起打游戏（QwQ），可通过以下电邮联系我：
                1831158739@qq.com
'''

#导入所需库与函数体
from time import sleep
from jksb import *

#简述版本情况
print("jksb.Ver" + str(ver) + '\n')

#创建或读取配置文件
chk_config()

###以下为运行部分###
#检查今日是否已运行
run()
#没有上报时的流程
print("\n今天没有运行 jksb ，正在准备上报...")
jksb()
creat_inct(get_name())
#说明
print("\n\n\n运行结束！您可以直接关闭本窗口和一同打开的浏览器.")
input()