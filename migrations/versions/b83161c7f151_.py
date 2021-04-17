"""empty message

Revision ID: b83161c7f151
Revises: fe6c5afcc909
Create Date: 2021-04-12 20:44:18.979835

"""
import csv
import logging
from datetime import datetime as dt
from pathlib import Path

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b83161c7f151'
down_revision = 'fe6c5afcc909'
branch_labels = None
depends_on = None


log = logging.getLogger(__name__)


def data_load(table):
    path = Path(__file__).parents[2] / "data" / "init-data.csv"
    now = dt.now()
    rows = []
    log.info(f"Reading path {path}")
    with path.open("r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append({**row, "created_at": now})
    log.info(f"Totals rows found: {len(rows)}")
    op.bulk_insert(table, rows)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    radios = op.create_table('radios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('badge', sa.String(20), nullable=False),
    sa.Column('radio', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('badge'),
    sa.UniqueConstraint('radio')
    )
    # ### end Alembic commands ###
    data_load(radios)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('radios')
    # ### end Alembic commands ###