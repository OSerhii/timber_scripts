import json
from requests import Request, Session


class Platforms:
    neb = "test-cbd3.neb.org.ua"


CREATE_TENDER_URL = "https://procedure-staging.prozorro.sale"
KEY = "9b09378f-0547-4069-8d6c-05aa82f84006"
TENDERS_COUNT = 50
PLATFORM_INSTANCE = Platforms.neb

s = Session()

def create_tender():
    with open("data/create_tender.json", 'r') as f_obj:
        jsn = f_obj.read()

    data = json.loads(jsn)

    headers = {
        "Authorization": KEY,
        "Content-Type": "application/json"
    }

    # r = Request('POST', "{}/api/procedures".format(CREATE_TENDER_URL), json=data, headers=headers)
    r = Request('POST', "{}/".format(CREATE_TENDER_URL), json=data, headers=headers)
    prepped = r.prepare()
    resp = s.send(prepped)
    return json.loads(resp.content)['id']


def retrieve_uaid(internal_id):
    #r = Request('GET', "{}/api/procedures/{}".format(CREATE_TENDER_URL, internal_id))
    r = Request('GET', "{}/{}".format(CREATE_TENDER_URL, internal_id))
    prepped = r.prepare()
    resp = s.send(prepped)
    ua_id = json.loads(resp.content)['auctionId']
    return ua_id


def create_platform_url(ua_id, platform):
    return "http://{}/participant/auction/bids/{}".format(platform, ua_id)


if __name__ == '__main__':
    tender_ids = list()
    for i in range(TENDERS_COUNT):
        internal_id = create_tender()
        ua_id = retrieve_uaid(internal_id)
        url = create_platform_url(ua_id, PLATFORM_INSTANCE)
        tender_ids.append(url)
    print(tender_ids)