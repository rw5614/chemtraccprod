import jwt
import json
import cryptography

# import jwt
# from jwt.algorithms import RSAAlgorithm
# IDjwt = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoSjZYWnF2cWVuVjVIay1qWnV5TUN5bGNPT3FnTzNpWlYtMnVBRTVhMDYwIn0.eyJqdGkiOiI3M2Y0NDk2NC03M2UxLTRmZTgtYmRlZi1mNGJiY2FkNDQ5NjUiLCJleHAiOjE1MzY2MjY2NzksIm5iZiI6MCwiaWF0IjoxNTM2NjI2MDc5LCJpc3MiOiJodHRwczovL3NpZ25pbi5kZW1vLm1hZGNvcmUuY2xvdWQvYXV0aC9yZWFsbXMvbWFzdGVyIiwiYXVkIjoibG9jYWxob3N0Iiwic3ViIjoiMjUzNDk1ZmUtZGY2MC00NDE5LWExMzQtZWZhZTFiMGE5OWQwIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoibG9jYWxob3N0IiwiYXV0aF90aW1lIjowLCJzZXNzaW9uX3N0YXRlIjoiMWZmYTgzZGItZDg3MS00YjQzLTk5YjgtOTMzNDQxNTg1OTExIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJQZXRlciBTdHlrIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicG9sZmlsbSIsImdpdmVuX25hbWUiOiJQZXRlciIsImZhbWlseV9uYW1lIjoiU3R5ayIsImVtYWlsIjoicG9sZmlsbUBnbWFpbC5jb20ifQ.gaYPTNBLVYQJTRU5UHJ3GpVNKOrpekBIHmso6ZWLvaUJu4lgXf5wY1fdCqtsubTl2IlCy-zL81LABqua3He1M8qdAFvhKiTqyjm5SvzT40sjIDEnzCfUjYTvJIor8gcVscyNlqAuph0LNJb-aGu_tkaXjjLBl0DXqbyVyUtQ80ai9-ReCsmLobVLWeoyfi7hu9-elP6pOxaueIh5kT-MIux63xvvhSXBwQTxN9Dv7mNfSd1MCUUGtUJE1Fsb8dnIzpGjQh23Mw3p7SLq_ox_IhFP_mzRh3H8ye0gwVjILOOFUrCvFcylBS6TGhCZtkZP6luqRFbkCM9flQjQkON6lw'
# key_json = '{"kid":"hJ6XZqvqenV5Hk-jZuyMCylcOOqgO3iZV-2uAE5a060","kty":"RSA","alg":"RS256","use":"sig","n":"q33wpseciIME_pakwslqucEAC6f_T9lN1OYaNhFN3cs_50KhWuPu8918JZFECvtby835CIyIEngKWLFr-VPbe5GW94dujvlaZJOj0eGst3t2gd6TOeu5FwzsAJWHNP725fu5SwGlN2J81fmYSYAWG1QNK3Bu5Fn5KD0gCN1MRD8gjC-hXHte904fdwRxZdLfQinaEyW1xwlItsJ1U9_Ve6hZbE4HMZeyeGPrJna__xWbNi9xCize32L-pepyeXWGmcTgq7--p9bXu6xtm_8Pmt5KkuLS-sE1Lrj19sZffjeJoy5q6tTXr8CAJT5qU-P9km4WAdKkb-2IlWMmGtHyQw","e":"AQAB"}'
# public_key = RSAAlgorithm.from_jwk(key_json)
# decoded = jwt.decode(IDjwt, public_key, algorithms='RS256')


jwks = {
	"keys": [
		{
			"alg": "RS256",
			"e": "AQAB",
			"kid": "8hbia+i5o8l6avCymREJ+9gCquwW/3t/zhNYMuxfecA=",
			"kty": "RSA",
			"n": "kdybrEQ5uYeY9UZ2Av08f-_PQSlXTQdazYAr8ZRVSv9boXPrH9gP3oh3uXLeToSK5ot30ojrLryKlx3M1J5uoI5HN7GM0Lg7nB9ZTsGkpkI1B3Gcyq1FfUzN2r9L2pkquGkFHqX8gQG9Angl6HYlydByj98L3XfdqYAZi1fqqsrHpmOnxPKZB26pygHnzfKNaTLhFyiRh8PRh7BtRzB2ps0WA_xRayxotfkXDJfOBkD4qvB4RV6PqHLUW8lNpUm6JA0YYD71FydlYjqNk0I00czOgADB-pR8tYJlRAKAe-TUaQ9Y8qz0Dq4LIHVvFx3TK1nUP8ZWxmCl5GGE5wK6Nw",
			"use": "sig"
		},
		{
			"alg": "RS256",
			"e": "AQAB",
			"kid": "co2F6GkMtaXxn5shjUSypjxjRjI6Hop7IS5GqK06Oq8=",
			"kty": "RSA",
			"n": "hyq8dIkeWZXVi7SgQNyHdwtYbPFe-9HeQxreON_ga1F0g_m2-51lpaKGgz5QUJBgNpdfgs3mdPDRwrsZvFoL1LmVIhobip9zP3E5VNPIA5JKR7JUSeZGudrepo6tLOBqJtX-02nDot1mJB3zmQ5kLl0CUV2JL3zyxz9vutTSCVuQPbjWkoPXCmU26gM3-baexOwyjJRAnWJYHCm6XkRuIA2vJKAEBMJfa34CRgQD_Hl6ztZ7YVrkm1lIl-jzVZx4RL4EyJVgeTt9wcONX2uVjykiA6ugOMvOd9pmrCFcxSeZwoxCZrJmHriNyt4RzsifV7yVCaK6fKJQYQQqf3SCuQ",
			"use": "sig"
		}
	]
}

audience_id = '7m1prek8gppfutbgs11kukg8tg'

# def decode_token(token, jwks=jwks):
# 	public_keys = {}
# 	pk = []
# 	for jwk in jwks['keys']:
# 		kid = jwk['kid']
# 		public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
# 		pk.append(public_keys[kid])
#
# 	def pad_token(token):
# 		while len(token) % 4 != 0:
# 			token += '='
# 		print(len(token))
# 		return token
# 		# fullpiece = ''
# 		# Counter = 0
# 		# for subpiece in token.split('.'):
# 		# 	while len(subpiece) % 3 != 0:
# 		# 		subpiece += '='
# 		# 	if Counter == 2:
# 		# 		fullpiece += subpiece
# 		# 	else:
# 		# 		fullpiece += subpiece + '.'
# 		# 	Counter += 1
# 		#
# 		# # while len(token) % 3 != 0:
# 		# # 	token += '='
# 		# # token += (4 - len(token) % 4) * "="
# 		# return fullpiece
#
# 	token = pad_token(token)
# 	try:
# 		payload = jwt.decode(token, key=pk[0], algorithms=['RS256'], options={'verify_aud': False})
# 		print(payload)
# 		return payload
# 	except:
# 		payload = jwt.decode(token, key=pk[1], algorithms=['RS256'], options={'verify_aud': False})
# 		print(payload)
# 		return payload
# 	# print(token)
# 	#
# 	# kid = jwt.get_unverified_header(token)['kid']
# 	#
# 	# key = public_keys[kid]
# 	#
# 	# # https://pyjwt.readthedocs.io/en/latest/search.html?q=error&check_keywords=yes&area=default
# 	# try:
# 	# 	print(token)
# 	# 	print(kid)
# 	# 	payload = jwt.decode(token, key=key, algorithms=['RS256'], options={'verify_aud': False})
# 	# 	return payload
# 	# except jwt.exceptions.ExpiredSignatureError:
# 	# 	# It's expired
# 	# 	return None
# 	# except Exception as e:
# 	# 	# There's some other error
# 	# 	print(token)
# 	# 	print(e)
# 	# 	return None
#
#

def decode_token(token, jwks=jwks):
	public_keys = {}
	for jwk in jwks['keys']:
		kid = jwk['kid']
		public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

	def pad_token(token):
		token += (len(token) % 4) * "="
		return token

	token = pad_token(token)

	kid = jwt.get_unverified_header(token)['kid']
	key = public_keys[kid]

	# https://pyjwt.readthedocs.io/en/latest/search.html?q=error&check_keywords=yes&area=default
	try:
		payload = jwt.decode(token, key=key, algorithms=['RS256'], options={'verify_aud': False})
		return payload
	except jwt.exceptions.ExpiredSignatureError:
		# It's expired
		return None
	except Exception as e:
		# There's some other error
		print(e)
		return None

def verify_all_tokens(tokens):
	# DO NOT VERIFY THE REFRESH_TOKEN BECAUSE IT IS NOT A JWT!
	# Much pain was brought about by this token.
	for token_type in ['access_token', 'id_token']:
		if token_type not in tokens:
			return False
		if decode_token(tokens[token_type]) is None:
			return False
	return True
