# cvtools

OpenCV tools for cv applications.

## cvtools.cv_load_image 

Use opencv to load images, either in local file system or remote http servers.

```
from cvtools import cv_load_image
cv_load_image('https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=4234657924,3898859385&fm=173&app=25&f=JPEG?w=640&h=756&s=DA202EC74623C8EE582E73620300D07F')
```

## cvtools.get_image_info

To get image meta info really fast.

```
from cvtools import get_image_info, verify_jpeg
with open("test.png", 'rb') as f:
    print(get_image_info(f))
    print(verify_jpeg(f))

# 'image/png', 1506, 1186
# False
```
