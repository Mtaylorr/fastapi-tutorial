"""create tables

Revision ID: 33961924991b
Revises: 
Create Date: 2022-10-17 19:59:45.053199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33961924991b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('title', sa.String, nullable=False)
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
