## notice

### require
python >= 3.8

### installation moduls
```shell
git clone https://github.com/shensg/packaging_notice.git
cd packaging_notice/dist
pip install notice-*-py3-none-any.whl
```

### used moduls


### 1. feishu notice
example
```python
from notice import fs_notice

image = "img_v3_025s_bdc4954d-e00b-4d4f-9b01-0d1eaf3d0ddg"
title = "test noitce"
content = "test notice example\nthis is test noitce\n you are welcome\n"
webhook = "" # feishu robot token

if __name__ == '__main__':
    fs_notice.fs_notice(image, title, content, webhook)
```

### 2. qiwei notice


### 3. dingding notice


### 关于封装pip包的例子
例如本项目，就是一个封装pip包的例子
[classifiers](https://pypi.org/classifiers/)
```
# 基础结构
packaging_notice/
├── src/
    └── notice/
        ├── __init__.py
        └── fs_notice.py


# 结构补充完整(需要手动补充其他的文件或者目录)
packaging_notice/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── notice/
│       ├── __init__.py
│       └── fs_notice.py
└── tests/

# 安装build
python3 -m pip install --upgrade build

# 切换工作目录，将项目打成pip包
cd packaging_notice
python3 -m build

# 打包后的结构，dist目录下就是打包后的产物，可以通过pip直接安装
packaging_notice/
├── LICENSE
├── dist/
│   └── notice-0.0.1.tar.gz
│   └── notice-0.0.1-py3-none-any.whl
├── pyproject.toml
├── README.md
├── src/
│   └── notice/
│       ├── __init__.py
│       └── fs_notice.py
└── tests/
```
