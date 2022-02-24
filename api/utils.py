from datetime import datetime
import pytz


def convert_to_UTC(ny_datetime):

    pickup_datetime = datetime.strptime(ny_datetime, "%Y-%m-%d %H:%M:%S")

    # localize the user datetime with NYC timezone
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)

    # convert to UTC
    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    return utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
