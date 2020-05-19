import os

# Each website crawled is a new proj/folder
def  create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project directory '+ directory)
        os.makedirs(directory)

# Create queue and crawled files
def create_data_files(proj_name, base_url):
    waiting_queue = proj_name + '/waiting_queue.txt'
    crawled_queue = proj_name + '/crawled_queue.txt'
    if not os.path.exists(waiting_queue):
        create_file(waiting_queue, base_url)
    if not os.path.exists(crawled_queue):
        create_file(crawled_queue, '')

# Create new a file
def create_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data to an existing file
def append_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the content of a file
""" 
Just overwriting the old file without writing anything，
because open a file with w mode will erase the file automatically
"""
def clear_file(path):
    with open(path, 'w'):
        pass

# Convert each line of a file to a set
def file_to_set(path):
    ret = set()
    with open(path, 'rt') as file:
        for line in file:
            # Remove the '\n' when we wrote to the file
            ret.add(line.replace('\n', ''))
        return ret

# Convert a set to a file line by line
def set_to_file(set, path):
    clear_file(path)
    for link in sorted(set):
        append_file(path, link)

