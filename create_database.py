from sqlalchemy import (
    create_engine, Column, Integer, String, Numeric, Date,
    ForeignKey, CheckConstraint, func
)
from sqlalchemy.orm import declarative_base, relationship

DATABASE_URL = "postgresql+psycopg2://postgres:postgres:5432/urban_basket_python"

# Base is a special class that every model below inherits from -- it's how
# SQLAlchemy keeps track of all your table definitions together, so it can
# create them all at once later.
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    city = Column(String(50))
    signup_date = Column(Date, nullable=False, server_default=func.current_date())

    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("unit_price >= 0", name="ck_products_unit_price"),
    )


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, server_default="Completed")

    __table_args__ = (
        CheckConstraint("status IN ('Completed','Cancelled','Pending')", name="ck_orders_status"),
    )

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "orderitems"

    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("quantity > 0", name="ck_orderitems_quantity"),
        CheckConstraint("unit_price >= 0", name="ck_orderitems_unit_price"),
    )

    order = relationship("Order", back_populates="items")
    product = relationship("Product")


def create_all_tables():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/urban_basket_python")
    Base.metadata.create_all(engine)  # creates any table that doesn't exist yet; safe to re-run
    print("All Urban Basket tables created (or already existed).")
    return engine


if __name__ == "__main__":
    create_all_tables()