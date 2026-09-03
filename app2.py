import streamlit as st
from sqlalchemy import create_engine , Table , Column, Integer, String, MetData
import pandas as pd
from faker import Faker

engine = create_engine('sqlite:///mydatabase.db')
metdata = Metdata()

users_table = Table('users' , metdata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('address' , String))

metdata.create_all(engine)

fake = Faker()

def generate_fake_data(n=10) :
    with engine.connect() as conn:
        conn.execute(users_table.delete())
        for _ in range(n):
            conn.execute(users_table.insert().values(
                name=fake.name(),
                email=fake.email(),
                address=fake.address()
            ))
        conn.commit()

if st.button('Generate Fake Data'):
    generate_fake_data(20)
    st.success('Fake data generated generated!')

@st.cache_data
def load_data() :
    with engine.connect() as conn:
        query = 'SELECT * FROM users'
        return pd.read_sql(query, conn)

data = load_data()
st.write(data)