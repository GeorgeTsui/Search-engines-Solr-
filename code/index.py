# -*- coding:utf-8 -*-
from whoosh.fields import *
import os.path
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.query import *
from jieba.analyse import ChineseAnalyzer

"""class ChineseTokenizer(Tokenizer):
#def __call__(self, value, positions=False, chars=False, keeporiginal=False, removestops=True, start_pos=0, start_char=0, mode='', **kwargs):
# assert isinstance(value, text_type), "%r is not unicode" %value 
  t = Token(positions, chars, removestops=removestops, mode=mode,**kwargs)
  seglist=jieba.cut(value,cut_all=False)                       #使用结巴分词库进行分词
  for w in seglist:
   t.original = t.text = w
   t.boost = 1.0
   if positions:
     t.pos=start_pos+value.find(w)
   if chars:
     t.startchar=start_char+value.find(w)
     t.endchar=start_char+value.find(w)+len(w)
   yield t                                               #通过生成器返回每个分词的结果token

def ChineseAnalyzer():
	return ChineseTokenizer()
"""
analyzer = ChineseAnalyzer()
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
if not os.path.exists("index"):
	os.mkdir("index")

ix = create_in("index", schema)
#iix = open_dir("index")
writer = ix.writer()
writer.add_document(title=u"First document", path=u"/a",content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/a",content=u"The second one 你 中文测试中文 is even more interesting!")
writer.commit()

#with ix.searcher() as searcher:
#	myquery = QueryParser("content", ix.schema).parse("interesting")
#	results = searcher.search(myquery)
#	print results[0]

searcher = ix.searcher()
results = searcher.find("content", u"你")  
print results[0]
results = searcher.find("content", u"测试")
print results[0]

