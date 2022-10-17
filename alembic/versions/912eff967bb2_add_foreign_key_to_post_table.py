"""add foreign key to post table

Revision ID: 912eff967bb2
Revises: 568c1a3d58f1
Create Date: 2022-10-17 20:22:53.812816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912eff967bb2'
down_revision = '568c1a3d58f1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', source_table = "posts", referent_table="users",
        local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name='posts')
    op.drop_column('posts', "owner_id")
    pass
