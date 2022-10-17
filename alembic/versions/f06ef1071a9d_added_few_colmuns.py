"""added few colmuns

Revision ID: f06ef1071a9d
Revises: 912eff967bb2
Create Date: 2022-10-17 20:27:45.080830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f06ef1071a9d'
down_revision = '912eff967bb2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean, nullable=False, server_default='TRUE')
    )
    op.add_column('posts', sa.Column(
        "created_at",sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
    )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
