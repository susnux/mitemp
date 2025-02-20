"""End to End test cases for MiTemp."""
import unittest
import pytest
from btlewrap.gatttool import GatttoolBackend
from btlewrap.bluepy import BluepyBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY


class TestEverythingGatt(unittest.TestCase):
    """End to End test cases for MiTemp."""

    # pylint does not understand pytest fixtures, so we have to disable the warning
    # pylint: disable=no-member

    def setUp(self):
        """Set up the test environment."""
        self.backend_type = GatttoolBackend

    @pytest.mark.usefixtures("mac")
    def test_everything(self):
        """Test reading data from a sensor

        This check if we can successfully get some data from a real sensor. This test requires bluetooth hardware and a
        real sensor close by.
        """
        assert hasattr(self, "mac")
        poller = MiTempBtPoller(self.mac, self.backend_type)
        self.assertIsNotNone(poller.firmware_version())
        self.assertIsNotNone(poller.name())
        self.assertIsNotNone(poller.parameter_value(MI_TEMPERATURE))
        self.assertIsNotNone(poller.parameter_value(MI_HUMIDITY))
        self.assertIsNotNone(poller.parameter_value(MI_BATTERY))


class TestEverythingBluepy(TestEverythingGatt):
    """Run the same tests as in the gatttool test"""

    def setUp(self):
        """Set up the test environment."""
        self.backend_type = BluepyBackend
