def get_risk(probability):
    """
    Determine customer risk level
    """

    if probability >= 0.70:
        return "High"

    elif probability >= 0.40:
        return "Medium"

    else:
        return "Low"


def get_recommendation(risk):
    """
    Business recommendations
    """

    if risk == "High":

        return [
            "Offer a 20% Discount",
            "Assign a Relationship Manager",
            "Provide Free Technical Support",
            "Contact Customer Within 24 Hours"
        ]

    elif risk == "Medium":

        return [
            "Send Personalized Offers",
            "Recommend Better Plans",
            "Increase Customer Engagement"
        ]

    else:

        return [
            "Maintain Regular Customer Engagement",
            "Reward Customer Loyalty",
            "Send Promotional Offers Occasionally"
        ]