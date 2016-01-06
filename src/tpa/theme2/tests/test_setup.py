# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tpa.theme2.testing import TPA_THEME2_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that tpa.theme2 is properly installed."""

    layer = TPA_THEME2_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tpa.theme2 is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('tpa.theme2'))

    def test_browserlayer(self):
        """Test that ITpaTheme2Layer is registered."""
        from tpa.theme2.interfaces import ITpaTheme2Layer
        from plone.browserlayer import utils
        self.assertIn(ITpaTheme2Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TPA_THEME2_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tpa.theme2'])

    def test_product_uninstalled(self):
        """Test if tpa.theme2 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('tpa.theme2'))

    def test_browserlayer_removed(self):
        """Test that ITpaTheme2Layer is removed."""
        from tpa.theme2.interfaces import ITpaTheme2Layer
        from plone.browserlayer import utils
        self.assertNotIn(ITpaTheme2Layer, utils.registered_layers())
