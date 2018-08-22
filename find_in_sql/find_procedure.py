import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
search_folder_path = os.path.join(current_dir, migrations)
file_list = list(os.listdir(search_folder_path))


def check_string(substring):
    def find_in_str(string):
        return string.endswith(substring)
    return find_in_str


def check_file(path, substring):
    def check_text(filename):
        file_path = os.path.join(path, filename)
        with open(file_path) as file:
            text = file.read()
            return substring in text
    return check_text


def iterative_file_filter(file_list, ext):
    filtered_file_list = list(filter(check_string(ext), file_list))
    while len(filtered_file_list) > 1:
        query = input('Enter string to find: ')
        filtered_file_list = list(filter(check_file(search_folder_path, query), filtered_file_list))
        for file in filtered_file_list:
            print(file)
        print('Total:', len(filtered_file_list))


if __name__ == '__main__':
    iterative_file_filter(file_list, '.sql')
