1.修改了 gulp rev 插件的源码：替换 \\ 为 /
line 16 修改为：
	if (newPath[0] === path.sep) {
		return newPath.substr(1).replace(/\\/g, '/');
	} else {
		return newPath.replace(/\\/g, '/');
	}
2.
项目路径：各个操作系统不一样，apache\django.wsgi
windows 为：path = 'D:\Projects\chongwug\chongwug'