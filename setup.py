from setuptools import setup

setup(
        name = 'todo-and2797',
        version = '0.1.3',
        packages = ['todo-list'],
        entry_points = {
            'console_scripts': [
                'todo = todo-list.__main__:main'
                ]
            }
        )
