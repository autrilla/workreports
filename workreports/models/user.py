from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)
from passlib.apps import custom_app_context as workreports_pwd_context


from .meta import Base


Boolean = Integer


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    token = Column(String)
    closing_date = Column(Date)
    # jobs = relationship("Job", back_populates="user")
    can_see_own_reports = Column(Boolean)
    can_see_others_reports = Column(Boolean)
    can_create_reports = Column(Boolean)
    can_edit_reports = Column(Boolean)
    can_review_reports = Column(Boolean)
    can_finish_reports = Column(Boolean)
    can_see_report_sale_price = Column(Boolean)

    can_see_own_jobs = Column(Boolean)
    can_see_others_jobs = Column(Boolean)
    can_create_own_jobs = Column(Boolean)
    can_create_others_jobs = Column(Boolean)

    can_manage_users = Column(Boolean)
    can_manage_permissions = Column(Boolean)

    can_create_notifications = Column(Boolean)

    can_create_own_payment_reports = Column(Boolean)
    can_create_others_payment_reports = Column(Boolean)
    can_create_profit_reports = Column(Boolean)

    def verify_password(self, password):
        return workreports_pwd_context.verify(password, self.password)

    def set_password(self, password):
        password_hash = workreports_pwd_context.encrypt(password)
        self.password = password_hash
