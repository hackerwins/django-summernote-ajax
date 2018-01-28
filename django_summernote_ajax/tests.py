from django.test import TestCase


class DjangoSummernoteAjaxTest(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
