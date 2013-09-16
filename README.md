PFetion  
==========

**尝试做一个自己的Fetion版本 基于 [PyWapFetion](https://github.com/whtsky/PyWapFetion). 感谢[whtsky](http://whouz.com/)**

PyWapFetion是一个飞信的Python模块，使用Wap飞信协议。  
因为目前没有看到比较好的Python飞信模块（PyFetion虽然很强大，但是基于电脑客户端的协议，容易被各种验证码问题所困扰），所以自己动手写了一个。

安装
---------------

在终端下输入（*nix）： `sudo pip install PyWapFetion` 或者 `sudo easy_install -U PyWapFetion`  
或者把源码下载下来，运行：`python setup.py install`

使用
---------------

	from PyWapFetion import Fetion, send2self, send

	#快速发送：
	send2self('手机号',  '密码', '信息')
	send('手机号', '密码', '接收方手机号', '信息')

	#----------------------------------------------------------------------
	myfetion = Fetion('手机号', '密码')

	myfetion.changestatus('0')  # 改变在线状态

	myfetion.send2self('发给自己的东西')
	myfetion.findid('输入手机号，返回飞信ID')
	myfetion.sendBYid('飞信ID', '消息')
	myfetion.send('手机号', '消息', sm=True)  # 发送飞信信息
	#通过设定sm=True强制发送短信（sm=ShortMessage）
	myfetion.send('昵称', '消息')  # 你也可以这么干
	myfetion.addfriend('手机号', '你的昵称（5字以内）')
	myfetion.send(['手机号1', '手机号2', '这就是传说中的群发'], '消息')
	  # 成功返回True，失败返回False

	myfetion.send2self('这个是发给自己的定时短信', time='201111201120')
	'''发送定时短信。格式：年月日小时分钟
	如：2011年11月20日11时14分：201111201144
		2012年11月11日11时11分：201211111111
	注意：时间允许范围：当前时刻向后10分钟-向后1年
	如：当前时间：2011年11月20日 11:17
	效时间范围是:2011年11月20日11:27分到2012年11月20日11:27分
	'''

	myfetion.changeimpresa('改签名')
	myfetion.alive()  # 保持在线，10分钟以上无操作会被判定为离线
	#如果你想要自动保持在线，那么：
	from PyWapFetion.AliveKeeper import AliveKeeper
	AliveKeeper(myfetion)

	myfetion.deletefriend('要删除的好友ID')
	myfetion.addblacklist('要拉黑的好友ID')
	myfetion.relieveblack('要解除拉黑的好友ID')

	myfetion.logout()
	  # -----------------------------------------------------------------------

	with Fetion('手机号', '密码') as f:  # 其实你也可以用with，这样更方便一点
    	f.send2self('xxxx')