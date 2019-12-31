"""empty message

Revision ID: 4548240bc39a
Revises: f48b33c4a723
Create Date: 2019-12-31 13:12:06.560938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4548240bc39a'
down_revision = 'f48b33c4a723'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('left',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('right',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('left_id', sa.Integer(), nullable=True),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['left_id'], ['left.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['right.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('right')
    op.drop_table('left')
    # ### end Alembic commands ###
