# -*- coding: utf-8 -*-
# author = "chaichai"


"""
实现DNS查找缓存
思路：使用trie树，存储IP地址与对应域名
"""


class TrieNode:
    def __init__(self):
        C = 11
        self.is_leaf = False
        self.url = None
        self.child = [None] * C
        i = 0
        while i < C:
            self.child[i] = None
            i += 1


def get_index_from_char(c):
    return 10 if c == '.' else (ord(c) - ord('0'))


# def get_char_from_index(i):
#     return '.' if i == 10 else ('0' + str(i))


class DNS:
    def __init__(self):
        self.c = 11
        self.root = TrieNode()

    def insert(self, ip, url):
        lens = len(ip)
        p = self.root
        level = 0
        while level < lens:
            index = get_index_from_char(ip[level])
            if p.child[index] is None:
                p.child[index] = TrieNode()
            p = p.child[index]
            level += 1
        p.is_leaf = True
        p.url = url


    def search(self, ip):
        p = self.root
        l = len(ip)
        level = 0
        while level < l:
            index = get_index_from_char(ip[level])
            if p.child[index] == None:
                return None
            p = p.child[index]
            level += 1
        if p is not None and p.is_leaf:
            return p.url
        return None


if __name__ == '__main__':
    ip = ['10.57.11.127', '121.57.61.129', '66.125.100.103']
    url = ['www.samsung.com', 'www.samsung.net', 'www.google.com']
    n = len(ip)
    cache = DNS()
    for i in range(n):
        cache.insert(ip[i], url[i])
        i += 1
    dst = '121.57.61.129'
    res_url = cache.search(dst)
    if res_url is not None:
        print("对应域名为：", res_url)
    else:
        print("无匹配域名")