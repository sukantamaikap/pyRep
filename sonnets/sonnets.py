import time

# find the word from Shakespeare sonnet that are not present in modern dictionary
sonnet_words = [line.strip() for line in open("sonnet_words.txt", "r").readlines()]
modern_words = [line.strip() for line in open("sowpods.txt", "r").readlines()]
modern_words_set = set(modern_words)

count = 0

start = time.time()
for word in sonnet_words:
    # time comparison code
    #if word not in modern_words
    if word not in modern_words_set:
        print(word)
        count += 1
stop = time.time()

print("Total not found word count : %d", count)
print("Time elapsed : %.1f seconds" %(stop - start))