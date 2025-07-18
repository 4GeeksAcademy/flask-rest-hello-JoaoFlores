"""empty message

Revision ID: 3bd69636beef
Revises: b6a993ae80a9
Create Date: 2025-07-16 15:13:51.160045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bd69636beef'
down_revision = 'b6a993ae80a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('Media')
    op.drop_table('Post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Post',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Post_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='Post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Post_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Media',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], name='Media_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Media_pkey')
    )
    op.create_table('comment',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment_text', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], name='comment_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comment_pkey')
    )
    # ### end Alembic commands ###
