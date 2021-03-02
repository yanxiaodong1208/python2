def test(aVersion, bVersion):
    # print(version1.rfind('.'),len(version1))
    aIndex1 = aVersion.find('.')
    aIndex2 = aVersion.find('.', aIndex1 + 1)
    aIndex3 = aVersion.find('.', aIndex2 + 1)

    bIndex1 = bVersion.find('.')
    bIndex2 = bVersion.find('.', bIndex1 + 1)
    bIndex3 = bVersion.find('.', aIndex2 + 1)

    # print(aIndex1, aIndex2, aIndex3, bIndex1, bIndex2, bIndex3)

    aVersion1 = int(aVersion[aIndex1 - 1:aIndex1])
    aVersion2 = int(aVersion[aIndex2 - 1:aIndex2])
    aVersion3 = int(aVersion[aIndex3 - 1:aIndex3])
    aVersion4 = int(aVersion[aIndex3 + 1:len(aVersion)])

    bVersion1 = int(bVersion[bIndex1 - 1:bIndex1])
    bVersion2 = int(bVersion[bIndex2 - 1:bIndex2])
    bVersion3 = int(bVersion[bIndex3 - 1:bIndex3])
    bVersion4 = int(bVersion[bIndex3 + 1:len(bVersion)])

    # print(aVersion1, aVersion2, aVersion3, aVersion4 , bVersion1, bVersion2, bVersion3, bVersion4)
    if aVersion1 > bVersion1 or aVersion2 > bVersion2 or aVersion3 > bVersion3 or aVersion4 > bVersion4:
        print("aVersion 大")
    else:
        print("bVersion 大")

for i in range(3):
    a, b = input('输入aVersion,bVersion空格隔开:').split()
    a = str(a)
    b = str(b)
    test(a,b)

# if aVersion1>bVersion1:
#     print("aVersion 大")
# elif aVersion1==bVersion1:
#     if aVersion2>bVersion2:
#         print("aVersion 大")
#     elif aVersion2==bVersion2:
#         if aVersion2>bVersion2:
