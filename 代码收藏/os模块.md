# os模块
```python
import os
```
## 执行操作系统命令，并读取结果
```python
os.popen("command").read()
```
## 显示当前系统类型
```python
os.name
# Output:Linux'posix' / Windows'nt' / 'ce' / 'java'
```
## path变量分隔符
```python
os.pathsep
# Output:windows是; linux是:
```
## 查看系统环境变量字典
```python
os.environ
```
## 读取环境变量，没有返回None
```python
os.getenv("key")
```
## 删除环境变量
```python
os.unsetenv("key")
```
## 获取当前路径
```python
os.getcwd()
```
## 切换路径
```python
os.chdir("路径")
```
## 当前系统路径分隔符
```python
os.sep
```
## 列出指定路径下文件和目录
```python
os.listdir("path")
```
## 遍历目录树,返回迭代器(包含dirpath,dirnames[],filenames[])
```python
os.walk("path")
```
## 输出指定路径的绝对路径
```python
os.path.abspath("path")
```
## 拼接路径
```python
os.path.join("path","filename")
```
## 分割路径(返回列表[路径，文件名])
```python
os.path.split(p)
```
## 分离扩展名
```python
os.path.splitext("path")
```
## 获取文件大小
```python
os.path.getsize("filename")
```
## 判断路径是否存在
```python
os.path.exists("path")
```
## 判断是否是文件
```python
os.path.isfile("path")
```
## 判断是否是目录
```python
os.path.isdir("path")
```