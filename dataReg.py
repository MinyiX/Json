import re, json

mode = "json_format"

jsonFile = open('sample1.json', 'r')
jsonStr = jsonFile.read()
print jsonStr
jsonData = json.loads(jsonStr)
print json.dumps(jsonData, indent=4, sort_keys=True)

fhOrig = open('unprocessed_data.json', 'w')
if mode == "json_format":
    fhOrig.write(json.dumps(jsonData, indent=4, sort_keys=True))
else:
    fhOrig.write(json.dumps(jsonStr, indent=4, sort_keys=True))
fhOrig.close()

listElement = ['start',      'duration',    'fwd_flow_id', 'rev_flow_id', 'id',
               'request_ts', 'response_ts', 'sensor',      'seq',         'response_time']
lelem = '|'.join(listElement)
pat = re.compile(r'("('+lelem+r')":\s+[^,]+?(,\s*| |\}))')

jsonProcessedStr = re.sub(pat, '', jsonStr)
#jsonProcessedStr = re.sub(r',\s*\}', '\}', jsonProcessedStr)


jsonProcessedData = json.loads(jsonProcessedStr)
print jsonProcessedStr

print json.dumps(jsonProcessedData, indent=4, sort_keys=True)
fhProc = open('processed_data.json', 'w')
if mode == "json_format":
    fhProc.write(json.dumps(jsonProcessedData, indent=4, sort_keys=True))
else:
    fhProc.write(json.dumps(jsonProcessedStr, indent=4, sort_keys=True))
fhProc.close()


