import math
import os
import requests
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from chapter16.spider.time_cost import time_use

# 创建请求头和会话
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) '
                         'Gecko/20100101 Firefox/41.0'}
"""
创建一个session对象
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出
的所有请求之间保持cookies。
session对象还能为我们提供请求方法的缺省数据，通过设置session对象的属性来实现。
"""
session = requests.session()

# 取得文件完整路径
txt_file_path = os.path.join(os.getcwd(), 'files/t_singer_info.txt')


# 获取歌手的全部歌曲
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
        response = session.get(url)
        # 获取歌手姓名
        song_singer = response.json()['data']['singer_name']
        # 获取歌曲总数
        song_count = str(response.json()['data']['total'])
        print('歌手名称:{}, 歌手歌曲总数:{}'.format(song_singer, song_count))

        singer_info = ','.join([song_singer, song_count, singer_mid, '\n'])

        with open(txt_file_path, 'a') as f_write:
            f_write.write(singer_info)
    except Exception as ex:
        print('get singer info error:{}'.format(ex))


# 获取当前字母下全部歌手
def get_alphabet_singer(alphabet, page_list):
    for page_num in page_list:
        url = f'https://c.y.qq.com/v8/fcg-bin/v8.fcg?channel=singer' \
              f'&page=list&key=all_all_{alphabet}&pagesize=100' \
              f'&pagenum={page_num + 1}&loginUin=0&hostUin=0&format=jsonp'
        response = session.get(url)
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


# 多线程
def multi_threading(alphabet):
    # 每个字母分类的歌手列表页数
    url = f'https://c.y.qq.com/v8/fcg-bin/v8.fcg?channel=singer' \
          f'&page=list&key=all_all_{alphabet}&pagesize=100' \
          f'&pagenum={1}&loginUin=0&hostUin=0&format=jsonp'
    r = session.get(url, headers=headers)
    page_num = r.json()['data']['total_page']
    page_list = [x for x in range(page_num)]
    thread_num = 10
    # 将每个分类总页数平均分给线程数
    per_thread_page = math.ceil(page_num / thread_num)
    # 设置线程对象
    thread_obj = ThreadPoolExecutor(max_workers=thread_num)
    for thread_order in range(thread_num):
        # 计算每条线程应执行的页数
        start_num = per_thread_page * thread_order
        if per_thread_page * (thread_order + 1) <= page_num:
            end_num = per_thread_page * (thread_order + 1)
        else:
            end_num = page_num
        # 每个线程各自执行不同的歌手列表页数
        thread_obj.submit(get_alphabet_singer, alphabet, page_list[start_num: end_num])

# 多进程
@time_use
def execute_process():
    # # max_workers 用于指定进程数
    with ProcessPoolExecutor(max_workers=4) as executor:
        for i in range(65, 90):
            # 创建26个线程，分别执行A-Z分类
            executor.submit(multi_threading, chr(i))


if __name__ == '__main__':
    # 执行多进程多线程
    execute_process()
