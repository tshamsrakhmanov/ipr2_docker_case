from nicegui import ui
import requests

backend_host = 'http://localhost:1234'

rows = [{'id': 'none', 'name': 'none'}]
columns = [{'label': 'id', 'field': 'id'}, {'label': 'name', 'field': 'name'}]

button_save = ui.button(text='Load users', on_click=lambda: update_users_table())

table = ui.table(columns=columns, rows=rows, )

name_input = ui.input('NAME')
surname_input = ui.input('SURNAME')
button_add_user = ui.button(text='Add user', on_click=lambda: add_user())

id_input = ui.input('ID')
button_delete = ui.button(text='Remove user', on_click=lambda: remove_user())


def remove_user():
    response = requests.delete(f'{backend_host}/delete_user/', params=f'id={id_input.value}')
    update_users_table()


def clear_user_input():
    id_input.value = ''
    name_input.value = ''
    surname_input.value = ''


def add_user():
    response = requests.post(f'{backend_host}/add_user/', json={'name': name_input.value, 'surname': surname_input.value})
    update_users_table()


def update_users_table():
    response = requests.get(f"{backend_host}/get_users")
    response_dict = response.json()
    table.rows = [{'id': str(k), 'name': str(v)} for k, v in response_dict.items()]
    table.update()
    clear_user_input()


ui.run(port=1235)
