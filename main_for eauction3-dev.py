import json
from requests import Request, Session


class Platforms:
    dev = "eauction3-dev.byustudio.in.ua"


CREATE_TENDER_URL = "https://procedure-staging.prozorro.sale"
KEY = "9fa74b0e-e692-4746-b38b-8a4387097a53"
TENDERS_COUNT = 10
PLATFORM_INSTANCE = Platforms.dev

s = Session()


def create_tender():
    with open("create_tender.json", 'r', encoding='utf-8') as f_obj:
        jsn = f_obj.read()

    data = json.loads(jsn)
    headers = {
        "Authorization": KEY,
        "Content-Type": "application/json"
    }


    r = Request('POST', "{}/api/procedures".format(CREATE_TENDER_URL), json=data, headers=headers)
    prepped = r.prepare()
    resp = s.send(prepped)
    #print(resp.content)
    return json.loads(resp.content)['id']


def retrieve_uaid(internal_id):
    r = Request('GET', "{}/api/procedures/{}".format(CREATE_TENDER_URL, internal_id))
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



#Changing line 112 to self.encoder = json.load(open(vocab_file, 'r', encoding='utf-8')) should fix this issue.

