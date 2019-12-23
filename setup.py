from distutils.core import setup

setup(
    name='ConsoleMenu',
    packages=['consolemenu'],
    version='1.0.1',
    license='MIT',
    description='Simplest console menu you\'ve ever seen.\n'
                'Made on dicts, it allows you to easily implement a console menu '
                'without a number of classes like \'MenuItem\', etc.\n'
                'Just setup a dict, type a title and that\'s all.',
    author='Egor Almikeev',
    author_email='ealmikeew@gmail.com',
    url='https://github.com/EgorAlmikeev/ConsoleMenu',
    download_url='https://github.com/EgorAlmikeev/ConsoleMenu/archive/v_1.0.0.tar.gz',
    keywords=['CONSOLE', 'MENU', 'CONSOLEMENU'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
