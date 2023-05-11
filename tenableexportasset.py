from tenable.io import TenableIO
import json

access_key='kkkkkkkkkkkkkkk'
secret_key='sssssssss'

tio = TenableIO(access_key, secret_key, vendor='Casey Reid', product='Export Asset Data', build='0.0.1')

for asset in tio.exports.assets():
    with open('assets.json', 'a') as outfile:
        # add a newline before start appending string
        outfile.write('\n')
        json.dump(asset, outfile)
