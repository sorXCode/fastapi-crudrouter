from setuptools import setup, find_packages

VERSION = '0.5.1'

setup(
    name='fastapi-crudrouter',
    version=VERSION,
    author='Adam Watkins',
    author_email='cadamrun@gmail.com',
    packages=find_packages(exclude=('tests.*', 'tests')),
    url='https://github.com/awtkns/fastapi-crudrouter',
    documentation='https://fastapi-crudrouter.awtkns.com/',
    license='MIT',
    description='A dynamic FastAPI router that automatically creates CRUD routes for your models',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=["fastapi"],
    python_requires='>=3.6',
    keywords=['fastapi', 'crud', 'restful', 'routing', 'generator', 'crudrouter'],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
    ]
)

