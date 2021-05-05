import subprocess
import sys

import sort


def process():
    subprocess.run([sys.executable, "-c", "print('ocean')"])


if __name__ == '__main__':
    process()
