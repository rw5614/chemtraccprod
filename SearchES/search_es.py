import requests

url = "https://cbzl40i7le.execute-api.us-east-1.amazonaws.com/default/query-elasticsearch"


def search_es(q, cid):
	json_req = {
		"q": q,
		"cid": cid
	}
	r = requests.post(url, json=json_req)

	resp_json = [r["_source"] for r in r.json()]

	return resp_json


def possible_data_fields(results):
	data_fields = set().union(*(d.keys() for d in x))
	return data_fields


if __name__ == "__main__":
	x = search_es("sword", "1")
	print(x)
	data_fields = set().union(*(d.keys() for d in x))
	print(data_fields)
