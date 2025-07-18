"""empty message

Revision ID: d95b907c0503
Revises: 3bd69636beef
Create Date: 2025-07-16 15:20:44.773136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95b907c0503'
down_revision = '3bd69636beef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Follower', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_to_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'User', ['user_to_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Follower', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_to_id')

    # ### end Alembic commands ###
