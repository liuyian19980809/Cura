# Cura is released under the terms of the AGPLv3 or higher.

from . import UpgradeFirmwareMachineAction

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
    }

def register(app):
    return { "machine_action": [
        UpgradeFirmwareMachineAction.UpgradeFirmwareMachineAction(),
    ]}
