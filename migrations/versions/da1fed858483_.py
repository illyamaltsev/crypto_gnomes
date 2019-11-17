"""empty message

Revision ID: da1fed858483
Revises: 6168ab8b5dba
Create Date: 2019-11-17 16:28:49.722064

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da1fed858483'
down_revision = '6168ab8b5dba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'open_key',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'private_key',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'private_key',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('users', 'open_key',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###
