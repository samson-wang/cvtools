import struct

def get_image_info(datastream):
    '''
    Input: datastream (file like object with .read() and .seek() functions)

    Return:
        content_type: "image/gif" / "image/png" / "image/jpeg". "" if it can not recognize or crash.
        width: with of image. -1 if it can not recognize or crash.
        height: height of image. -1 if it can not recognize or crash.

    '''
#    datastream = ReseekFile(datastream)
    datastream.seek(0)
    data = bytes(datastream.read(30))
    size = len(data)
    height = -1
    width = -1
    content_type = ''

    # handle GIFs
    if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
        # Check to see if content_type is correct
        content_type = 'image/gif'
        w, h = struct.unpack("<HH", data[6:10])
        width = int(w)
        height = int(h)

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n')
          and (data[12:16] == b'IHDR')):
        content_type = 'image/png'
        w, h = struct.unpack(">LL", data[16:24])
        width = int(w)
        height = int(h)

    # Maybe this is for an older PNG version.
    elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        content_type = 'image/png'
        w, h = struct.unpack(">LL", data[8:16])
        width = int(w)
        height = int(h)

    # handle JPEGs
    elif (size >= 2) and data.startswith(b'\377\330'):
        content_type = 'image/jpeg'
        datastream.seek(0)
        jpeg = datastream
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while (b and ord(b) != 0xDA):
                while (ord(b) != 0xFF): b = jpeg.read(1)
                while (ord(b) == 0xFF): b = jpeg.read(1)
                if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                    jpeg.read(3)
                    h, w = struct.unpack(">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(">H", jpeg.read(2))[0])-2)
                b = jpeg.read(1)
            width = int(w)
            height = int(h)
        except struct.error:
            raise
        except ValueError:
            raise
        except:
            raise

    return content_type, width, height

def verify_jpeg(datastream):
    '''
    To verify if a jpeg image is valid.
    Input:
        datastream, 
    Return:
        bool, True if good, False if something weird happens 
    '''
    ENDING = [0xFF, 0xD9]
    try:
        datastream.seek(-2, 2)
    except IOError:
        return False
    for e in ENDING:
        b = datastream.read(1)
        if ord(b) == e:
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], 'rb') as f:
        print(get_image_info(f))
        print(verify_jpeg(f))
