class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'company_name', 'linemail_addressenos', 'country', 'code','phone_number','password']