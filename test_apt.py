import unittest

from myApt import PackageManager

class TestPackageManager(unittest.TestCase):

    def test_manage_dependency(self):
        apt = PackageManager()
        apt.manage_depenencies("PK1", ["PK2","PK3","PK4",])
        self.assertEqual({"PK1": {"PK2","PK3","PK4",}}, apt.downwards_dependencies)
        self.assertEqual({"PK2": {"PK1"}, "PK3": {"PK1"}, "PK4": {"PK1"} }, apt.upwards_dependencies)

    def test_install_package(self):
        apt = PackageManager()
        apt.manage_depenencies("PK1", ["PK2","PK3","PK4",])
        apt.manage_depenencies("PK2", ["PK5"])
        apt.manage_depenencies("PK6", ["PK7"])
        apt.install("PK1",True)
        self.assertEqual({"PK1","PK2","PK3","PK4", "PK5"}, apt.installed)
        self.assertEqual({"PK1"}, apt.manually_installed)
    
    def test_remove_package(self):
        apt = PackageManager()
        apt.manage_depenencies("PK1", ["PK2","PK3","PK4",])
        apt.manage_depenencies("PK2", ["PK5"])
        apt.manage_depenencies("PK6", ["PK7"])
        apt.install("PK1",True)
        apt.install("PK6",True)
        apt.remove("PK1", False)
        self.assertEqual({"PK6","PK7"}, apt.installed)
        self.assertEqual(1, len(apt.manually_installed))