from flask_marshmallow import Marshmallow

from app.database.enums import W_D
from app.database.models import WalletHistory

ma = Marshmallow()


class WalletHistorySchema(ma.ModelSchema):
    class Meta:
        model = WalletHistory