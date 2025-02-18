"""empty message

Revision ID: a69b8c6967f6
Revises: 048e61822b9e
Create Date: 2025-02-18 16:42:47.910037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a69b8c6967f6'
down_revision = '048e61822b9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=100),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=10000),
               type_=sa.Text(),
               nullable=False)
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.VARCHAR(length=30), nullable=True))
        batch_op.alter_column('description',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=10000),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=128),
               nullable=True)

    # ### end Alembic commands ###
