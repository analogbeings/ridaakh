from setuptools import setup
from ridaakh.info import VERSION

setup(
        name="ridaakh",
        packages=[
            'ridaakh',
            'templates',
            'static',
            'DB',
            'app.py',
            ],
            version=VERSION,
            install_requires=[
            'gunicorn==19.9.0',
            'Jinja2==2.10',
            'requests-wsgi-adapter==.0.4',
            'parse==1.11.1',
            'pytest==4.2.1',
            'requests==2.21.0',
            'WebOb==1.8.5',
            'whitenoise==4.1.2',
            'sqlalchemy==1.3.3',
            'orator==0.9.8',
            'click==7.0',
            ],
        entry_points={
        'console_scripts':[
            'ridaakh= ridaakh.cli:main',
        ],

        },
            description="The Core package for ridaakh",
            author='zowhair',
            author_email='zowhair@gmail.com',
            url='https://github.com/ridaakhFramework/ridaakh',
            keywords=['ridaakh','python web framework', 'python3'],
            liscense='MIT',
            include_package_data=True,
        )
