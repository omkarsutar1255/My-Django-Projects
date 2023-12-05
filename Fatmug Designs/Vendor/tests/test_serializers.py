from ..serializers import *
from ..models import *
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta


class UserSerializerTestCase(TestCase):
    def test_user_serializer_valid_data(self):
        username = "adityasutar"
        password = "aditya1234"
        email = "adityasutar@gmail.com"
        first_name = "Aditya"
        last_name = "Sutar"
        data = {
            'username':username,
            'password': password,
            'email':email,
            'first_name': first_name,
            'last_name': last_name
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_user_serializer_duplicate_username(self):
        username = "adityasutar"
        password = "aditya1234"
        email = "adityasutar@gmail.com"
        first_name = "Aditya"
        last_name = "Sutar"
        User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        data = {
            'username':username,
            'password': "omkar1234",
            'email':"omkarsutar123@gmail.com",
            'first_name': "Omkar",
            'last_name': "Sutar"
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['username'][0], 'A user with that username already exists.')

    def test_user_serializer_create(self):
        data = {
            'username':"omkarsutar",
            'password': "omkar1234",
            'email':"omkarsutar123@gmail.com",
            'first_name': "Omkar",
            'last_name': "Sutar"
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.create(serializer.validated_data)
        self.assertEqual(user.username, "omkarsutar")
        self.assertEqual(user.email, "omkarsutar123@gmail.com")
        self.assertEqual(user.first_name, "Omkar")
        self.assertEqual(user.last_name, "Sutar")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.check_password("omkar1234"))

    def test_user_serializer_update(self):
        username = "omkarsutar"
        password = "aditya1234"
        email = "adityasutar@gmail.com"
        first_name = "Omkar"
        last_name = "Sutar"
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        data = {
            'first_name': 'Aditya',
            'last_name':'Patil'
        }

        serializer = UserSerializer(instance=user, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.update(user, serializer.validated_data)
        self.assertEqual(updated_user.first_name, 'Aditya')
        self.assertEqual(updated_user.last_name, 'Patil')


class LoginSerializerTests(TestCase):
    def setUp(self):
        username = "adityasutar"
        password = "aditya1234"
        email = "adityasutar@gmail.com"
        first_name = "Aditya"
        last_name = "Sutar"
        self.user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

    def test_login_serializer_valid_data(self):
        data = {'username': "adityasutar", 'password': "aditya1234"}
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['username'], "adityasutar")

    def test_login_serializer_invalid_data(self):
        data = {'name': "adityasutar", 'password': "sutar123"}
        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('This field is required.', serializer.errors['username'])


class VendorSerializerTests(TestCase):
    def setUp(self):
        username = "adityasutar"
        password = "aditya1234"
        email = "adityasutar@gmail.com"
        first_name = "Aditya"
        last_name = "Sutar"
        self.user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

    def test_vendor_serializer(self):
        data = {
            'name': 'Microsoft',
            'contact_details': 9013434545,
            'address': "Cleveland, USA",
            'vendor_code': "MI68",
            'created_by': self.user.id
        }

        serializer = VendorSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        vendor = serializer.save()
        self.assertEqual(vendor.name, 'Microsoft')
        self.assertEqual(vendor.contact_details, 9013434545)
        self.assertEqual(vendor.address, "Cleveland, USA")
        self.assertEqual(vendor.vendor_code, "MI68")


class PerformanceSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adityasutar', password='aditya@1234')
        self.vendor = Vendor.objects.create(
            name='Microsoft',
            contact_details=90134345,
            address="Cleveland, USA",
            vendor_code="MI68",
            created_by=self.user
        )

    def test_performance_serializer(self):
        data = {'vendor': self.vendor.id}
        serializer = PerformanceSerializer(data=data)
        self.assertTrue(serializer.is_valid())


class PurchaseOrderSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adityasutar', password='aditya@1234')
        self.vendor = Vendor.objects.create(
            name='Microsoft',
            contact_details=90134345,
            address="Cleveland, USA",
            vendor_code="MI68",
            created_by=self.user
        )

    def test_purchase_order_serializer(self):
        data = {
            "vendor": self.vendor.id,
            'delivery_date': datetime.now() + timedelta(days=7),
            'items': {'Laptop': 5},
            'quantity': 10,
            'created_by': self.user.id
        }

        serializer = PurchaseOrderSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        purchase_order = serializer.save()
        self.assertIsNotNone(purchase_order.po_number)
        self.assertEqual(purchase_order.vendor, self.vendor)
        self.assertEqual(purchase_order.status, 'Pending')
        self.assertEqual(purchase_order.created_by, self.user)
