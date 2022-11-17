from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
import sqlalchemy as sa

str_connection = 'postgresql://postgres:Andes420.@localhost:5432/postgres'

engine = create_engine(str_connection)
metadata = MetaData()


with engine.connect() as connection:
    str_sql = "CREATE SCHEMA IF NOT EXISTS cryptocurrencies;"
    str_sql += "COMMENT ON SCHEMA cryptocurrencies IS 'Tablas con valores de Cryptomonedas'"
    result = connection.execute(str_sql)


crypto = sa.Table(
                    'crypto_value',
                    metadata,
                    sa.Column('id', sa.BigInteger(), primary_key = True, autoincrement = True),
                    sa.Column('currency', sa.String(15)),
                    sa.Column('value', DOUBLE_PRECISION),
                    sa.Column('timestamp', sa.DateTime(), nullable = False),
                    schema = 'cryptocurrencies',
                    extend_existing = True,
                    comment = 'Tabla con los valores de cryptomonedas'
)

metadata.create_all(engine)

