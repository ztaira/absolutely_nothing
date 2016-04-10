from distutils.core import setup
setup(
    name = 'absolutely_nothing',
    packages = ['absolutely_nothing'], # this must be the same as the name above
    version = '0.1',
    description = 'Does Absolutely Nothing better than anything else',
    author = 'Zachary Taira',
    author_email = 'zach.taira@gmail.com',
    url = 'https://github.com/ztaira14/absolutely_nothing', # use the URL to the github repo
    # use git tag {version} -m "description of tag"
    # use git push --tags origin master to update tags on github
    # Github creates tarballs for download at 
    # https://github.com/{username}/{module_name}/tarball/{tag}
    download_url = 'https://github.com/ztaira14/absolutely_nothing/tarball/0.1',
    keywords = ['absolutely', 'nothing', 'python'], # arbitrary keywords
    classifiers = [],
)
