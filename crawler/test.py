import base64, hashlib

print base64.b16encode('zhang-jia-wei')
print hashlib.md5('zhang-jia-wei').hexdigest()
print hashlib.sha1('zhang-jia-wei').hexdigest()
print hashlib.sha512('zhang-jia-wei').hexdigest()
