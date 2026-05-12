import os

# 定义哪些是核心文件
CORE_FILES = ['_config.yml', '_posts', '_data', 'index.md']

def scan_blog():
    print("--- 🔍 博客文件体检报告 ---")
    files = os.listdir('.')
    
    for f in files:
        if f in CORE_FILES:
            print(f"【核心】{f} - 请务必保留")
        elif f.endswith('.py'):
            print(f"【脚本】{f} - 这是你写的 Python 工具")
        elif f in ['test.md', 'debug.md']:
            print(f"【杂物】{f} - 建议完成后删除")
        else:
            print(f"【普通】{f}")

if __name__ == "__main__":
    scan_blog()