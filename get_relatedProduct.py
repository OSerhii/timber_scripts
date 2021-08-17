import json
from requests import Request, Session


class Platforms:
    testTO = "https://tender-online.com.ua/catalogue/offers?id="


CREATE_TENDER_URL = "https://tender-online.com.ua/catalogue/offers?id="
KEY = "9b09378f-0547-4069-8d6c-05aa82f84006"
TENDERS_COUNT = 50
PLATFORM_INSTANCE = Platforms.testTO
relatedProductID = "3019-NAVI-5602024006102-631531"

s = Session()

def create_tender():
    # with open("data/create_tender.json", 'r') as f_obj:
    #     jsn = f_obj.read()
    with open("data/offer_payload.json", 'r') as f_obj:
        jsn = f_obj.read()

    data = json.loads(jsn)

    headers = {
        "Authorization": KEY,
        "Content-Type": "application/json"
    }

    #r = Request('POST', "{}/api/procedures".format(CREATE_TENDER_URL), json=data, headers=headers)
    r = Request('GET',"{}.format(CREATE_TENDER_URL), json=data, headers=headers")
    prepped = r.prepare()
    resp = s.send(prepped)
    return json.loads(resp.content)['id']


def retrieve_uaid(relatedProductID):
    #r = Request('GET', "{}/api/procedures/{}".format(CREATE_TENDER_URL, relatedProductID))
    r = Request('GET', "{}/".format(CREATE_TENDER_URL, relatedProductID))
    prepped = r.prepare()
    resp = s.send(prepped)
    #ua_id = json.loads(resp.content)['auctionId']
    #relatedProductID = json.loads(resp.content)['relatedProduct']
    print("Це уаід", ua_id)
    return ua_id


def create_platform_url(relatedProductID, platform):
    #return "http://{}/participant/auction/bids/{}".format(platform, relatedProductID)
    print(relatedProductID)
    return "http://{}/{}".format(platform, relatedProductID)


if __name__ == '__main__':
    tender_ids = list()
    for i in range(TENDERS_COUNT):
        #internal_id = create_tender()
        #ua_id = retrieve_uaid(internal_id)
        ua_id = retrieve_uaid(relatedProductID)
        #url = create_platform_url(ua_id, PLATFORM_INSTANCE)
        #tender_ids.append(url)
        tender_ids.append(ua_id)
    print(tender_ids)