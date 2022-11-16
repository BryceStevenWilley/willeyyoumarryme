"""spell rehearsal right

Revision ID: 7ecffa2afe8a
Revises: 206258ab306f
Create Date: 2022-11-15 23:52:22.786481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ecffa2afe8a'
down_revision = '206258ab306f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.add_column(sa.Column('invite_to_rehearsal_dinner', sa.Boolean(), nullable=True))
        batch_op.drop_column('invite_to_rehersal_dinner')

    with op.batch_alter_table('user_resp', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rsvp_rehearsal', sa.Boolean(), nullable=True))
        batch_op.drop_column('rsvp_rehersal')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_resp', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rsvp_rehersal', sa.BOOLEAN(), nullable=True))
        batch_op.drop_column('rsvp_rehearsal')

    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.add_column(sa.Column('invite_to_rehersal_dinner', sa.BOOLEAN(), nullable=True))
        batch_op.drop_column('invite_to_rehearsal_dinner')

    # ### end Alembic commands ###
