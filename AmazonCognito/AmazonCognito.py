import requests
import base64
from .decode import decode_token, verify_all_tokens


class AmazonCognito:

    def __init__(self, client_id, client_secret, url, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = url
        self.redirect_url = redirect_uri

    def check_logged_in(self, access_token):
        headers = {
            "Authorization": "Bearer " + access_token
        }
        r = requests.get(self.url + "/oauth2/userInfo", headers=headers)
        if r.status_code == 401:
            return False
        elif r.status_code == 200:
            return True
        else:
            print("BAD REQUEST")

    def get_user_info(self, access_token):
        headers = {
            "Authorization": "Bearer " + access_token
        }
        r = requests.get(self.url + "/oauth2/userInfo", headers=headers)
        return r.json()

    def client_id_and_secret_to_HTTP_auth(self):
        return base64.b64encode(bytes(self.client_id + ':' + self.client_secret, 'utf-8')).decode('utf-8')

    def refresh(self, refresh_token):
        headers = {
            "Content-Type": 'application/x-www-form-urlencoded',
            "Authorization": "Basic " + self.client_id_and_secret_to_HTTP_auth()
        }
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": refresh_token
        }

        r = requests.post(self.url + "/oauth2/token",
                          data=data, headers=headers)

        if r.status_code == 400:
            print("Refresh messed up")
            return None

        tokens = r.json()

        if verify_all_tokens(tokens) is False:
            # We could not verify all the tokens.
            return None
        else:
            return tokens

    def logout(self, logout_uri):
        params = {
            "client_id": self.client_id,
            "logout_uri": logout_uri
        }

        r = requests.get(self.url + "/logout", params=params)
        return r

    def get_auth_token(self, code):
        url = self.url + "/oauth2/token"
        headers = {
            "Content-Type": 'application/x-www-form-urlencoded',
            "Authorization": 'Basic ' + base64.b64encode(
                bytes(self.client_id + ':' + self.client_secret, 'utf-8')).decode(
                'utf-8')
        }
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "code": code,
            "redirect_uri": self.redirect_url
        }

        r = requests.post(url, data=data, headers=headers)

        tokens = r.json()
        print("tokens in Amazon Cognito:")
        print(tokens)

        if verify_all_tokens(tokens) is False:
            # We could not verify the tokens
            return None

        return r.json()


if __name__ == "__main__":
    myAmazonCognito = AmazonCognito("7m1prek8gppfutbgs11kukg8tg",
                                    "176k6jem77d561vgmcp8gnkadapm5vcoi1vt4c4ukdfnre2soioi",
                                    "https://labtracc.auth.us-east-1.amazoncognito.com",
                                    "http://localhost:5000/users/callback")
