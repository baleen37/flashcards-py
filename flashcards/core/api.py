import json

import flask as fl


class APIResponse(fl.Response):
    _status_code = 200

    def __init__(self, data=None, status=None, message=None, headers=None, mimetype='application/json', content_type=None,
                 direct_passthrough=False):
        response = {
            'status': status or self._status_code,
            'message': message or ''
        }
        if data:
            response['data'] = data
        super().__init__(response=json.dumps(response), status=status, headers=headers, mimetype=mimetype,
                         content_type=content_type,
                         direct_passthrough=direct_passthrough)
