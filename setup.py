# from setuptools import setup, find_packages

# setup(
#     name='excel_library',  # Library ka naam
#     version='0.1',  # Version number
#     packages=find_packages(),  # Automatically packages ko dhoondta hai
#     description='A simple library for Excel operations',  # Short description
#     url='https://github.com/mohitbisht-tech/excel_library',  # GitHub repository URL
#     author='Mohit Bisht',  # Tumhara naam
#     author_email='m2079b@gmail.com',  # Tumhara email
#     install_requires=[],  # Dependencies agar koi hai to add karo
# )


from setuptools import setup, find_packages

setup(
    name='excel_library',               # Package ka naam
    version='0.1',                 # Package version
    author='Mohit Bisht',              # Tumhara naam
    author_email='m2079b@gmail.com',  # Tumhara email
    description='A simple library for Excel operations',  # Package ka description
    long_description=open('README.md').read(),  # README file se description
    long_description_content_type='text/markdown',
    url='https://github.com/mohitbisht-tech/excel_library',  # GitHub repo URL
    packages=find_packages(),        # Packages ko automatically find karega
    classifiers=[                    # Package classification
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',        # Python version requirement
)
