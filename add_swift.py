s = 'swift://'
with open('added_swift.txt', 'w') as out_file:
    with open('all_day_files.txt', 'r') as in_file:
        for line in in_file:
            out_file.write(s+line)