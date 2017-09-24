#coding=utf-8
import gensim
from gensim.models import word2vec

class Train_word2vec():
    def __init__(self):
        self.data_path = 'train_data/word2vec_data'
        self.embedding_size = 128

    def load_data(self):
        # with open(self.data_path,'r') as f:
        #     lines = f.readlines()
        lines = word2vec.Text8Corpus(self.data_path)
        print type(lines)
        return lines

    def train_data(self):
        sentences = self.load_data()
        model = word2vec.Word2Vec(sentences,size=self.embedding_size,min_count=0)#min_count 表示去掉低于该词频的词

        model.wv.save_word2vec_format('train_data/word2vec_' + str(self.embedding_size) + '.bin',binary=True)

    def load_model(self):
        model = gensim.models.KeyedVectors.load_word2vec_format('train_data/word2vec_' + str(self.embedding_size) + '.bin',binary=True)
        print model['区别'.decode('utf-8')]

if __name__ == '__main__':
    train_word2vec = Train_word2vec()
    train_word2vec.train_data()
    train_word2vec.load_model()