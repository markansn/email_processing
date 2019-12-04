def parse_email(subject, body, metadata):
    claim_status = get_email_type(subject)
    toc_claim_id = get_id(subject)
    toc_outcome_ts = get_timestamp(metadata)
    toc_payment_amount = get_payment_amount(body)
    toc_rejection_reason = get_rejection_reason(body)
    toc_outcome_notes = get_outcome_notes(body)
def get_email_type(subject):
    if "Approved" in subject:
        return "Approved"
    elif "Unsuccessful" in subject:
        return "Unsuccessful"
    else:
        return ""

def get_id(subject):
    subject_list = subject.split()
    for word in subject_list:
        if 'SWR' in word:
            return word

    return ""


def get_timestamp(metadata):
    #this needs to be figured out based on what's in the metadata
    return metadata

def get_payment_amount(body):
    body_list = body.split()
    for word in body_list:
        if "£" in word:
            return word

    return ""

def get_rejection_reason(body):
    if "overall delay" in body and "no compensation" in body:
        return "insufficient_delay"
    if "to be able to assess a claim fully" in body:
        return "missing_information"
    if "the ticket provided is not valid" in body:
        return "invalid ticket"
    if "unable to find a timetabled journey" in body:
        return "no_service_match"

    return ""


def get_outcome_notes(body):
    #todo

