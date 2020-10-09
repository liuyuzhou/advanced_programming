import time
import csv
import os

from chapter15.memory_monitor import monitor_info

csv_file_path = os.path.join(os.getcwd(), 'files/query_hive.csv')
# 取得文件完整路径
txt_file_path = os.path.join(os.getcwd(), 'files/batch_read_info.txt')


def lines_count():
    """
    csv文件总行数统计
    :return: 总行数
    """
    f_read = open(csv_file_path, "r")
    cline = 0
    while True:
        buffer = f_read.read(8*1024*1024)
        if not buffer:
            break
        cline += buffer.count('\n')
    f_read.seek(0)
    return cline


# 读取csv文件
def read_csv_file():
    start_time = time.time()
    # csv文件总行数统计
    total_line = lines_count()
    # 打开文件并读取内容
    with open(csv_file_path, 'r') as r_read:
        # 读取csv文件所有内容
        file_read = csv.reader(r_read)
        # 按行遍历读取内容
        row_count = 0
        basic_info_obj_list = list()
        for row in file_read:
            if row_count == 0:
                row_count += 1
                print(row)
                continue

            image_id = row[0]
            file_path = row[1]
            modify_timestamp = row[2]
            product_code = row[3]
            en_name = row[4]
            full_path_id = row[5]
            full_path_en_name = row[6]

            read_info = ','.join([image_id, file_path, modify_timestamp,
                                  product_code, en_name, full_path_id,
                                  full_path_en_name, '\n'])
            basic_info_obj_list.append(read_info)
            row_count += 1

            # 内存使用情况监控
            # is_danger = monitor_info()
            # if is_danger:
            #     print('内存使用超出预定警戒值，程序中断执行。')
            #     break

            # 每1000条记录做一次插入
            if row_count % 1000 == 0:
                with open(txt_file_path, 'a') as f_write:
                    f_write.write(''.join(basic_info_obj_list))
                basic_info_obj_list.clear()
                continue

            # 剩余数据插入数据库
            if row_count == total_line:
                with open(txt_file_path, 'a') as f_write:
                    f_write.write(''.join(basic_info_obj_list))
                basic_info_obj_list.clear()

        print('插入({0})条记录，花费：{1}s'.format(row_count - 1, time.time() - start_time))


if __name__ == "__main__":
    read_csv_file()
