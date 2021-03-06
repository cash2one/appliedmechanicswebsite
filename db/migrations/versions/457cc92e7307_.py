"""empty message

Revision ID: 457cc92e7307
Revises: 36f0758013b4
Create Date: 2016-04-22 05:45:47.560916

"""

# ignore flake8 checks as files generated by Alembic are not PEP8 compatible
# flake8: noqa

# revision identifiers, used by Alembic.
revision = '457cc92e7307'
down_revision = '36f0758013b4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumni',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('surname', sa.String(length=30), nullable=True),
    sa.Column('graduationyear', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alumni')
    ### end Alembic commands ###
