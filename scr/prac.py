# s = "test hello"
# print(s[::10])
#
# sample_set = {1,2,3,4}
#
# print(type(sample_set))
#
# test_dict = {1:2, 'garbage': 'data'}
#
# test_set = {"remember that", "primitives ", "can be keys"}
# ttest_set = {"remember", "primitis ", "can be keys"}
#
# print(test_set.union(ttest_set))
# print(test_set.intersection(ttest_set))
#
#
# print(test_dict.items())
#
# for item in test_dict.items():
#     print(type(item))
#
#

a = [1,2,3]
b = a
b[0] = 100000
print(a)

# python has references

c = [lambda x: x+i for i in range(3)]

for i in c:
    print(i)


k = ord('0')
bb = chr(k)


print(k)
print(bb)