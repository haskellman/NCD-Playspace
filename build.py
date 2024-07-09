#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

# These are the plugins we want to use in our project.
# Projects provide tasks which are blocks of logic executed by PyBuilder.

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a linter plugin that runs flake8 (pyflakes + pep8) on our project sources
use_plugin("python.flake8")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")

name = "ncd_playspace"
default_task = "publish"



@init
def set_properties(project):
    project.set_property("coverage_break_build", False) # default is True
    project.build_depends_on("mock")

