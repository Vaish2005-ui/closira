def match_sop(message: str):

    message = message.lower()

    if "price" in message or "pricing" in message:
        return {
            "sop": "Pricing Enquiry",
            "response": "Thank you for your pricing enquiry. Our team will contact you shortly."
        }

    elif "book" in message or "appointment" in message:
        return {
            "sop": "Booking Enquiry",
            "response": "Your booking enquiry has been received."
        }

    elif "complaint" in message or "bad" in message:
        return {
            "sop": "Complaint",
            "response": "We are sorry for the inconvenience caused."
        }

    elif "closed" in message or "after hours" in message:
        return {
            "sop": "After Hours",
            "response": "Our office is currently closed."
        }

    else:
        return None