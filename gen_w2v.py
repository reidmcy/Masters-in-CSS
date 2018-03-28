import pandas
import gensim
import io
import simple_id
import simple_id.utilities

target = '../data/full_ss.tsv'

def main():
    df_data = pandas.read_csv(target, sep = '\t', error_bad_lines=False)
    simple_id.preprocesing(df_data, 'w2v', 'w2v.bin', 'full_pickle.p', 200, useFeather = False)

if __name__ == '__main__':
    main()
