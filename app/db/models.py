import uuid
from typing import Optional

from sqlalchemy import (
    String, Date, Numeric, BigInteger,
    DateTime, ForeignKey, text
)

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[uuid.UUID]= mapped_column( primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str]=mapped_column(String(20), unique=True, index=True)
    asset_type: Mapped[str]=mapped_column(String(20), default="equity")

    name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    currency: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    exchange: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

class PriceBarDaily(Base):
    __tablename__ = "price_bars_daily"

    asset_id: Mapped[uuid.UUID]=mapped_column(ForeignKey("assets.id"),primary_key=True)
    date: Mapped[str]=mapped_column(Date, primary_key=True)
    open: Mapped[Optional[float]] = mapped_column(Numeric(18, 6))
    high: Mapped[Optional[float]] = mapped_column(Numeric(18, 6))
    low: Mapped[Optional[float]] = mapped_column(Numeric(18, 6))
    close: Mapped[Optional[float]] = mapped_column(Numeric(18, 6))
    adj_close: Mapped[Optional[float]] = mapped_column(Numeric(18, 6))
    volume: Mapped[Optional[int]] = mapped_column(BigInteger)

    source: Mapped[str] = mapped_column(
        String(30), default="yahoo"
    )
    ingested_at: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        server_default=text("now()")
    )

    asset: Mapped["Asset"] = relationship()