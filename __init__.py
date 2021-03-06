# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WorkflowTest
                                 A QGIS plugin
 test for figuring out my workflow
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-03-30
        copyright            : (C) 2018 by Phil Ribbens
        email                : philip.ribbens@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Phil Ribbens'
__date__ = '2018-03-30'
__copyright__ = '(C) 2018 by Phil Ribbens'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WorkflowTest class from file WorkflowTest.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .workflow_test import WorkflowTestPlugin
    return WorkflowTestPlugin()
