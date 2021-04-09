from distutils.core import setup
from setuptools import setup
setup(
	name = 'aparat_dl',        
	packages = ['Scripts'],  
	version = '8',  
	license='MIT',     
	description = 'a handy tools to download from aparat ',   
	author = 'mehdi',                  
	author_email = 'gudarzi.gi@gmail.com',     
	url = 'https://github.com/thisismehdi/aparat-dl',  
	download_url = 'https://github.com/thisismehdi/aparat-dl/archive/v8.tar.gz',  
	keywords = ['aparat_dl', 'aparat-dl', 'aparat'],  
	install_requires=[  

	      'beautifulsoup4',
	      'certifi',
	      'chardet',
	      'idna',
	      'requests',
	      'soupsieve',
	      'urllib3',
	      'youtube-dl',
	  ],
	classifiers=[
	"Programming Language :: Python :: 3.6",
	'Development Status :: 5 - Production/Stable',
	"Operating System :: OS Independent",
	'License :: OSI Approved :: MIT License',  

	],
	entry_points={

		'console_scripts': [
	    'aparat_dl = Scripts.aparat_dl:main',
	],
	},



)