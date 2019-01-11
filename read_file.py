if __name__ == '__main__':
    with open('sentence_data.tsv', 'r') as f:
        i = 1
        for line in f:
            sentences = line.strip().split('\t')
            print('%3d.' % i)
            i += 1
            print('\t[ POS ] : %s' % sentences[0])
            print('\t[ NEG ] : %s' % sentences[1])
            print('')
