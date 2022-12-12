# https://adventofcode.com/2022/day/7
import common
import re

input = common.read_file(day='07', type='final')
steps = input.strip('\n').split('\n$ ')

tree_root = {}
tree_root['_dir_parent'] = tree_root
tree_root['_dir_name'] = '/'
cwd = tree_root

def create_dir_metadata(cwd, dir_name):
    new_metadata = {
        '_dir_parent': cwd,
        '_dir_name': dir_name
    }
    cwd[dir_name] = new_metadata
    return new_metadata


for step in steps:
    if 'cd /' in step:
        cwd = tree_root
        continue

    elif step.startswith('ls\n'):
        dir_list = step[3:].split('\n')

        for item in dir_list:
            if item.startswith('dir '):
                dir_name = item[4:]
                create_dir_metadata(cwd, dir_name)
            else:
                file_size, file_name = re.search(r'(\d+) (.+)', item).groups()
                cwd[file_name] = int(file_size)

    elif step.startswith('cd '):
        new_dir = step[3:]

        if new_dir == '..':
            cwd = cwd['_dir_parent']
        else:
            create_dir_metadata(cwd, new_dir)
            cwd = cwd[new_dir]


def compute_dir_sizes(root):
    total_size = 0
    for key, value in root.items():
        if key.startswith('_'):
            continue
        if type(value) == dict:
            total_size += compute_dir_sizes(value)
        if type(value) == int:
            total_size += value
    root['_total_size'] = total_size
    return total_size


def sum_dirs_over(root, size):
    total = 0

    for key, value in root.items():
        if key == '_dir_parent':
            continue
        if type(value) == dict:
            total += sum_dirs_over(value, size)

    if root['_total_size'] <= size:
        total += root['_total_size']

    return total

total_used_space = compute_dir_sizes(tree_root)
total = sum_dirs_over(tree_root, 100000)
print(total)  # Part 1


def collect_dir_sizes(root):
    dir_sizes = []

    for key, value in root.items():
        if key == '_dir_parent':
            continue
        if type(value) == dict:
            dir_sizes.extend(collect_dir_sizes(value))

    return [root['_total_size'], *dir_sizes]


disk_size = 70000000
update_size = 30000000
free_space = disk_size - total_used_space
need_to_free = update_size - free_space

dir_sizes = collect_dir_sizes(tree_root)
smallest = [x for x in sorted(dir_sizes) if x >= need_to_free][0]
print(smallest)  # Part 2
