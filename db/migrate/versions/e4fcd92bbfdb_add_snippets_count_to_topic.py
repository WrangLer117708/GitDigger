"""add snippets_count to Topic

Revision ID: e4fcd92bbfdb
Revises: 39f44685b041
Create Date: 2018-07-01 22:24:58.788000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4fcd92bbfdb'
down_revision = '39f44685b041'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('snippets_count', sa.Integer(), nullable=True, server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topic', 'snippets_count')
    # ### end Alembic commands ###
