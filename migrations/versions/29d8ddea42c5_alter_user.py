"""alter_user

Revision ID: 29d8ddea42c5
Revises: bae43553016b
Create Date: 2022-01-16 00:44:00.927851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29d8ddea42c5'
down_revision = 'bae43553016b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar', sa.VARCHAR(1024), nullable=True))
    op.add_column('user', sa.Column('intro', sa.VARCHAR(1024), nullable=True))
    op.add_column('user', sa.Column('nickname', sa.VARCHAR(256), nullable=True))
    op.add_column('user', sa.Column('password', sa.VARCHAR(256), nullable=True))
    op.add_column('user', sa.Column('user_type', sa.SMALLINT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_type')
    op.drop_column('user', 'password')
    op.drop_column('user', 'nickname')
    op.drop_column('user', 'intro')
    op.drop_column('user', 'avatar')
    # ### end Alembic commands ###
