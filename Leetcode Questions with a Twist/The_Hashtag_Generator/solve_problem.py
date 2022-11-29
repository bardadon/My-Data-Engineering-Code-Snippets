import pandas as pd

def generate_hashtag():

    def process_hashtag(s):

        if len(s) < 1:
            return False

        string = '#' + s.title().replace(' ', '')

        if len(string) > 140:
            return False
        else:
            return string


    input_strings = pd.read_csv('input_data.csv')
    input_list = input_strings.string.to_list()
    input_results = dict()

    for input_data in input_list:
        input_results[input_data] = process_hashtag(input_data)



    df = pd.DataFrame.from_dict(input_results.items())
    df.rename({0:'Input', 1:'Solution'}, axis=1, inplace = True)
    df.to_csv('solution.csv', index=None)

if __name__ == '__main__':
    
    generate_hashtag()
    df = pd.read_csv('solution.csv')
    print(df)
