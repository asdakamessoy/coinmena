from django.db import models


# wanted ID to be BIG INT but sue to shortage of time, could not resolve the error
# leaving it here just to  give you an idea
# class ModelBigIntegerAuto(models.BigAutoField):
#     """
#     This basically tells django not to try apply the rules it does
#     to 'serial' columns and not trash our custom insta-sequence
#     """
#
#     def get_internal_type(self):
#         return "BigIntegerField"
#
#     def db_type(self, connection):
#         """
#         Custom db type
#         """
#         db_type_format = "BIGINT DEFAULT public.next_id()"
#
#         return db_type_format


class Coin(models.Model):
    """
    Crypto Coin model
    """

    S_ACTIVE = 1
    S_INACTIVE = 2
    S_EXPIRED = 4

    STATES = (
        (S_ACTIVE, "Active"),
        (S_INACTIVE, "Inactive"),
        (S_EXPIRED, "Expired"),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100)
    code = models.TextField(max_length=20)
    # We can use this status in very different ways, we may use this flag to ignore updating its value
    status = models.BooleanField(default=True, help_text="Current coin Status")

    @property
    def display_status(self):
        """
        Get descriptive status

        :return:
        """
        policy_states = dict(self.STATES)
        return policy_states.get(self.status, "-")


class Currency(models.Model):
    """
    Currency model

    """

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100)
    code = models.TextField(max_length=20)


class ExchangeRateLogs(models.Model):
    """
    Currency model

    """

    M_UNKNOWN = 1
    M_RECEIVED = 2
    M_PENDING = 3
    M_FAILURE = 4

    REQUEST_STATUS = (
        (M_UNKNOWN, "Unknown state"),
        (M_RECEIVED, "The exchange rate received"),
        (M_PENDING, "The request pending"),
        (M_FAILURE, "The exchange rate request failed"),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    request_status = models.PositiveSmallIntegerField(
        blank=False,
        default=M_UNKNOWN,
        choices=REQUEST_STATUS,
    )
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    asking_price = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    bid_price = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    last_refreshed = models.DateTimeField(blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    message = models.TextField(
        blank=True, help_text="Response/error message can be saved here"
    )

    @property
    def display_request_status(self):
        """
        Get descriptive status

        :return:
        """
        policy_states = dict(self.REQUEST_STATUS)
        return policy_states.get(self.request_status, "-")
