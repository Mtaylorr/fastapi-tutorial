"""add content column to post table

Revision ID: 07dfd95d04cf
Revises: 33961924991b
Create Date: 2022-10-17 20:07:51.747318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07dfd95d04cf'
down_revision = '33961924991b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
        sa.Column('content', sa.String, nullable=False)
    )
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
