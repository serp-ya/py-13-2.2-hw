import chardet


def read_files(file_names_list):
    result_dict = dict()

    for file_name in file_names_list:

        with open('./sources/' + file_name, 'rb') as f:
            data = f.read()
            result = chardet.detect(data)

            result_dict[file_name] = data.decode(result['encoding'])

    return result_dict


def split_words_in_news_dict(news_dict):
    result_dict = dict()

    for filename in news_dict:
        result_dict[filename] = news_dict[filename].split(' ')

    return result_dict


def formating_lowercase_words_in_news_dict(news_dict):
    result_dict = dict()

    for filename in news_dict:
        result_dict[filename] = list()

        for word in news_dict[filename]:
            result_dict[filename] += [word.lower()]

    return result_dict


def count_words_in_news_dict(news_dict):
    result_dict = dict()

    for filename in news_dict:
        result_dict[filename] = dict()

        for word in news_dict[filename]:
            result_dict[filename][word] = news_dict[filename].count(word)

    return result_dict


def formating_counted_words_in_new_dict(news_dict):
    result_dict = dict()

    for filename in news_dict:
        result_dict[filename] = list()

        for word in news_dict[filename]:
            word_data = dict()
            word_data['word'] = word
            word_data['count'] = news_dict[filename][word]

            result_dict[filename] += [word_data]

    return result_dict


def sort_popular_words_in_new_dict(news_dict):
    result_dict = news_dict.copy()

    def sort_by_count(item):
        return item['count']

    for filename in news_dict:
        result_dict[filename].sort(key=sort_by_count, reverse=True)

    return result_dict


def filtering_words_by_length(news_dict):
    result_dict = dict()

    for filename in news_dict:
        result_dict[filename] = list()

        for word_data in news_dict[filename]:
            if len(word_data['word']) >= 6:
                result_dict[filename] += [word_data]

    return result_dict


def core():
    file_names_list = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']
    news_dict = read_files(file_names_list)

    news_dict_splited_by_words = split_words_in_news_dict(news_dict)
    news_dict_with_lowercase_words = formating_lowercase_words_in_news_dict(news_dict_splited_by_words)
    news_dict_with_counted_words = count_words_in_news_dict(news_dict_with_lowercase_words)
    news_dict_with_formated_words_list = formating_counted_words_in_new_dict(news_dict_with_counted_words)
    news_dict_with_sorted_words = sort_popular_words_in_new_dict(news_dict_with_formated_words_list)
    news_dict_filtered_by_length = filtering_words_by_length(news_dict_with_sorted_words)

    for filename in news_dict_filtered_by_length:
        print('\nТоп-10 самых популярных слов в файле {0}'.format(filename))

        for i in range(10):
            word_data = news_dict_filtered_by_length[filename][i]
            word = word_data['word']
            count = word_data['count']

            print('{0}. Слово "{1}" встречалось {2} раз!'.format(i + 1, word, count))


core()
