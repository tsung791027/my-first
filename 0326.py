#ch9_29
'''seq1 = ['name', 'city']
list_dict1 = dict.fromkeys(seq1)
print('字典1   :', list_dict1)
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print('字典2   :', list_dict2)

seq2 = ('name', 'city')
tup_dict1 = dict.fromkeys(seq2)
print('字典3   :', tup_dict1)
print(seq1,seq2)'''

#ch9_31
"""song = '''Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding ding, Ding ding ding.'''

mydict = {}
print('原始歌詞')
print(song)

songLower = song.lower()
print('小寫歌詞')
print(songLower)

for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch,' ')
print('不在有標點符號的歌詞')
print(songLower)

songlist = songLower.split()
print('以下是歌詞串列')
print(songlist)

for wd in songlist:
    if wd in mydict:
        mydict[wd] += 1
    else:
        mydict[wd] = 1
print('以下是最後執行結果')
print(mydict)"""

pysong = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! '''

mypy = {}
x = pysong.lower()
for ch in x:
    if ch in ",.?*-!":
        x = x.replace(ch, ' ')
print(x)

song = x.split()
for wd in song:
    if wd in mypy:
        mypy[wd] += 1
    else:
        mypy[wd] = 1
print(mypy)