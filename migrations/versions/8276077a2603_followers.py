"""followers

Revision ID: 8276077a2603
Revises: 23b4bb60731e
Create Date: 2021-03-27 16:27:18.820913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8276077a2603'
down_revision = '23b4bb60731e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
