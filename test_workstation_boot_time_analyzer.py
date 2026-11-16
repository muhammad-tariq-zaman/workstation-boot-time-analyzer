import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyse

def row(workstation, boot_date, seconds):
    return {"workstation": workstation, "boot_date": boot_date,
            "boot_seconds": str(seconds)}

class TestBootTimeAnalyzer(unittest.TestCase):
    def test_slow_flagged(self):
        self.assertEqual(analyse([row("WS-1", "2026-11-10", 210)])[0][3], "SLOW")

    def test_ok_under_limit(self):
        self.assertEqual(analyse([row("WS-1", "2026-11-10", 95)])[0][3], "OK")

    def test_exactly_at_limit_is_ok(self):
        self.assertEqual(analyse([row("WS-1", "2026-11-10", 120)])[0][3], "OK")

    def test_custom_threshold(self):
        r = analyse([row("WS-1", "2026-11-10", 95)], slow_seconds=60)
        self.assertEqual(r[0][3], "SLOW")

    def test_slowest_first(self):
        r = analyse([row("WS-1", "2026-11-10", 45), row("WS-2", "2026-11-10", 210)])
        self.assertEqual(r[0][0], "WS-2")

    def test_seconds_kept(self):
        self.assertEqual(analyse([row("WS-1", "2026-11-10", 45)])[0][2], 45)

    def test_boot_date_kept(self):
        self.assertEqual(analyse([row("WS-1", "2026-11-10", 45)])[0][1], "2026-11-10")

    def test_empty_input(self):
        self.assertEqual(analyse([]), [])
