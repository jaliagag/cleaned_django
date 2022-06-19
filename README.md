# Clean django

## Conventions

- Programming language: English
- WUI language: Spanish
- Case style: `snake_case` ([official guide](https://peps.python.org/pep-0008/))
- When possible, use single quotes `''`

## Steps

- `django-admin startproject clean`
- `cd clean`
- `python manage.py migrate`
- `python manage.py runserver`
- `python manage.py startapp BookRecord`
- Create `BookRecord/urls.py` and add `home` path
- In `views.py` create `home` view
- Add db info to `BookRecord/models.py`
- Mirror db info on `BookRecord/forms.py`
- Import views on `BookRecord/views.py`
- Add models to `BookRecord/views.py` as well as tables created on models
- Create superuser with name `jaliaga` password `123Admin`
- Create CRUD using views

```console
├── admin.py
├── apps.py
├── forms.py
├── migrations
│   [...]   
├── models.py
├── static
│   [...]   
├── template
│   ├── BookRecord
│   │   ├── book_confirm_delete.html
│   │   ├── book_detail.html
│   │   ├── book_form.html
│   │   ├── book_list.html
│   │   ├── dev.html
│   │   └── template.html
│   └── template.html
├── tests.py
├── urls.py
│   ├── delete_book
│   ├── update_book
│   ├── create_book
│   └── list_book
├── views.py
│   ├── Delete_book() # uses book_confirm_delete.html
│   ├── Detail_book() # uses book_detail.html
│   ├── Create_book() # uses book_form.html
│   ├── List_book()   # uses book_list.html
│   └── template.html
```

- Create login
  - Create `template/login.html`
  - Add login url on `BookRecord/urls.py`
  - On `BookRecord/views.py` make imports







