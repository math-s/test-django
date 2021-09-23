from django.test import TestCase

class CheckoutTestCase(TestCase):
    def test_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)