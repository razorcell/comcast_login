<!-- Get the Firebase App Check Token using goog recaptcha token-->

import requests
import json

url = "https://content-firebaseappcheck.googleapis.com/v1/projects/um-prod/apps/1:191301842497:web:ce1fa5c46dfd19d7:exchangeRecaptchaEnterpriseToken?key=AIzaSyAk4hekTavR_VAVwjJ1vdIxjq1Dxn_3j48"

payload = json.dumps({
  "recaptcha_enterprise_token": "0cAFcWeA7Xb6A57w0j7q7ZibS_dVFIelzw6NMFNUS8Ub5ezTQHMcD8IS_vXXx5IezSZ6ttD5l6qLUU5fQ4zp88zVpzX6VUAROxhD_ZRxcvdJVfmyec-ffWpm0TQQj7SOiF_nJ9HWZ3D4XEWBOg1_pjNZib5n9JfaU4MQWf8b8wGBW4RwYtnCac9qjHSl8rKnELiCmHMrHdHZi_Nj3CTFnvEl5SB2lL6D2h7vaslD4LGOZkqP65oolxmwL1LtU5FrXaVCJptNZQV7GWsqjLUJwV8-uUumX09hNCYhHXgaKSkHGkql-cxa0Bi3FZWrJ9EiqDHbyBhNlG15cwX8-2poyiKnY_uRY0aK-E6fqJNzDwZOV9yjCzMpcWSBKclnlyi4AxJLGZdEqdBk54SJFplEbVgR5WNSpbjO8uplfLgzzpkSGFrHBvVowMOJpDJ01M5hIX8Fugp-K38-bQsc3mb6g-UgqxJV0DQ0vPqYwFfTmGyqJyS7yn0RODKEatJPo01zwlw4heWQgRaWmtvfnNyyBNI4AgYJkQSmI8UMTmXvJJgoWFxCWmoX6D3aSaF2gy-aRMLmhxwyKdBBtU4HeJmPczkcfbzlUt-u94RcZJDg3ufe5yKjkY2lifVojxfVsvsTsViaKQPyaQiGey53go3TTgIpe6RqRESrc8qn6rbOaBnOhvNDA6h52VTaIX94N2hm4pZDm5Ln-UJ3VyaUIFZ9-NywChg_pqFf6tjvNoGqoMmlKwPyV8pl59GYhjpERmB-ATuKV5D6fPznMPRU3fYugwYMMJ9sYGRfUOorvqfnyRqFzBECPB80QZ5NoW3Rl6GY0OnIw5g3Y0QIGl8825qjpTvn77Q-WhuW_45orYNFrTTRZqnLxAdrGpHC9ZDXymlIBt7nhRD5-mCJioPEmdNzVJfyEsExq1Sa6OceYlNKC106kCGNKtOqMSOtumPeevaHUbecHQ7pftoyUVRkQrtu3OD2uRDEWO5Bc6rYdNeWv7lOJazxGli97lbOUv6Np-jc8i9UDocsP93nQN7OMb0XzX_vWA8d8Yt4jZHqvWddOGGytFKbvB_hv1X8ajfZ_Lh3DJiMHys_GuYH9t4neanBEU1Ljg0x0mSyQ9OvTze8fMiqpt6v7HxwPcA7V12lZUUFEPtKECFBGxjraj9KT2h1JcJNREef7jXjJXS5lIKtfL2fOxPoOxIyfGLol24LUGj8UoCmgF_l2EmYJ5QAODTNdy72mvJMD9snQwrSQvnuIulssuE1k4bvg8evfQvgvCHg5lNTxA8tT4HXuXAZcHTPdgtoUIGBV0OnHlE97xzqzNTy6yy5DlifJKnAAVqu0k2v19-TJbw-5JSLn8_t2RrgMlDDzS5-mwhpBa0DrDfSgasK53Fqyer2f2ztmT0Wsab51yEHP3TIyV8oWeZgEbi6nMPORkDQYrpxsmn9aamrT2vnyZoMNawd9vIAEHLuN4Vz4AtT_-pxh0JzmNuS53037NZ-oHfsdTax14kuQxs9tIjwaU_oypd9EKtN-l-GYYjxtzq7i_eWUdYIsS-5B9FxpunfzDJXAK7nQ9pWBHsxPGDwRP7R0oBOMaiM0CMsNIoaS9blaRsBUR2TLkX8uEGMgVR-Cg0mUtrmhtAXyM53EVUC3B8EtTB6GKlDy8qCkyQiiHJZD_FPXO-15T40CJvrDPKLvcSNtKs7tY3tAKDaptb4ddgSQejlEfbJW9xSpfV0cy4kj2YMLuZJIacqxELZKzJ6bOzIQd2JLSTU3ZQsBF40ZZaLLVQeXF_drNe73c14cke25GTBwW5wXlb7ZKJes9qvuJzQRB9WW-LtZBN6AEUEnwsz2Vqwvju7c"
})
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'origin': 'https://unitedmasters.com',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://unitedmasters.com/',
  'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
  'x-browser-channel': 'stable',
  'x-browser-copyright': 'Copyright 2025 Google LLC. All rights reserved.',
  'x-browser-validation': 'Hg4L+ikvx4e+Kz4C1Vi1rALvggw=',
  'x-browser-year': '2025',
  'x-client-data': 'CIi2yQEIprbJAQipncoBCNfeygEIk6HLAQiGoM0BGOHizgE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



<!-- Sign in with Password -->

fetch("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAk4hekTavR_VAVwjJ1vdIxjq1Dxn_3j48", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-browser-channel": "stable",
    "x-browser-copyright": "Copyright 2025 Google LLC. All rights reserved.",
    "x-browser-validation": "Hg4L+ikvx4e+Kz4C1Vi1rALvggw=",
    "x-browser-year": "2025",
    "x-client-data": "CIi2yQEIprbJAQipncoBCNfeygEIk6HLAQiGoM0BGOHizgE=",
    "x-client-version": "Chrome/JsCore/10.14.1/FirebaseCore-web",
    "x-firebase-appcheck": "eyJraWQiOiIwMHlhdmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE5MTMwMTg0MjQ5Nzp3ZWI6Y2UxZmE1YzQ2ZGZkMTlkNyIsImF1ZCI6WyJwcm9qZWN0c1wvMTkxMzAxODQyNDk3IiwicHJvamVjdHNcL3VtLXByb2QiXSwicHJvdmlkZXIiOiJyZWNhcHRjaGFfZW50ZXJwcmlzZSIsImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xOTEzMDE4NDI0OTciLCJleHAiOjE3NTU3ODk0MzQsImlhdCI6MTc1NTc4NzYzNCwianRpIjoiMDBuQnpxdVhTQ2cxcUFDQlhMMUxYR2tIako3TTlJY3FCZ0ZBTXNjbGozTSJ9.dmlcHsM11hs1dmrS27T7H1jzazO-HJ0KpCzoClCFZInrmlqFbvjrJkHDRJdFjyoJsL-zjO5_bbP8BbiL-k6AyTAGH77wT1DiivIW5bZBVwuPo_pr7HsvFE8un3LF6MUP_w-uHMFKK7UdR53BSEVuXdc8LU7CAoIaIJxUKIs5dFPLSRyyde7G5P6F4pSqSbjr5138AUWVdlxt46f2etoL_WH4vg-TK5MPyvTLAPjkcu92sqh6s23TIOX1CtA7VOZnBl1sPzBdXtUlI7CUafN6R49LvYFG3rbstl0cnMaPxR82sbpMu94cdK1j3IPfHSye1bvmf38OP4y_GJ0zrSxamCoOfQKd8TY_3RHGfbPRWWUETu6YQqZeNLykbcS143tFKDC8RR12f9zqSQfjfggjdn1MTp-I7nv8QIsLAJns9zJgFVxO7O49fXnjznd14Noy-wOKEmrBaAyJL7XV_JWKNe8nuEB9vyY9Xs-rVrcmDmTw0oRRrkdhzVPk--rDlc4Q",
    "x-firebase-gmpid": "1:191301842497:web:ce1fa5c46dfd19d7"
  },
  "body": "{\"returnSecureToken\":true,\"email\":\"marc@deck.co\",\"password\":\"@oJ!tbq8yB#!B\",\"clientType\":\"CLIENT_TYPE_WEB\"}",
  "method": "POST",
});

Response:

{
    "kind": "identitytoolkit#VerifyPasswordResponse",
    "localId": "OoyWyKVtc6SyRcqySA57jZE0NF63",
    "email": "marc@deck.co",
    "displayName": "",
    "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3YmZiMmExMWRkZmZjMGFkMmU2ODE0YzY4NzYzYjhjNjg3NTgxZDgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdW0tcHJvZCIsImF1ZCI6InVtLXByb2QiLCJhdXRoX3RpbWUiOjE3NTU3ODkyMTAsInVzZXJfaWQiOiJPb3lXeUtWdGM2U3lSY3F5U0E1N2paRTBORjYzIiwic3ViIjoiT295V3lLVnRjNlN5UmNxeVNBNTdqWkUwTkY2MyIsImlhdCI6MTc1NTc4OTIxMCwiZXhwIjoxNzU1NzkyODEwLCJlbWFpbCI6Im1hcmNAZGVjay5jbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1hcmNAZGVjay5jbyJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.lsRJrRc2jRLmYB6j_jm-le7mIU98-LHY568GgJgd1M9CtCvnHCanDbGFi6p9LbmSoW58zOYfaoSMemrfNwgO8EZSJ1AYcCvQZqPrDbcUj3tfWKxydjH6DC4T1soJw8HmbyeO8jFaye7g3bW86GLjM3-4gqSt8BC5AGxdOkHMceyUjiISAsdi_t4aLimDQhfrEUXStxGTAhs_NFkAVMOqsatarZw2LFKJjwXaLXGL01C3vf5O3rnC9DuBl-RfILZ6H7OoSiGMjfuU18izXVrFSIf1DM-OYMdKyBaUtoAScOILHGMZiVpoRue6IuOsJSIxhGXtZy7MtsJRP_pSCJjpdQ",
    "registered": true,
    "refreshToken": "AMf-vBxUVfUVxojyu3morKQ2rlTaVNvbXKS-DcWikMZuVWZ5n38-Utu_DOzOLP3X-Xi9Y6E6jJJbyG5mHkj10Ph4FPvIClu9PmNyEMWludfNgyjitzcXYfVEEezx9_bBIY9fccSOHk-Odlr1cbTFiLYt_vozmZqNtszBO3QcrYVCQlU2R_bbeOPc3Rj28YFRTg6Cf9A9PsmW",
    "expiresIn": "3600"
}

<!-- Account lookup  -->

we use the idToken from previous request in this one which gives us some details about the user account

fetch("https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=AIzaSyAk4hekTavR_VAVwjJ1vdIxjq1Dxn_3j48", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-browser-channel": "stable",
    "x-browser-copyright": "Copyright 2025 Google LLC. All rights reserved.",
    "x-browser-validation": "Hg4L+ikvx4e+Kz4C1Vi1rALvggw=",
    "x-browser-year": "2025",
    "x-client-data": "CIi2yQEIprbJAQipncoBCNfeygEIk6HLAQiGoM0BGOHizgE=",
    "x-client-version": "Chrome/JsCore/10.14.1/FirebaseCore-web",
    "x-firebase-appcheck": "eyJraWQiOiIwMHlhdmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE5MTMwMTg0MjQ5Nzp3ZWI6Y2UxZmE1YzQ2ZGZkMTlkNyIsImF1ZCI6WyJwcm9qZWN0c1wvMTkxMzAxODQyNDk3IiwicHJvamVjdHNcL3VtLXByb2QiXSwicHJvdmlkZXIiOiJyZWNhcHRjaGFfZW50ZXJwcmlzZSIsImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xOTEzMDE4NDI0OTciLCJleHAiOjE3NTU3ODk0MzQsImlhdCI6MTc1NTc4NzYzNCwianRpIjoiMDBuQnpxdVhTQ2cxcUFDQlhMMUxYR2tIako3TTlJY3FCZ0ZBTXNjbGozTSJ9.dmlcHsM11hs1dmrS27T7H1jzazO-HJ0KpCzoClCFZInrmlqFbvjrJkHDRJdFjyoJsL-zjO5_bbP8BbiL-k6AyTAGH77wT1DiivIW5bZBVwuPo_pr7HsvFE8un3LF6MUP_w-uHMFKK7UdR53BSEVuXdc8LU7CAoIaIJxUKIs5dFPLSRyyde7G5P6F4pSqSbjr5138AUWVdlxt46f2etoL_WH4vg-TK5MPyvTLAPjkcu92sqh6s23TIOX1CtA7VOZnBl1sPzBdXtUlI7CUafN6R49LvYFG3rbstl0cnMaPxR82sbpMu94cdK1j3IPfHSye1bvmf38OP4y_GJ0zrSxamCoOfQKd8TY_3RHGfbPRWWUETu6YQqZeNLykbcS143tFKDC8RR12f9zqSQfjfggjdn1MTp-I7nv8QIsLAJns9zJgFVxO7O49fXnjznd14Noy-wOKEmrBaAyJL7XV_JWKNe8nuEB9vyY9Xs-rVrcmDmTw0oRRrkdhzVPk--rDlc4Q",
    "x-firebase-gmpid": "1:191301842497:web:ce1fa5c46dfd19d7"
  },
  "body": "{\"idToken\":\"eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyZTg4M2NjNDY2M2E2MzMyYWRhNmJjMWU0N2YzZmY1ZTRjOGI1ZDciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdW0tcHJvZCIsImF1ZCI6InVtLXByb2QiLCJhdXRoX3RpbWUiOjE3NTU3ODc4NDcsInVzZXJfaWQiOiJPb3lXeUtWdGM2U3lSY3F5U0E1N2paRTBORjYzIiwic3ViIjoiT295V3lLVnRjNlN5UmNxeVNBNTdqWkUwTkY2MyIsImlhdCI6MTc1NTc4Nzg0NywiZXhwIjoxNzU1NzkxNDQ3LCJlbWFpbCI6Im1hcmNAZGVjay5jbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1hcmNAZGVjay5jbyJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.AilVmLYjubN0PP0IkW6YAa4f_xdBbKx0T4PI-pUXLebrbdlX9oP4BCw-l1FwT17oqLFj2UcrghX3RUVz5rVY370KM2xka3yWPYxcUnXxEkw7HKvI1pbKG18N_TwKU8Gl128W2vnHORuvNY1QNxJE4hprS4w7tAEqvT2Bp2pggPIaAvJLUKlRPzR8frKYavwaNzu70dTxuPbTP_5DzrU92Oxu4Dz5S8dap9O-6UunL7XC3s2dy_3Jav045HJLuApDlQWuRkqmjMQ8SWd6-k4l6Lr7nVIeaF9bJ8j9ha8Bd4JSDUG97Ctkt4oWeq0ANorHdFyBDFLG_RQbeaiMb3Q_lw\"}",
  "method": "POST",
});

Response:

{
    "kind": "identitytoolkit#GetAccountInfoResponse",
    "users": [
        {
            "localId": "OoyWyKVtc6SyRcqySA57jZE0NF63",
            "email": "marc@deck.co",
            "passwordHash": "UkVEQUNURUQ=",
            "emailVerified": true,
            "passwordUpdatedAt": 1755784791201,
            "providerUserInfo": [
                {
                    "providerId": "password",
                    "federatedId": "marc@deck.co",
                    "email": "marc@deck.co",
                    "rawId": "marc@deck.co"
                }
            ],
            "validSince": "1755784791",
            "disabled": false,
            "lastLoginAt": "1755789161936",
            "createdAt": "1755784791201",
            "lastRefreshAt": "2025-08-21T15:12:41.936Z"
        }
    ]
}

<!-- Refresh Token -->

You give it existing refresh token to give you new one with both access_token and refresh_token

fetch("https://securetoken.googleapis.com/v1/token?key=AIzaSyAk4hekTavR_VAVwjJ1vdIxjq1Dxn_3j48", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-browser-channel": "stable",
    "x-browser-copyright": "Copyright 2025 Google LLC. All rights reserved.",
    "x-browser-validation": "Hg4L+ikvx4e+Kz4C1Vi1rALvggw=",
    "x-browser-year": "2025",
    "x-client-data": "CIi2yQEIprbJAQipncoBCNfeygEIk6HLAQiGoM0BGOHizgE=",
    "x-client-version": "Chrome/JsCore/10.14.1/FirebaseCore-web",
    "x-firebase-appcheck": "eyJraWQiOiIwMHlhdmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE5MTMwMTg0MjQ5Nzp3ZWI6Y2UxZmE1YzQ2ZGZkMTlkNyIsImF1ZCI6WyJwcm9qZWN0c1wvMTkxMzAxODQyNDk3IiwicHJvamVjdHNcL3VtLXByb2QiXSwicHJvdmlkZXIiOiJyZWNhcHRjaGFfZW50ZXJwcmlzZSIsImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xOTEzMDE4NDI0OTciLCJleHAiOjE3NTU3ODk0MzQsImlhdCI6MTc1NTc4NzYzNCwianRpIjoiMDBuQnpxdVhTQ2cxcUFDQlhMMUxYR2tIako3TTlJY3FCZ0ZBTXNjbGozTSJ9.dmlcHsM11hs1dmrS27T7H1jzazO-HJ0KpCzoClCFZInrmlqFbvjrJkHDRJdFjyoJsL-zjO5_bbP8BbiL-k6AyTAGH77wT1DiivIW5bZBVwuPo_pr7HsvFE8un3LF6MUP_w-uHMFKK7UdR53BSEVuXdc8LU7CAoIaIJxUKIs5dFPLSRyyde7G5P6F4pSqSbjr5138AUWVdlxt46f2etoL_WH4vg-TK5MPyvTLAPjkcu92sqh6s23TIOX1CtA7VOZnBl1sPzBdXtUlI7CUafN6R49LvYFG3rbstl0cnMaPxR82sbpMu94cdK1j3IPfHSye1bvmf38OP4y_GJ0zrSxamCoOfQKd8TY_3RHGfbPRWWUETu6YQqZeNLykbcS143tFKDC8RR12f9zqSQfjfggjdn1MTp-I7nv8QIsLAJns9zJgFVxO7O49fXnjznd14Noy-wOKEmrBaAyJL7XV_JWKNe8nuEB9vyY9Xs-rVrcmDmTw0oRRrkdhzVPk--rDlc4Q",
    "x-firebase-gmpid": "1:191301842497:web:ce1fa5c46dfd19d7"
  },
  "referrer": "https://unitedmasters.com/",
  "body": "grant_type=refresh_token&refresh_token=AMf-vBwqlTf8PpvhnPHTFRuBxTnhu8pg0jy22i0oRi04l86ov4bNpmjyxCd7lBc0wOnXtALDKEXEUhl0NyJAPlmVTpoECRZb0Y-asSKPhWna3C20NfwA4UuYyhOEyFXpqyhyj4t2gxsO8CicEoM1EeOUVSgVeYVV_7xO9cb-uP7Yx7s6YxG4j7GcEjLmYdUtMfLRZIXnYz9P",
  "method": "POST",
});

Response:

{
    "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3YmZiMmExMWRkZmZjMGFkMmU2ODE0YzY4NzYzYjhjNjg3NTgxZDgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdW0tcHJvZCIsImF1ZCI6InVtLXByb2QiLCJhdXRoX3RpbWUiOjE3NTU3ODkyMTAsInVzZXJfaWQiOiJPb3lXeUtWdGM2U3lSY3F5U0E1N2paRTBORjYzIiwic3ViIjoiT295V3lLVnRjNlN5UmNxeVNBNTdqWkUwTkY2MyIsImlhdCI6MTc1NTc4OTUxOSwiZXhwIjoxNzU1NzkzMTE5LCJlbWFpbCI6Im1hcmNAZGVjay5jbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1hcmNAZGVjay5jbyJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.Cs_yEat2rWuw_PeDLX_AKNsAfkWL-1YqsyQKpngIC9GxZ1VcUZmBXodjZh0j6lMUHRKs6Q0qdulgKD1Bj4gDuNK3LZMCW7-V7GlHQbl9UR-pIJAVlWpqIWuPny9FM3429JGmPQa96YnnHB6Q4hl7axGLHPf9zENIXR94a1Dq381HwdQXhuyrSxBMYvaTRNsMr35sHPmwkb30DS3lhWlycQ4vcZbmbB4OxKOro6qY98mbZHz_4IPXi38DaboV832CBemumA2wm8OIIs4kMVU2734GVSzpJhoyRn8cC0FHB2kF03Vy7tuuvVd_llRBjM-upMBnU-poBoTRvAUX1niEfg",
    "expires_in": "3600",
    "token_type": "Bearer",
    "refresh_token": "AMf-vBxUVfUVxojyu3morKQ2rlTaVNvbXKS-DcWikMZuVWZ5n38-Utu_DOzOLP3X-Xi9Y6E6jJJbyG5mHkj10Ph4FPvIClu9PmNyEMWludfNgyjitzcXYfVEEezx9_bBIY9fccSOHk-Odlr1cbTFiLYt_vozmZqNtszBO3QcrYVCQlU2R_bbeOPc3Rj28YFRTg6Cf9A9PsmW",
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3YmZiMmExMWRkZmZjMGFkMmU2ODE0YzY4NzYzYjhjNjg3NTgxZDgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdW0tcHJvZCIsImF1ZCI6InVtLXByb2QiLCJhdXRoX3RpbWUiOjE3NTU3ODkyMTAsInVzZXJfaWQiOiJPb3lXeUtWdGM2U3lSY3F5U0E1N2paRTBORjYzIiwic3ViIjoiT295V3lLVnRjNlN5UmNxeVNBNTdqWkUwTkY2MyIsImlhdCI6MTc1NTc4OTUxOSwiZXhwIjoxNzU1NzkzMTE5LCJlbWFpbCI6Im1hcmNAZGVjay5jbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1hcmNAZGVjay5jbyJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.Cs_yEat2rWuw_PeDLX_AKNsAfkWL-1YqsyQKpngIC9GxZ1VcUZmBXodjZh0j6lMUHRKs6Q0qdulgKD1Bj4gDuNK3LZMCW7-V7GlHQbl9UR-pIJAVlWpqIWuPny9FM3429JGmPQa96YnnHB6Q4hl7axGLHPf9zENIXR94a1Dq381HwdQXhuyrSxBMYvaTRNsMr35sHPmwkb30DS3lhWlycQ4vcZbmbB4OxKOro6qY98mbZHz_4IPXi38DaboV832CBemumA2wm8OIIs4kMVU2734GVSzpJhoyRn8cC0FHB2kF03Vy7tuuvVd_llRBjM-upMBnU-poBoTRvAUX1niEfg",
    "user_id": "OoyWyKVtc6SyRcqySA57jZE0NF63",
    "project_id": "191301842497"
}


<!-- Login and get the session cookies -->

Need a JWT token

fetch("https://unitedmasters.com/api/proxy/auth", {
  "headers": {
    "content-type": "application/json",
    "system-props": "device_model: Macintosh; os_name: Chrome; os_version: 139; platform: Web;",
    "x-csrf-protect": "1",
  },
  "referrer": "https://unitedmasters.com/login",
  "body": "{\"token\":\"eyJhbGciOiJSUzI1NiIsImtpZCI6IjkyZTg4M2NjNDY2M2E2MzMyYWRhNmJjMWU0N2YzZmY1ZTRjOGI1ZDciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdW0tcHJvZCIsImF1ZCI6InVtLXByb2QiLCJhdXRoX3RpbWUiOjE3NTU3ODc4NDcsInVzZXJfaWQiOiJPb3lXeUtWdGM2U3lSY3F5U0E1N2paRTBORjYzIiwic3ViIjoiT295V3lLVnRjNlN5UmNxeVNBNTdqWkUwTkY2MyIsImlhdCI6MTc1NTc4Nzg0NywiZXhwIjoxNzU1NzkxNDQ3LCJlbWFpbCI6Im1hcmNAZGVjay5jbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1hcmNAZGVjay5jbyJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.AilVmLYjubN0PP0IkW6YAa4f_xdBbKx0T4PI-pUXLebrbdlX9oP4BCw-l1FwT17oqLFj2UcrghX3RUVz5rVY370KM2xka3yWPYxcUnXxEkw7HKvI1pbKG18N_TwKU8Gl128W2vnHORuvNY1QNxJE4hprS4w7tAEqvT2Bp2pggPIaAvJLUKlRPzR8frKYavwaNzu70dTxuPbTP_5DzrU92Oxu4Dz5S8dap9O-6UunL7XC3s2dy_3Jav045HJLuApDlQWuRkqmjMQ8SWd6-k4l6Lr7nVIeaF9bJ8j9ha8Bd4JSDUG97Ctkt4oWeq0ANorHdFyBDFLG_RQbeaiMb3Q_lw\"}",
  "method": "POST",
});