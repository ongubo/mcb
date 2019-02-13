from django.test import TestCase
from django.contrib.auth.models import User
from .models import Loan, Profile


class TestUser(TestCase):
    def test_user_creation__ok(self):
        # check if a user is created in the database
        user = User(username="test_user", password="password")
        user.save()

        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_loan_creation__ok(self):
        # Check if a created loan belongs to a  user
        user = User(username="test_user_loan", password="password")
        user.save()

        # Create a profile for the user
        profile = Profile(
            membership_number="P001",
            first_name="testfirstname",
            last_name="testlastname",
            middle_name="testmiddlename",
            id_number="12345678",
            dob="12/12/1998",
            home_address="001 Nairobi",
            office_phone="0712333333",
            mobile_phone="0712333333",
            pin_number="00000000",
            email="user@email.com",
            user=user,
        )
        profile.save()

        # attach the loan to a profile
        loan = Loan(
            purpose=2,
            amount_requested=30000,
            profile=user
        )
        loan.save()

        user_count = User.objects.all().count()
        self.assertEqual(loan.profile.user.id, user.id)

    def test_loads_home_page_ok(self):
        # Issue a GET request.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_logout_ok(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_delete_loans_ok(self):
        initial_loan_count = Loan.objects.all().count()
        Loan.objects.all()[:1].delete()
        latter_loan_count = Loan.objects.all().count()

        self.assertEqual(initial_loan_count-latter_loan_count, 1)

    def test_delete_users_ok(self):
        initial_user_count = User.objects.all().count()
        User.objects.all()[:1].delete()
        latter_user_count = User.objects.all().count()

        self.assertEqual(initial_user_count-latter_user_count, 1)
