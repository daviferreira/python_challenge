from string import maketrans

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

_in = "abcdefghijklmnopqrstuvwxyz .'()"
_out = "cdefghijklmnopqrstuvwxyzab .'()"
trans = maketrans(_in, _out)

print text.translate(trans)
