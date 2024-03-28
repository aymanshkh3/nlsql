from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st 
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

#connect api fectch from .env 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')       #genrative ,odel gemini pro
    response=model.generate_content([prompt[0],question])       #rquesting response
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):             
    conn=sqlite3.connect(db)            #connection with database   
    cur=conn.cursor()               
    cur.execute(sql)                    #run the prompt fetched given from API
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:                    #print all
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL queries!
The SQL database has the tables SALES and Products with the following columns:

For the SALES table:
- SaleID (INTEGER PRIMARY KEY)
- Date (DATE)
- CustomerID (INTEGER)
- EmployeeID (INTEGER)
- TotalAmount (NUMERIC(10, 2))

For the Products table:
- ProductID (INTEGER PRIMARY KEY)
- ProductName (VARCHAR(255))
- Description (TEXT)
- UnitPrice (NUMERIC(10, 2))
- QuantityInStock (INTEGER)

For example:
Example 1 - How many sales transactions were made in the last week?
The SQL command could resemble this:
SELECT COUNT(*) FROM SALES WHERE Date >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);

Example 2 - Retrieve all products with a unit price greater than $100.
The corresponding SQL query might be:
SELECT * FROM Products WHERE UnitPrice > 100;
also the sql code should not have ``` in beginning or end and sql word in output


    """

    ]



## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")       #interface
st.header("App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")                   #string for input for API

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"storedb")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
