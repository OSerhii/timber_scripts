import json
from requests import Request, Session

CREATE_TENDER_URL = "https://procedure-sandbox.prozorro.sale"
KEY = "9fa74b0e-e692-4746-b38b-8a4387097a53"
TENDERS_COUNT = 100


def create_tender():
    with open("data/create_tender.json", 'r') as f_obj:
        jsn = f_obj.read()

    data = json.loads(jsn)
    headers = {
        "Authorization": KEY,
        "Content-Type": "application/json"
    }

    s = Session()
    r = Request('POST', "{}/api/procedures".format(CREATE_TENDER_URL), json=data, headers=headers)
    prepped = r.prepare()
    resp = s.send(prepped)
    print(resp.content)
    return json.loads(resp.content)['id']


if __name__ == '__main__':
    tender_ids = list()
    for i in range(TENDERS_COUNT):
        tender_ids.append(create_tender())
    print(tender_ids)
