import json
from requests import Request, Session


class Platforms:
    testTO = "https://tender-online.com.ua/catalogue/offers?id="


CREATE_TENDER_URL = "https://tender-online.com.ua/catalogue/offers?id="
KEY = "9b09378f-0547-4069-8d6c-05aa82f84006"
TENDERS_COUNT = 50
PLATFORM_INSTANCE = Platforms.testTO
relatedProductID = "3019-NAVI-5602024006102-631531"
testTO = "https://tender-online.com.ua/catalogue/offers?id="

s = Session()

# def retrieve_uaid(relatedProductID):
#     #r = Request('GET', "{}/api/procedures/{}".format(CREATE_TENDER_URL, relatedProductID))
#     r = Request('GET', "{}/".format(CREATE_TENDER_URL, relatedProductID))
#     prepped = r.prepare()
#     resp = s.send(prepped)
#     #ua_id = json.loads(resp.content)['auctionId']
#     #relatedProductID = json.loads(resp.content)['relatedProduct']
#     print("Це уаід", ua_id)
#     return ua_id


def create_platform_url(relatedProductID, testTO):
    print(testTO, relatedProductID)
    return "http://{}/{}".format(testTO, relatedProductID)
