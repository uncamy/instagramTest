from instagram.client import InstagramAPI
import sys

client_id = raw_input("Client ID: ").strip()
client_secret = raw_input("Client Secret: ").strip()
redirect_uri = raw_input("Redirect URI: ").strip()
raw_scope = raw_scope.split(' ')

if not scope or scope == [""]:
    scope = ["basic"]

api = InstagramAPI(client_id=client_id, client_secret=client_secret, recirect_uri=redirect_uri)
redirect_uri = api.get_authorize_login_url(scope =scope)
