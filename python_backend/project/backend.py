from fastapi import FastAPI, HTTPException
import psycopg2
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str


def make_app():
    application = FastAPI()

    @application.get("/status")
    async def status():
        return {"Message": "Welcome!"}

    @application.get("/db_status")
    async def db_status():

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {"Message": "Database host ONLINE, Database present OK"}

    @application.get("/check_table")
    async def check_table():

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_catalog='postgres_db' AND table_schema='public' AND table_name='newtable')"
                cursor.execute(command_new_user)
                user_id = cursor.fetchone()

            if user_id[0] is False:
                raise HTTPException(status_code=500,
                                    detail='base_table not present. Please create one by another request.')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {'Result': 'Table newtable present in database'}

    @application.get("/create_table")
    async def create_table():

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"CREATE TABLE public.newtable (id bigserial NOT NULL,name varchar NULL,surname varchar NULL,CONSTRAINT newtable_pk PRIMARY KEY (id));"
                cursor.execute(command_new_user)

            with connection.cursor() as cursor:
                command_new_user = f"insert into newtable values (0, 'root', 'root')"
                cursor.execute(command_new_user)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {'Result': 'Table newtable created successfully!'}

    @application.get("/delete_table")
    async def delete_table():

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"DROP table newtable"
                cursor.execute(command_new_user)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {'Result': 'Scheme "newtable" have been deleted'}

    @application.post("/add_user/")
    async def add_user(user: User):

        # check process
        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"select * from newtable n where id = 0 "
                cursor.execute(command_new_user)
                list_of_users = cursor.fetchall()

                # print(list_of_users, 'asdfasdfasdf!')

                if list_of_users == []:
                    command_new_user = f"insert into newtable values (0, 'root', 'root')"
                    cursor.execute(command_new_user)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        # process of add
        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"insert into newtable values ((select max(id) from newtable) + 1, '{user.name}', '{user.surname}')"
                cursor.execute(command_new_user)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {'Result': f'User {user.name} / {user.surname} have been added'}

    @application.get("/get_users")
    async def get_users():

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"select * from newtable"
                cursor.execute(command_new_user)
                users_list = cursor.fetchall()

            # print(users_list)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {str(id_user): str(name + ' ' + surname) for id_user, name, surname in users_list} if users_list else {
            'Result': 'No active users found!'}

    @application.delete("/delete_user/")
    async def add_user(id: int):
        # print(id)

        # check - if user exists
        # if not - throw error

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"select * from newtable where id = {id}"
                cursor.execute(command_new_user)
                user_id = cursor.fetchall()
            if user_id == []:
                raise HTTPException(status_code=500, detail=f"User {id} not found")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"DELETE FROM newtable WHERE id = {id}"
                cursor.execute(command_new_user)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        # removal process
        try:
            connection = psycopg2.connect(
                host='localhost',
                port='5430',
                user='postgres_user',
                password='postgres_password',
                database='postgres_db'
            )

            connection.set_session(autocommit=True)

            with connection.cursor() as cursor:
                command_new_user = f"DELETE FROM newtable WHERE id = {id}"
                cursor.execute(command_new_user)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

        return {'Result': f'User ID:{id} have been removed'}

    return application


if __name__ == '__main__':
    import uvicorn

    new_app = make_app()

    uvicorn.run(new_app, host='0.0.0.0', port=1234)
