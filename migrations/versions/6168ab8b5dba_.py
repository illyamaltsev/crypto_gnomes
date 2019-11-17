"""empty message

Revision ID: 6168ab8b5dba
Revises: 
Create Date: 2019-11-17 16:11:35.448212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6168ab8b5dba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('open_key', sa.String(length=20), nullable=False),
    sa.Column('private_key', sa.String(length=20), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('open_key'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('private_key')
    )
    op.create_table('coins_of_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('coin_id', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['coin_id'], ['coins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stakan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('B', 'S', name='b_s'), server_default='B', nullable=True),
    sa.Column('count', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('A', 'InA', name='a_ina'), server_default='InA', nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('coin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['coin_id'], ['coins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallet_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('coin_id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Float(), nullable=False),
    sa.Column('operation', sa.Enum('W', 'D', name='w_d'), server_default='W', nullable=True),
    sa.ForeignKeyConstraint(['coin_id'], ['coins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet_history')
    op.drop_table('stakan')
    op.drop_table('coins_of_user')
    op.drop_table('users')
    op.drop_table('coins')
    # ### end Alembic commands ###