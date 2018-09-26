# time 模块总结
## 1. 字符串转时间对象
```python
import time
str1 = "2018-09-25 12:30:00"
res = time.strptime(str1,"%Y-%m-%d %H:%M:%S")
print(res)
# Output:time.struct_time(tm_year=2018, tm_mon=9, tm_mday=25, tm_hour=12, tm_min=30, tm_sec=0, tm_wday=1, tm_yday=268, tm_isdst=-1)
```

## 2. 字符串转时间戳

```python
import time
str1 = "2018-09-25 12:30:00"
res = time.mktime(time.strptime(str1,"%Y-%m-%d %H:%M:%S"))
print(res)
#Output:1537849800.0
```

## 3. 时间对象转字符串
```python
import time
date_obj = time.localtime()
res = time.strftime("%Y-%m-%d %H:%M:%S",date_obj)
print(res)
#Output:2018-09-25 13:35:58
```
## 4. 时间对象转时间戳
```python
import time
date_obj = time.localtime()
res = time.mktime(date_obj)
print(res)
# Output:1537853910.0
```
## 5. 时间戳转字符串
```python
import time
date_c = 1537853910.0
res = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(date_c))
print(res)
# Output:2018-09-25 13:38:30
```
## 6. 时间戳转时间对象
```python
import time
date_c = 1537853910.0
res = time.localtime(date_c)
print(res)
# Output:time.struct_time(tm_year=2018, tm_mon=9, tm_mday=25, tm_hour=13, tm_min=38, tm_sec=30, tm_wday=1, tm_yday=268, tm_isdst=0)
```