from sqlalchemy import (Column, Integer, String, Date, Float, Boolean,
                        ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    token = Column(String)
    closing_date = Column(Date)
    jobs = relationship("Job", back_populates="user")

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


class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    description = Column(String)
    price = Column(Float)
    hours_worked = Column(Float)
    report_id = Column(Integer, ForeignKey('report.id'))
    report = relationship("Report", back_populates="jobs")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="jobs")


class Report(Base):
    __tablename__ = 'report'
    customer_number = Column(String)
    customer_name = Column(String)
    city = Column(String)
    sale_price = Column(Float)
    observations = Column(String)
    finished = Column(Boolean)
    finished_date = Column(Date)
    checked = Column(Boolean)
    jobs = relationship("Job", back_populates="report")
    waybills = Column(postgresql.ARRAY(String))


class Notification(Base):
    __tablename__ = 'notification'
    from_user_id = Column(Integer, ForeignKey('user.id'))
    from_user = relationship("User", back_populates="sent_notifications")
    to_user_id = Column(Integer, ForeignKey('user.id'))
    to_user = relationship("User", back_populates="received_notifications")
    date = Column(Date)
    message = Column(String)
