import jieba
import sys

if __name__ == '__main__':
    for l in sys.stdin:
        words = jieba.cut(l.strip())
        sys.stdout.write((u' '.join(words) + u'\n'))
