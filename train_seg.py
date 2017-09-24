# -*- coding:UTF-8 -*-
import csv
import jieba
from gensim.models import word2vec
import re
import codecs

def read_csv(excel_path,save_path):
    with open(excel_path) as csv_file:
        datas = csv.reader(csv_file)
        col = [data[5] for data in datas]#第五列为评论文本
        # print col

    with open(save_path,'w') as w:
        for index in range(1,len(col)):
            col[index]
            w.write(col[index])
            w.write('\n')
            w.flush()
            # w.write()
#分词，拆分测试与训练集
def segmentation(original_path, train_save_path,test_save_path,word2vec_path):
    with open(original_path) as f:
        lines = f.readlines()
    sentences = []
    test_sub = len(lines)/10
    for index,line in enumerate(lines):#按行循环
        wordlist = list(jieba.cut(line))#分词
        words = ''
        for word in wordlist:
            words = words + word + ' '#分词后结果以空格拼接成字符串
        words = words.strip().encode('utf-8')#去掉首尾空白
        ori_words = words
        with codecs.open(word2vec_path, 'a', 'utf-8') as w:#将分词后全部文本保存
            words = re.sub('\s+', ' ', words).strip().decode('utf-8')
            w.write(words)
            w.write('\n')
            w.flush()
        if index < test_sub:#写入测试文件
            with codecs.open(test_save_path, 'a', 'utf-8') as w:
                words = re.sub('\s+', ' ', ori_words).strip().decode('utf-8')
                w.write(words)
                w.write('\n')
                w.flush()
        else:#写入训练文件
            with codecs.open(train_save_path, 'a','utf-8') as w:
                words = re.sub('\s+',' ',ori_words).strip().decode('utf-8')
                w.write(words)
                w.write('\n')
                w.flush()

        #train the word2vec
        sentences.append(words)

if __name__ == '__main__':
    read_csv('original_data/好评.csv'.decode('utf-8'), 'train_data/polarity_pos')#提取csv格式的原文本
    read_csv('original_data/差评.csv'.decode('utf-8'), 'train_data/polarity_neg')
    segmentation('train_data/polarity_pos', 'train_data/segment_pos','train_data/test_segment_pos','train_data/word2vec_data')
    segmentation('train_data/polarity_neg', 'train_data/segment_neg','train_data/test_segment_neg','train_data/word2vec_data')