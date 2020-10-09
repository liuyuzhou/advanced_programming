import requests
import os
import time

from functools import wraps

# 创建请求头和会话
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) '
                         'Gecko/20100101 Firefox/41.0'}
"""
创建一个session对象
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例
发出的所有请求之间保持cookies。
session对象还能为我们提供请求方法的缺省数据，通过设置session对象的属性来实现。
"""
req_session = requests.session()

# 取得文件完整路径
txt_file_path = os.path.join(os.getcwd(), 'files/singer_info.txt')


def time_use(func):
    """
    Decorator that reports the execution time.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'func name is: {func.__name__}, time use: {end - start} s')
        return result
    return wrapper


# 获取歌手的全部歌曲
# @profile
def get_singer_songs(singer_mid):
    try:
        """
        获取歌手姓名和歌曲总数
        原生地址形式：
        https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=5381&
        jsonpCallback=MusicJsonCallbacksinger_track&loginUin=0&hostUin=0&
        format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&
        needNewCode=0&singermid=003oUwJ54CMqTT&order=listen&begin=0&num=30&songstatus=1
        优化后地址形式：
        https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&
        singermid=003oUwJ54CMqTT&order=listen&begin=0&num=30&songstatus=1
        """
        url = f'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?' \
              f'loginUin=0&hostUin=0&singermid={singer_mid}' \
              f'&order=listen&begin=0&num=30&songstatus=1'
        response = req_session.get(url)
        # 获取歌手姓名
        song_singer = response.json()['data']['singer_name']
        # 获取歌曲总数
        song_count = str(response.json()['data']['total'])
        print(f'歌手名称:{song_singer}, 歌手歌曲总数:{song_count}')

        singer_info = ','.join([song_singer, song_count, singer_mid, '\n'])

        with open(txt_file_path, 'a') as f_write:
            f_write.write(singer_info)
    except Exception as ex:
        print('get singer info error:{}'.format(ex))


# 获取当前字母下全部歌手
def get_singer_letter(chr_key, page_list):
    for page_num in page_list:
        url = f'https://c.y.qq.com/v8/fcg-bin/v8.fcg?channel=singer&page=list' \
              f'&key=all_all_{chr_key}&pagesize=100&pagenum={page_num + 1}' \
              f'&loginUin=0&hostUin=0&format=jsonp'
        response = req_session.get(url)
        # 循环每一个歌手
        per_singer_count = 0
        for k_item in response.json()['data']['list']:
            singer_mid = k_item['Fsinger_mid']
            get_singer_songs(singer_mid)
            per_singer_count += 1
            # 演示使用，每位歌手最多遍历5首歌
            if per_singer_count > 5:
                break
        # 演示使用，只遍历第一页
        break


# 单进程单线程方式获取全部歌手
@time_use
# @profile
def get_all_singer():
    # 获取字母A-Z全部歌手
    for chr_i in range(65, 91):
        key_chr = chr(chr_i)
        # 获取每个字母分类下总歌手页数
        url = f'https://c.y.qq.com/v8/fcg-bin/v8.fcg?channel=singer&' \
              f'page=list&key=all_all_{key_chr}&pagesize=100&pagenum={1}' \
              f'&loginUin=0&hostUin=0&format=jsonp'
        response = req_session.get(url, headers=headers)
        page_num = response.json()['data']['total_page']
        page_list = [x for x in range(page_num)]
        # 获取当前字母下全部歌手
        get_singer_letter(key_chr, page_list)


if __name__ == '__main__':
    # 获取全部歌手
    get_all_singer()
