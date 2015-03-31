import http
import datetime
import util
import oauth_base

class Error(Exception):
	"""Exceptions"""

def login():
	oauth_base.delete_file()
	refresh_token()

def refresh_token(auth):
	content = http.req_json('GET', 
		'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token', 
		headers = { 'Metadata-Flavor': 'Google' })
	now = int(datetime.datetime.now().strftime("%s"))
	expires_in = content['expires_in']
	content['created'] = now
	content['expires'] = now + expires_in
	content['handler'] = 'gce'
	oauth_base.write_file(content)

def __main():
	return login()

if __name__ == '__main__':
	__main()