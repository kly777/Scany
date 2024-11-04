from Search import get_g_url, get_b_url, get_d_url, get_ba_url, get_y_url, get_s_url
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
q = 'vue ui library'

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(func, q) for func in [
        get_b_url, get_d_url, get_g_url, get_y_url, get_ba_url, get_s_url]]
    all_urls = sum((future.result() for future in futures), [])
print("collected")
url_counter = Counter(all_urls)

# 将结果根据出现次数排序
sorted_urls = sorted(url_counter.items(),key=lambda item: item[1], reverse=True)
print("已排序")
# 写入文件
web_count = 0

with open('sorted_urls.txt', 'w', encoding="utf-8") as file:
    for url, count in sorted_urls:
        file.write(f"{url}: {count}\n")
        web_count += count

print("已输出到文件sorted_urls.txt")
print("共爬取到", web_count, "条结果")
