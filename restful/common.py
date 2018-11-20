"""Common methods"""
import ast
import simplejson as json
import werkzeug.wrappers


def valid_response(data, status=200):
    """Valid Response
    This will be return when the http request was successfully processed."""
    data = {
        'count': len(data),
        'data': data
    }
    return werkzeug.wrappers.Response(
        status=status,
        content_type='application/json; charset=utf-8',
        response=json.dumps(data),
    )


def invalid_response(typ, message=None, status=400):
    """Invalid Response
    This will be the return value whenever the server runs into an error
    either from the client or the server."""
    return werkzeug.wrappers.Response(
        status=status,
        content_type='application/json; charset=utf-8',
        response=json.dumps({
            'type': typ,
            'message': message if message else 'wrong arguments (missing validation)',
        }),
    )


def extract_arguments(payload, offset=0, limit=0, order=None):
    """."""
    fields, domain = [], []
    data = payload.keys()
    for payload in data:
        payload = json.loads(payload)
    if payload.get('domain'):
        domain += payload.get('domain')
    if payload.get('fields'):
        fields += payload.get('fields')
    if payload.get('offset'):
        offset = int(payload['offset'])
    if payload.get('limit'):
        limit = int(payload.get('limit'))
    if payload.get('order'):
        order = payload.get('order')
    return [domain, fields, offset, limit, order]
