import time
import csv
import os

from chapter15.memory_monitor import monitor_info

csv_file_path = os.path.join(os.getcwd(), 'files/query_hive.csv')
# 取得文件完整路径
txt_file_path = os.path.join(os.getcwd(), 'files/read_info.txt')


# 读取csv文件
def read_csv_file():
    start_time = time.time()
    # 打开文件并读取内容
    with open(csv_file_path, 'r') as r_read:
        # 读取csv文件所有内容
        file_read = csv.reader(r_read)
        # 按行遍历读取内容
        row_count = 0
        # 按行读取csv文件内容，并按行插入mysql
        for row in file_read:
            if row_count == 0:
                row_count += 1
                print(row)
                continue

            row_count += 1
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
            with open(txt_file_path, 'a') as f_write:
                f_write.write(read_info)

            # 内存使用情况监控
            # is_danger = monitor_info()
            # if is_danger:
            #     print('内存使用超出预定警戒值，程序中断执行。')
            #     break
        print('完成插入({0})条记录，花费：{1}s'.format(row_count - 1, time.time() - start_time))


if __name__ == "__main__":
    read_csv_file()
