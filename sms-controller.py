""" Uses the body of the sms to decide what to do """

def sms_controller(body):
    if (body[0] == '$'):
        