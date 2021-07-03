def exchange_log_to_dict(log):
    """
    Utility function to build the basic representation of a exchange rate log.

    :param log:
    :return:
    """
    return {
        "timestamp": log.timestamp,
        "coin": log.coin.code,
        "request_status": log.display_status,
        "asking_price": "{:.2f}".format(log.asking_price),
        "bid_price": "{:.2f}".format(log.bid_price),
        "exchange_rate": "{:.2f}".format(log.exchange_rate),
        "last_refreshed": log.last_refreshed,
        "currency": log.currency.code,
        "message": log.message,
    }
