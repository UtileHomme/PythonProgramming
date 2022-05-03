import json, requests

URL = 'http://api.beta.dowjones.com/api/public/2.0/Content/PDF/ArticleRef/json?articleRef=article:archive/AIWINE0020220420ei4k0000l&EncryptedToken=S00UF3DXqFQSTJyMT7yMTYqOTQoM92sMdmm5ErERdBNVsZgME7RQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB'
LocalFilePath = r'C:\Users\jsharma029\Downloads'


def GetPDFforArticle():
    head = {'content-type': 'application/pdf'}

    resp = requests.get(URL, headers=head, timeout=300)

    statusCode = resp.status_code

    if statusCode == 200:
        newfilePath = LocalFilePath + 'article.pdf'
        with open(newfilePath, 'wb') as file:
            file.write(resp.content)


article = GetPDFforArticle()
