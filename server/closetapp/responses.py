from collections import namedtuple

from flask import jsonify
from flask import request
from flask import redirect


ResponseCode = namedtuple('ResponseCode',
                          ['numeric_code', 'http_status', 'message'])

class ResponseCodes(object):
    SUCCESS = ResponseCode(0, 200, "ok")
    LOGIN_REQUIRED = ResponseCode(1, 401, "You must be authenticated to " +
                                          "perform that request.")
    ASSIGNMENT_MISSING = ResponseCode(2, 403, "You tried to label an item " +
                                              "that was not assigned to you.")
    DECISION_MISMATCH = ResponseCode(3, 403, "You tried to submit one or more " +
                                             "decisions for the same widget.")
    ADD_TO_DB_ERROR = ResponseCode(4, 500, "There's error adding item to db.")
    INVALID_PARAMETERS = ResponseCode(5, 400, "Invalid parameters.")
    ACCESS_DENIED = ResponseCode(6, 403, "Access denied.")
    QUEUE_SIZE_LIMIT_REACHED = ResponseCode(7, 403, "The size limit for this queue " +
                                                    "has been reached.")
    INVALID_CONTENT = ResponseCode(8, 400, "The content data is not valid. Please check and make sure the objects " +
                                           "have correct keys.")
    UNSUPPORTED_DECISION = ResponseCode(9, 400, "Decision is not supported.")
    USER_EXISTS = ResponseCode(10, 400, "That user already exists!")
    ENTITY_NOT_FOUND = ResponseCode(11, 400, "Entity not found!")
    SEARCH_QUEUE_EXISTS = ResponseCode(12, 400, "search query queue with the same name already exists!")
    INTERNAL_ERROR = ResponseCode(13, 500, "Unexpected internal error")
    QUEUE_EXISTS = ResponseCode(14, 400, "Queue already exists!")
    UNREVIEWED_ITEMS_EXIST = ResponseCode(15, 400, "Failure! You were trying to hide a queue " +
                                                   "with unreviewed items in it.")
    PAGESPEED_LIMIT_EXCEED_ERROR = ResponseCode(16, 403, 'API call failure due to daily Limit Exceeded, ' +
                                                         'please try manually at the moment.')
    PAGESPEED_INTERNAL_ERROR = ResponseCode(17, 500, 'Fail to fetch pagespeed test result, ' +
                                                     'please try manually at the moment.')
    EMPTY_CONTENT = ResponseCode(18, 400, "Content data should not be empty.")
    INVALID_ACTION = ResponseCode(19, 400, "The action is not valid for the object you submitted")
    DECISION_SUBMISSION_ERROR = ResponseCode(20, 500, "Failure on submitting at least one decision. " +
                                                      "Check response data for details")


def api_response(code=None, data=None, headers=None):
    status = "success" if code == ResponseCodes.SUCCESS else "failure"
    
    http_redirects = (301,)
    if not request.is_xhr and code.http_status in http_redirects:
        return redirect(data['url'])

    return jsonify(
        status=status,
        code=code.numeric_code,
        message=code.message,
        data=data,
    ), code.http_status