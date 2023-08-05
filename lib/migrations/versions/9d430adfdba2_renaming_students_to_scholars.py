"""Renaming students to scholars

Revision ID: 9d430adfdba2
Revises: 791279dd0760
Create Date: 2023-08-05 04:02:13.914088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d430adfdba2'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
