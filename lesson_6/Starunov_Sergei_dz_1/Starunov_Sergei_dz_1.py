def logs(file_name='nginx_logs.txt'):
    with open(file_name, encoding='utf-8') as f:
        for line in f:  # line - отдельная строка прочитанная из файла
            data = line.split()
            ip = data[0]
            req_type = data[5].replace('"', '')
            req_res = data[6]
            yield ip, req_type, req_res


log = list(logs())  # sizeof log = 433808 bytes
# with open('all_visitors.txt', 'w', encoding='utf-8') as f:
#     print(*map(lambda x: x, log), file=f, sep='\n')
