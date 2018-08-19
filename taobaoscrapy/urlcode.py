from urllib.parse import quote

def encode(data,code):
    res = data.encode(code)
    return quote(res)
