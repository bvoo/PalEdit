import unittest

from palworld_pal_edit.PalInfo import PalEntity, xpthresholds


class PalExperienceTests(unittest.TestCase):
    def make_pal(self, level=12, experience=1600):
        pal = PalEntity.__new__(PalEntity)
        pal._level = level
        pal._exp = experience
        pal._obj = {
            "Level": {"value": {"value": level}},
            "Exp": {"value": experience},
        }
        pal.CleanseAttacks = lambda: None
        return pal

    def test_experience_can_be_read_and_written(self):
        pal = self.make_pal()

        self.assertEqual(1600, pal.GetExp())

        pal.SetExp(1750)

        self.assertEqual(1750, pal.GetExp())
        self.assertEqual(1750, pal._obj["Exp"]["value"])

    def test_changing_level_updates_the_experience_value(self):
        pal = self.make_pal()

        pal.SetLevel(20)

        self.assertEqual(xpthresholds[19], pal.GetExp())
        self.assertEqual(xpthresholds[19], pal._obj["Exp"]["value"])

    def test_experience_is_kept_in_the_save_integer_range(self):
        pal = self.make_pal()

        pal.SetExp(-1)
        self.assertEqual(0, pal.GetExp())

        pal.SetExp(2_147_483_648)
        self.assertEqual(2_147_483_647, pal.GetExp())


if __name__ == "__main__":
    unittest.main()
