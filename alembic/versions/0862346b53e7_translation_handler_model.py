"""translation handler model

Revision ID: 0862346b53e7
Revises: 88c5b7aeb2ea
Create Date: 2021-11-21 23:41:12.440979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0862346b53e7'
down_revision = '88c5b7aeb2ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('translation_handler',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('input_language', sa.String(length=50), nullable=True),
    sa.Column('output_language', sa.String(length=50), nullable=True),
    sa.Column('handler', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translation_handler')
    # ### end Alembic commands ###
