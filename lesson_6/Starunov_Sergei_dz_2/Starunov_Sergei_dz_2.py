def logs(file_name='nginx_logs.txt'):
    with open(file_name, encoding='utf-8') as f:
        for line in f:  # line - отдельная строка прочитанная из файла
            data = line.split()
            ip = data[0]
            req_type = data[5].replace('"', '')
            req_res = data[6]
            yield ip, req_type, req_res


visitors = {}
for line in logs():
    ip = line[0]
    if ip in visitors:
        visitors[ip] += 1
    else:
        visitors[ip] = 1
ip, requests = sorted(visitors.items(), key=lambda x: x[1])[-1]
print('spammer ip: ', ip, '\n', 'value requests: ', requests, sep='')
