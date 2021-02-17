from setuptools import setup

setup(
        name = 'todo-and2797',
        version = '0.1.0',
        packages = ['todo-list'],
        entry_points = {
            'console_scripts': [
                'todo = todo.__main__:main'
                ]
            }
        )
