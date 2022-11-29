
def generate_hashtag(s):

    string = '#' + s.title().replace(' ', '')
    return string


if __name__ == '__main__':

    string = ' Hello there thanks for trying my Kata '
    print(generate_hashtag(string))