# ----------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# ----------------------------------------------------------------------

__author__ = 'Aymeric Rateau (aymeric.rateau@gmail.com)'
__copyright__ = 'Copyright (c) 2015 Aymeric Rateau'
__license__ = 'GPLV3'
__version__ = "0.1.9.1"

#if it's run as a script or imported within python, this happens
if __name__ == 'mdfreader':
    from .mdfreader import mdf,mdfinfo
