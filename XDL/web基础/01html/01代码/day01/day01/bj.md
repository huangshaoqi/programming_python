联系方式:291707309

html
css
bootstrap
javaScript
jquery
vue

数据库 6天

html 超文本标记语言
	 制作网页的语言
	 由一个个标签组成

规范:
	所有标签小写
	双标签必须闭合 单标签可以省略
	标签内部的属性的值必须用双引号

标题标签: h1-h6
	会自动换行
	有默认的样式
段落标签:
	p 有自己的默认样式 会自动换行
	标记一个文本段落 段落和段落之间会有默认的间距
div标签:
	没有默认样式 会自动换行
	一般配和css来做页面的布局

行内标签:
	i,b,strong,em,u,del....
	不会自动换行 有默认样式
	span: 没有默认样式 配和css使用 用来标记一行当中一小段文本

块元素
	自动换行,独占一行
内联元素(行内元素)
	不会自动换行,不独占一行

图片标签
	img:
		src: 图片路径
		alt: 图片描述 当图片加载失败时 作为替换文字出现
		一般设置宽高时  只设置值一个属性 另一个等比例缩放 

连接：a标签
	href: 指定跳转的资源
	target: "_blank" 在新窗口打开加载的资源
锚点：通过a标签的href属性实现页面内部跳转 
	  元素要设置id属性
	  href属性的值设置为 #id值	


表格:
	table
		border: 边框
		cellspacing: 表格和表格之间的而间距
		cellpadding: 表格距离内容之间的间距
	tr
	td/th
		水平对齐方式 align 默认居左 center right 
		垂直方向   : valign 默认居中 top bottom
	colspan: 水平方向合并
	rowspan: 垂直方向合并