"""empty message

Revision ID: 097c35ea9d11
Revises: 
Create Date: 2021-10-22 19:26:48.644741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097c35ea9d11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('post_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
