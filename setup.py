from setuptools import setup

setup(
    name='resume_app',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'flask',
        'waitress',
    ],
    entry_points='''
        [console_scripts]
        resume-server=app:app
    ''',
)
