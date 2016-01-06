# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tpa.theme2


class TpaTheme2Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tpa.theme2)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tpa.theme2:default')


TPA_THEME2_FIXTURE = TpaTheme2Layer()


TPA_THEME2_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TPA_THEME2_FIXTURE,),
    name='TpaTheme2Layer:IntegrationTesting'
)


TPA_THEME2_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TPA_THEME2_FIXTURE,),
    name='TpaTheme2Layer:FunctionalTesting'
)


TPA_THEME2_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TPA_THEME2_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TpaTheme2Layer:AcceptanceTesting'
)
