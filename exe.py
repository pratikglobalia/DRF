# response = {
#     'data':[
#         {
#             'id': 1,
#             'name':'pravin',
#             'subject':['maths','physics']
#         }
#     ],
#     'body':'test'
# }


# print(response['body'])


dict = {
  "data": [
    {
      "billing_details": {
        "address": {
          "city": "null",
          "country": "null",
          "line1": "null",
          "line2": "null",
          "postal_code": "null",
          "state": "null"
        },
        "email": "null",
        "name": "null",
        "phone": "null"
      },
      "card": {
        "brand": "visa",
        "checks": {
          "address_line1_check": "null",
          "address_postal_code_check": "null",
          "cvc_check": "pass"
        },
        "country": "US",
        "exp_month": 7,
        "exp_year": 2023,
        "fingerprint": "Sd1LLdK7s5Sx4Pc1",
        "funding": "credit",
        "generated_from": "null",
        "last4": "4242",
        "networks": {
          "available": [
            "visa"
          ],
          "preferred": "null"
        },
        "three_d_secure_usage": {
          "supported": "true"
        },
        "wallet": "null"
      },
      "created": 1659078242,
      "customer": "cus_M95PUZNuFrjUsa",
      "id": "pm_1LQnEqSH5J91ca1yFSf9lccU",
      "livemode": "false",
      "metadata": {},
      "object": "payment_method",
      "type": "card"
    }
  ],
  "has_more": "false",
  "object": "list",
  "url": "/v1/payment_methods"
}

print(dict['data'][0]['card']['checks']['cvc_check'])