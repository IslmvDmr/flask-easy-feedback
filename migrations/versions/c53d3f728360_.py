"""empty message

Revision ID: c53d3f728360
Revises: f8db84051613
Create Date: 2025-02-18 16:55:36.325208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c53d3f728360'
down_revision = 'f8db84051613'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.drop_column('url')

    # ### end Alembic commands ###
