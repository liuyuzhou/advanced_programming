from collections import Counter
words = [
    'python', 'c++', 'abc', 'php', 'mysql', 'java', 'c#', '.net',
    'ruby', 'lisp', 'python', 'python', 'mongodb', 'hive', 'spark', 'go', 'vb',
    'java', "python", 'c', 'ios', 'sql', 'python', 'java', 'c++',
    'hbase', 'go', "java", 'c++'
]
word_counts = Counter(words)
frequency_num = 2
# 出现频率最高的 frequency_num 个单词
top_three = word_counts.most_common(frequency_num)
print(f'出现频率最高的{frequency_num}个单词是：{top_three}')

print(f"python出现频率：{word_counts['python']}")
print(f"go出现频率：{word_counts['go']}")

more_words = ['python','java','go']
for word in more_words:
    word_counts[word] += 1

print(f"python出现频率：{word_counts['python']}")
print(f"go出现频率：{word_counts['go']}")

more_words = ['python','java','python']
word_counts.update(more_words)
print(f"python出现频率：{word_counts['python']}")
print(f"go出现频率：{word_counts['go']}")

a_obj = Counter(words)
b_obj = Counter(more_words)
print(f'the object of a is:{a_obj}')
print(f'the object of b is:{b_obj}')

c_obj = a_obj + b_obj
print(f'the object of c is:{c_obj}')

d_obj = a_obj - b_obj
print(f'the object of d is:{d_obj}')
