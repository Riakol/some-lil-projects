class LoginWithPassword:
    def __init__(self) -> None:
        self.site = 'https://hh.kz/?hhtmFrom=account_login'
        self.entrance = '/html/body/div[4]/div/div[2]/div/div/div/div/div[5]/a'
        self.log_btn = '/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/form/div[6]/button[1]'
        self.with_psswrd = '/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[2]/form/div[4]/button[2]'
        self.tel_field = '/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/form/div[1]/fieldset/input'
        self.pswrd_field = '/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/form/div[2]/fieldset/input'
        self.phone = 'phone number'
        self.password = 'password'