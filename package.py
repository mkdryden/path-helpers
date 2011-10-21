import re
import tempfile
import tarfile

import jinja2

from path import path
from git_util import GitUtil


def get_version():
    g = GitUtil()
    return re.sub(r'-[^-]*$', '', g.describe())


class Packager(object):
    def __init__(self):
        self.version = get_version()
        self.tar = None
        self.temp_dir = None
        self.files = [path(p) for p in ['path.py', 'test_path.py', 'setup.py']]
        self.package_name = path('path.py-%s' % self.version)


    def package(self, build_dir):
        try:
            self.temp_dir = path(tempfile.mkdtemp(prefix='path_build'))
            print 'created temp dir: %s' % self.temp_dir
            self.build_dir = path(build_dir)
            self.build_dir.makedirs_p()

            for f in self.files:
                t = jinja2.Template(f.bytes())
                (self.temp_dir / f).write_bytes(
                    t.render(___VERSION___=self.version))

            tar_file = self.build_dir / path('%s.tar.gz' % self.package_name)
            self.tar = tarfile.open(tar_file, "w:gz")
            for f in self.files:
                self.tar.add(self.temp_dir / f, arcname=self.package_name / f)
        finally:
            self._clean_up()
        return tar_file


    def _clean_up(self):
        if self.tar:
            self.tar.close()
        if self.temp_dir:
            self.temp_dir.rmtree()


if __name__ == '__main__':
    build_dir = path('build')
    p = Packager()
    print 'built: %s' % p.package(build_dir)
