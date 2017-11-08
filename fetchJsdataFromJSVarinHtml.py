response.xpath("//footer[@class='footer']").extract() #   Get the footer content 
  
response.xpath("//body").re(r'metaData = \s*(.*)') # 获取到了json对象，但是多出了一串字符，需要去掉。

response.xpath("//body").re(r'metaData\s*(.*)')


response.xpath("//body").re(r'metaData\s=\s*(.*)};') # 这个实现了从html中的javascript里面抽取json对象，正则式中使用$符号限制以什么字符结尾的方式不起作用，直接把要做为结尾的字符放到正则表达式中即可。
