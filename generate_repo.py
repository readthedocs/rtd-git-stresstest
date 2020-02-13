"""
Generates lots of git commits by modifying the file docs/updates.rst
"""
import os
import subprocess
from datetime import datetime


GIT_AUTHORSHIP = "David Fischer <david@readthedocs.org>"
UPDATES_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs/updates.rst")
NUM_COMMITS_AND_TAGS = 10000


def create_commit(message):
    subprocess.check_output(['git', 'add', UPDATES_FILE_PATH])

    authorship = f'--author="{GIT_AUTHORSHIP}"'
    subprocess.check_output(['git', 'commit', '-m', message, authorship])


def create_tag(tag_name):
    tag_name = tag_name.replace(' ', '-')
    tag_name = tag_name.replace(':', '-')
    subprocess.check_call(['git', 'tag', tag_name])


def push_tags():
    """
    Helps push tags to GitHub

    GitHub limits how many tags can be pushed at a time.
    """
    tags_output = subprocess.check_output(['git', 'tag'])
    tags = tags_output.split()
    tags.reverse()

    groupsize = 100

    for index in range(0, len(tags), groupsize):
        # Group tags 100 at a time
        tag_group = tags[index:index + groupsize]
        subprocess.check_call(['git', 'push', 'origin'] + tag_group)


def main():
    for _ in range(NUM_COMMITS_AND_TAGS):
        date_str = str(datetime.now())
        with open(UPDATES_FILE_PATH, "a") as fd:
            output = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
            shahex = output.decode('utf-8').strip()

            added_line = f"* Previous commit - {shahex}\n"

            fd.write(added_line)

        create_commit(f"Generating commit from previous: {shahex}")
        create_tag(f"tag-{date_str}")


if __name__ == '__main__':
    main()
