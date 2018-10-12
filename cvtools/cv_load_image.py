import requests
import cv2
import numpy as np

# To speed up downloading
cv_session = requests.Session()
cv_session.trust_env = False


def cv_load_image(in_, type_='path'):
    '''
    Return
        image: opencv format np.array. (C x H x W) in BGR np.uint8
    '''
    if type_ == 'url' or in_.startswith('http'):
        img_nparr = np.fromstring(cv_session.get(in_).content, np.uint8)
        img = cv2.imdecode(img_nparr, cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(in_, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
        # img = cv2.imread(in_)
    return img


