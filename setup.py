from setuptools import setup

setup(
        name = 'todo-and2797',
        version = '0.1.4',
        packages = ['todo'],
        entry_points = {
            'console_scripts': [
                'todo = todo.__main__:main'
                ]
            }
        )
