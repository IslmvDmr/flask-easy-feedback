"""empty message

Revision ID: 7ae96adaaa08
Revises: 64bd42cab146
Create Date: 2025-02-18 16:29:23.146506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ae96adaaa08'
down_revision = '64bd42cab146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('message', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pages')
    # ### end Alembic commands ###
