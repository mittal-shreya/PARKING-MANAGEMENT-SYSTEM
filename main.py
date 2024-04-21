import streamlit as st
import psycopg2
import pandas as pd
import math

host = 'localhost'
#enter your details
dbname = ' '
user = ' '
password = ' '
port = ' '

conn_string = f"host={host} user={user} dbname={dbname} password={password} port={port}"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

st.title('Parking Management System')

query1 = "SELECT * FROM vehicle_type;"

cursor.execute(query1)
rows = cursor.fetchall()
column_names1 = [desc[0] for desc in cursor.description]
df1 = pd.DataFrame(rows, columns=column_names1)

st.write("Vehicle Types:")
st.write(df1)

st.subheader("Park a vehicle")
type_id = st.number_input("Type ID", min_value=1, max_value=4, value=1, step=1)
vehicle_id = st.text_input("Park Vehicle ID")

if st.button("Park"):
    if vehicle_id and type_id:
        cursor.execute(f"SELECT space_id from parking_space WHERE vehicle_id IS NULL AND type_id={type_id};")
        parking_space=cursor.fetchone()

        if parking_space is not None:
            parking_space=parking_space[0]
            query=f"INSERT INTO vehicle (type_id,vehicle_id,in_time) VALUES ({type_id},'{vehicle_id}',LOCALTIMESTAMP)"
            cursor.execute(query)
            conn.commit()
            query4 = f"UPDATE parking_space SET vehicle_id = '{vehicle_id}' WHERE space_id = {parking_space};"            
            cursor.execute(query4)
            conn.commit()
            st.success("Vehicle parked successfully")
        else:
            st.error("no parking space available")
    else:
        st.error("Please fill in all fields.")

st.subheader("Exit a vehicle")
exit_vehicle_id = st.text_input("Exit Vehicle ID")
if st.button("Exit"):
    if exit_vehicle_id:
        cursor.execute(f"SELECT parking_space.space_id, vehicle.in_time, vehicle.type_id FROM parking_space INNER JOIN vehicle on parking_space.vehicle_id = vehicle.vehicle_id WHERE parking_space.vehicle_id='{exit_vehicle_id}';")
        result = cursor.fetchone()
        
        if result is not None:
            space_id, in_time, type_id = result

            cursor.execute(f"SELECT cost FROM vehicle_type WHERE type_id = {type_id};")
            hourly_rate = cursor.fetchone()[0]

            cursor.execute("SELECT LOCALTIMESTAMP;")
            current_time = cursor.fetchone()[0]

            parking_duration = (current_time - in_time).total_seconds() / 3600

            if parking_duration<=1:
                amount_to_pay=hourly_rate;
            else:
                amount_to_pay = math.ceil(hourly_rate * parking_duration)

            query5=f"UPDATE vehicle SET out_time=LOCALTIMESTAMP, price={amount_to_pay} WHERE vehicle_id='{exit_vehicle_id}';"
            cursor.execute(query5)
            conn.commit()
            
            query6=f"UPDATE parking_space SET vehicle_id = NULL WHERE space_id = {space_id};"
            cursor.execute(query6)
            conn.commit()

            st.success(f"Vehicle exited successfully. The amount to be paid is {amount_to_pay}.")

st.subheader("Search Vehicle")
search_vehicle_id = st.text_input("Search Vehicle ID")
if st.button("Search"):
    if search_vehicle_id:
        cursor.execute(f"SELECT * FROM vehicle WHERE vehicle_id='{search_vehicle_id}';")
        result = cursor.fetchone()

        if result is not None:
            column_names = [desc[0] for desc in cursor.description]
            df_search = pd.DataFrame([result], columns=column_names)
            st.dataframe(df_search)
        else:
            st.error("Vehicle not found")
    else:
        st.error("Please enter a Vehicle ID.")


query2 = "SELECT * FROM vehicle;"
query3 = "SELECT * FROM parking_space;"

cursor.execute(query2)
rows = cursor.fetchall()
column_names2 = [desc[0] for desc in cursor.description]
df2 = pd.DataFrame(rows, columns=column_names2)

cursor.execute(query3)
rows = cursor.fetchall()
column_names3 = [desc[0] for desc in cursor.description]
df3 = pd.DataFrame(rows, columns=column_names3)

st.write("Vehicles:")
st.dataframe(df2)

st.write("Parking Spaces:")
st.dataframe(df3)

cursor.close()
conn.close()
