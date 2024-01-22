from setuptools import setup, find_packages

setup(
    name='asin2jan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-amazon-paapi',
        # 他の依存関係があれば追加
    ],
)