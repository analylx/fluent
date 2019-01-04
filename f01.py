#关于fluent python的笔记

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

#列表推导
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)