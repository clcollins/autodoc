#!/usr/bin/env

# !DOC
# autodoc.py searches the current working
# directory, recursively, for files that
# contain comments between !DOC/COD! tags
# and includes the commends in a README.md
# file, so general documentation can be
# compiled from individual document's documentation
# !COD

import os
import re
import textwrap

def get_documentation(file):
    block = []
    with open(file) as input:
        for line in input:
            if line.strip() == '# !DOC':
                break
        for line in input:
            if line.strip() == '# !COD':
                break
            block.append(line)
    return block


def write_readme(readme, header, input):
    with open(readme, 'w') as readme:
        readme.write(textwrap.dedent(header + '\n'))
        for item in input:
            for filename, comments in item.iteritems():
                delimiter = '-' * len(filename)
                text = filename + '\n' + delimiter + '\n' + ''.join(comments) + '\n'

                readme.write(text)

    readme.closed


def readme_content(file):
    readme_input = {}

    content = get_documentation(file)

    relative_file=re.sub(cwd, '.', file)

    if content:
        readme_input[relative_file] = content
        return readme_input
    else:
        return None


def get_conf_value(val):
    'Replace this with an actual lookup from the conf file'

    ignores = ['.git', '.gitignore', '.svn']

    if val == "ignore":
        return ignores


def findfiles():
    readinglist = []
    for root, dirs, files in os.walk(cwd, topdown=True):
        ignores = get_conf_value('ignore')
        for ignore in ignores:
            if ignore in dirs:
                dirs.remove(ignore)
        for file in files:
            readinglist.append(os.path.join(root, file))

    return readinglist


def main():
    global cwd
    cwd = os.getcwd()
    readinglist = findfiles()
    readme = os.path.join(cwd, 'README.md')
    readme_input = []

    header = """
    PLACEHOLDER HEADER
    ==================

    This should be generated automatically somehow
    """

    for file in readinglist:
        item = readme_content(file)
        if item:
            readme_input.append(item)

    write_readme(readme, header, readme_input)


main()
