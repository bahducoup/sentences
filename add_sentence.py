import os

class SentenceData:
    def __init__(self, file_name):
        self.output_file = file_name
        if not os.path.isfile(file_name) or os.stat(file_name).st_size == 0:
            self.num_sentences = 0
        else:
            with open(file_name, 'r') as f:
                for i, l in enumerate(f):
                    pass
                self.num_sentences = i + 1
        print('>> Number of sentence pairs: %d\n' % self.num_sentences)

    def add_sentence_pair(self, fd):
        positive_sentence = input('>> Positive version: ').strip()
        negative_sentence = input('>> Negative version: ').strip()
        fd.write(positive_sentence + '\t')
        fd.write(negative_sentence + '\n')
        print('positive sentence: [%s]' % positive_sentence)
        print('negative sentence: [%s]\n' % negative_sentence)


    def run(self):
        print('>> Program Start!\n')

        with open(self.output_file, 'a') as fd:
            while True:
                if input('Would you like to add an input? (y/n): ').strip().lower() == 'n':
                    print('>> Bye!')
                    break
            
                self.add_sentence_pair(fd)

if __name__ == '__main__':
    sd = SentenceData('sentence_data.tsv')
    sd.run()
