#coding:utf-8
import jieba
f = open("shiji.txt","r")
fhand = f.read()
seg_list = jieba.cut(fhand)
words = list(seg_list)
d = {}
for w in words:
    count = d.get(w, 0)
    d[w] = count + 1
print(d)