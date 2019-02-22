from rest_framework import serializers
from loan.models import Loan, Profile


class LoanSerializer(serializers.ModelSerializer):
    # profile = serializers.StringRelatedField(many=False)
    # profile_object = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Loan
        fields = ('id', "purpose", "amount_requested")

    def get_profile(self, loan):
        profile = Profile.objects.filter(self.profile_id)
        return ProfileSerializer(profile, many=True, context=self.context).data


class ProfileSerializer(serializers.ModelSerializer):

    loans = LoanSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ("membership_number", "first_name",
                  'last_name', 'id_number', 'loans')
