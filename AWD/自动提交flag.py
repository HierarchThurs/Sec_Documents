#!/usr/bin/env python2
import sys
import json
import urllib
import httplib
server_host = ' '    #�ύflag�ķ�������ַ
server_port = 80
def submit(team_token, flag, host=server_host, port=server_port, timeout=5):
    if not team_token or not flag:
        raise Exception('team token or flag wrong')
    conn = httplib.HTTPConnection(host, port, timeout=timeout)
    params = urllib.urlencode({        #�ύ��Ҫpost�Ĳ���,��������޸�
        'token': team_token,    
        'flag': flag,
    })
    headers = {
        "Content-type": "application/x-www-form-urlencode"
    }
    conn.request('POST', '[submit_flag_dir]', params, headers)    #�ڶ�������Ϊ�ύflag��Ŀ¼
    response = conn.getresponse()
    data = response.read()
    return json.loads(data)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: ./submitflag.py [team_token] [flag]'
        sys.exit()
    host = server_host
    if len(sys.argv) > 3:
        host = sys.argv[3]
    print json.dumps(submit(sys.argv[1], sys.argv[2], host=host), indent=4)