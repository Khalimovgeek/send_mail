from setuptools import setup, find_packages

setup(
    name='mail',
    version='1.0.0',
    packages=find_packages(),
    py_modules=['mail_script'],
    install_requires=[
        'google-api-python-client',
        # Add other dependencies here, if any
    ],
    entry_points={
        'console_scripts': [
            'mail=mail_script:main',  # This maps the command `mail` to the `main` function
        ],
    },
)
