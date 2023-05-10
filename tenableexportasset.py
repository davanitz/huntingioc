from tenable.io import TenableIO
import pprint

access_key='kkkkkkkkkkkkkkk'
secret_key='sssssssss'

tio = TenableIO(access_key, secret_key, vendor='Casey Reid', product='Export Asset Data', build='0.0.1')

for asset in tio.exports.assets():
    #pprint.pprint(asset)
    outfile = open('assets_tenableio.txt', 'w')
    print(input_list[asset], file=outfile)
    outfile.close()
