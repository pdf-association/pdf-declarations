#!/usr/bin/env python3
#
# SECURITY CAUTION: does not sanitize the JSON input!
#
import json

def generate_html(item):
    # Tidy up the JSON title to make it a reasonable HTML anchor ID
    id = item['title'].lower().replace(' ', '_').replace(':','').replace(',','').replace('.','').replace('(','').replace(')','').replace('/','')
    decln = '<h3 id="' + id + '">' + item['title'] + '</h3>\n'
    decln += '<p>' + item['description'] + '</p>\n'
    decln += '<table style="border: solid 1px lightgrey;">\n'
    # URI - do NOT hyperlink!
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">URI identifier</th><td style="width: 75%;">' + item['uri'] + '</td></tr>\n'
    # Recommended Fields
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">Recommended Fields</th><td style="width: 75%;">'
    s = '' 
    for f in item['recommendedFields']:
        if (len(s) > 0):
            s += ', ' + '<span style="font-family: monospace;">' + f + '</span>'
        else:
            s = '<span style="font-family: monospace;">' + f + '</span>'
    decln += s + '</td></tr>\n'
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">Optional Fields</td><td style="width: 75%;">'
    # Optional Fields
    s = '' 
    for f in item['optionalFields']:
        if (len(s) > 0):
            s += ', ' + '<span style="font-family: monospace;">' + f + '</span>'
        else:
            s = '<span style="font-family: monospace;">' + f + '</span>'
    decln += s + '</td></tr>'
    # Standard
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">Standard</th><td style="width: 75%;">' + item['standard'] + '</td></tr>\n'
    # Version
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">Version</td><td style="width: 75%;">'
    if ('version' in item):
        decln += str(item['version'])
    decln += '</td></tr>\n'
    # External URI
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">URL</th><td style="width: 75%;"><a href="' + item['externalURI'] + '">' + item['externalURI'] + '</a></td></tr>\n'
    # Level
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">Level</th><td style="width: 75%;">'
    if ('level' in item):
        decln += item['level']
    decln += '</td></tr>\n'
    # Technology Reliance
    decln += '  <tr><th scope="row" style="width: 25%; text-align: left;">Technology reliance</th><td style="width: 75%;">'
    s = '' 
    for f in item['technologyReliance']:
        if (len(s) > 0):
            s += ', ' + f
        else:
            s = f
    decln += s + '</td></tr>\n'
    decln += '</table>\n\n'
    return decln


if __name__ == '__main__':
    with open('./declarations/pdf-declarations.json') as f:
        data = json.load(f)
    html = ''
    for d in data['declarations']:
        html += generate_html(d)
    with open('output.html', 'w') as f:
        f.write(html)
