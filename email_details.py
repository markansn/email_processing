def parse_email(subject, body, metadata):
    toc_payment_amount = ""
    toc_delay_est = ""
    toc_rejection_reason = ""
    toc_outcome_notes = ""


    toc_outcome_ts = get_timestamp(metadata)
    toc_claim_id = get_id(subject)

    if toc_claim_id == "":
        print("COULD NOT FIND toc_claim_id")

    if toc_outcome_ts == "":
        print("COULD NOT FIND toc_outcome_ts")

    claim_status = get_email_type(subject)
    if(claim_status == "Approved"):
        toc_payment_amount = get_payment_amount(body)
        if toc_payment_amount == "":
            print("COULD NOT FIND toc_payment_amount")

        toc_delay_est = get_delay_est(body)
        if toc_delay_est == "":
            print("COULD NOT FIND toc_delay_est")


    elif(claim_status == "Unsuccessful"):
        toc_rejection_reason = get_rejection_reason(body)

        if toc_rejection_reason == "":
            print("COULD NOT FIND toc_rejection_reason")


        elif toc_rejection_reason == "insufficient_delay":
            toc_outcome_notes = get_outcome_notes(body)

            if toc_outcome_notes == "":
                print("COULD NOT FIND toc_outcome_notes")

    else:
        print("COULD NOT FIND claim_status")






    print("claim status " + claim_status)
    print("toc claim id " + toc_claim_id)
    print("toc outcome ts " + toc_outcome_ts)
    print("toc payment amount " + toc_payment_amount)
    print("toc rejection reason " + toc_rejection_reason)
    print("toc outcome notes " + toc_outcome_notes)
    print("toc delay est " + toc_delay_est)
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
    lines = body.strip().splitlines()
    for item in lines:
        if "We used the following information" in item:
            index = lines.index(item)
            out = lines[index + 1].strip() + lines[index + 1].strip()


            return out


    return ""


def get_delay_est(body):
    lines = body.strip().splitlines()
    for line in lines:
        if "We have confirmed that the delay" in line:
            words = line.split(" ")
            start = -1
            end  = -1
            for item in words:
                if item == "between":
                    start = words.index(item)
                elif item == "and":
                    end = words.index(item)

            if start != -1 and end != -1:
                out = ""
                for i in range(start+1, end):
                    if out != "":
                        out = out + " " + words[i]
                    else:
                        out = out + words[i]

                return out


    return ""

def main():
    subject = "South Western Railway Delay Repay – Claim SWR-1772-362-598 – Unsuccessful"
    body = """Dear Graham XXX,

    Thank you for your delay repay claim which we received on Mon, 14 Oct 2019.
    We are sorry that you experienced a delay to your journey.
    
    Your claim has been checked using a set process and the details of any delay verified using industry systems holding historic train running information. We have reviewed your claim and can confirm the following:
    
    Journey Details:
      Travel Date: Thu, 03 Oct 2019
      Departing 07:02 from HASLEMERE to LONDON WATERLOO
    
    Decision: Unsuccessful
    
    We’re sorry you experienced a delay. We’ve reviewed your claim and calculated the overall delay to your journey was 10 minutes. In this instance no compensation is due.
    
    We used the following information to calculate your delay:
    The intended leg from 07:02 HASLEMERE left at 07:06, scheduled to arrive at LONDON WATERLOO at 07:58, actually arrived 08:08.
    Total journey delay: 10 minutes - your intended arrival time was 07:58 and the calculated arrival time for your journey was 08:08.
    
    If you believe we’ve made the wrong decision or that you’ve given us the wrong information, then the quickest way to update us is to appeal the claim using our online web page at https://delayrepay.southwesternrailway.com/claim/SWR-1772-362-598 before Mon, 11 Nov 2019.
    You just need to tell us why you’re submitting the appeal and update any extra details or evidence to help us make the right decision."""

    subject2 = "South Western Railway Delay Repay – Claim SWR-1601-918-613 – Approved"

    body2 = """Dear Julia XXX,

    Thank you for your delay repay claim which we received on Mon, 14 Oct 2019.
    We are sorry that you experienced a delay to your journey.
    
    Your claim has been checked using a set process and the details of any delay verified using industry systems holding historic train running information. We have reviewed your claim and can confirm the following:
    
    Journey Details:
      Travel Date: Thu, 03 Oct 2019
      Departing 06:48 from HASLEMERE to LONDON WATERLOO
    
    Decision: Approved
    
    We have confirmed that the delay you experienced was between 30 - 59 minutes and that you are entitled to £5.39 in compensation.
    
    If you believe we’ve made the wrong decision or that you’ve given us the wrong information, then the quickest way to update us is to appeal the claim using our online web page at https://delayrepay.southwesternrailway.com/claim/SWR-1601-918-613 before Thu, 14 Nov 2019.
    You just need to tell us why you’re submitting the appeal and update any extra details or evidence to help us make the right decision.
    
    
    Yours sincerely,
    
    Customer Support Team"""



    metadata = "date"

    parse_email(subject2, body2, metadata)


if __name__ == '__main__':
    main()