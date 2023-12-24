# Set your SQL Server connection parameters
                        server = 'DESKTOP-03OJGVQ\SQLEXPRESS'
                        database = 'myCollege'
                        trusted_connection = 'yes'
                        driver = '{ODBC Driver 17 for SQL Server}'  # Adjust the driver based on your SQL Server version

                        # Create a connection string
                        connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}"

                        # Establish a connection
                        with pyodbc.connect(connection_string) as connection:
                                cursor = connection.cursor()

                                # Use parameterized query to prevent SQL injection
                                insert_query = "INSERT INTO [dbo].[Student] ([studentID], [studentName], [studentAge], [studentGender], [studentDept]) VALUES (?, ?, ?, ?, ?)"

                                # Provide values directly in the execute call
                                cursor.execute(insert_query, int(id), name, int(age), gender, depart)
                                connection.commit()


                        connection.close()

                        print("Data Transfered!")