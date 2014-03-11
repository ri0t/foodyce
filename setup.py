#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Gnu Public License v3
# =====================
# Copyright (C) 2014 riot <riot@c-base.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
import os

setup(name = "foodyce",
      version = "1.0.0",
      description = "foodyce",

      author = "Heiko 'riot' Weinen",
      author_email = "riot@c-base.org",
      url = "https://github.com/ri0t/foodyce",
      license ="Gnu Public License v3",
      packages = [
      ],
      package_dir = [
      ],
      scripts = [
                  'foodyce',
                ],
      data_files=[
                 ],

      long_description = """
Weatherscraper grabs some relevant data from the web and assembles a well designed HTML5 page to render the
current weather situation for a given area on web clients.
""",
      dependency_links = [
      ],
      # These versions are not strictly checked, older ones may or may not work.
      install_requires = [
      ]

)
