# Cookie Monster Secret Recipe

Web, 100 points

## Description:

> Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?You can access the Cookie Monster [here](http://verbal-sleep.picoctf.net:49737/) and good luck

## Hint:

> 1.  Sometimes, the most important information is hidden in plain sight. Have you checked all parts of the webpage?
> 2.  Cookies aren't just for eating - they're also used in web technologies!
> 3.  Web browsers often have tools that can help you inspect various aspects of a webpage, including things you can't see directly.

## Solution:

Đây là 1 thử thách khá đơn giản, khi chúng ta kiểm tra 1 trang web thường sẽ kiểm tra mã HTMl, CSS, Cookie... hoặc dựa vào tên đề

Đăng nhập vào trang web bằng tên và mật khẩu bất kì sau đó kiểm tra cookie sẽ thấy 1 mật mã base64

```
cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzk4RDA2MDNGfQ%3D%3D
```

Giải mã ta nhận được flag

```
picoCTF{c00k1e_m0nster_l0ves_c00kies_98D0603F}
```
