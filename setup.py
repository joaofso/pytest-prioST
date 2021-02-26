from setuptools import setup


with open('README.md') as f:
    readme = f.read()


setup(
     name="pytest-prioST",
     version='0.0.1',
     description='A pytest plugin that uses a set of criteria to prioritize test cases after the collection phase',
     long_description=readme,
     license='APACHE',
     author='Joao Felipe Ouriques',
     author_email='joaofso@gmail.com',
     url='https://github.com/joaofso/pytest-prioST',
     platforms=['macos', 'linux'],
     packages=['priost'],
     entry_points={'pytest11': ['priost.plugin']},
     zip_safe=False,
     install_requires=['pytest>=2.4.2'],
     classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
     ]
)
