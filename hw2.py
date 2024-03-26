word_count = {}

with open("hw2_data.txt", "r") as file:
      for line in file:
        words = line.strip().split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

total_words = len(word_count)

print("總共有 {} 個不重複的英文字".format(total_words))

for word, count in word_count.items():
    print("英文字'{}' 出現次數為{}次".format(word, count))
