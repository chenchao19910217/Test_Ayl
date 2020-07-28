import execjs

# 读取js文件
with open('encrypt.js', encoding='utf-8') as f:
    js = f.read()

# 通过compile命令转成一个js对象
docjs = execjs.compile(js)

# 调用function方法
res = docjs.call('getnow')
print(res)

# 调用变量方法
res = docjs.eval('name')
print(res)