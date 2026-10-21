# install_settings_form_validate()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 952–967 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L952-L967)

## Signature

```php
function install_settings_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for install_settings_form().

@see install_settings_form_submit()
```

## Code

```php
function install_settings_form_validate($form, &$form_state) {
  $driver = $form_state['values']['driver'];
  $database = $form_state['values'][$driver];
  $database['driver'] = $driver;

  // TODO: remove when PIFR will be updated to use 'db_prefix' instead of
  // 'prefix' in the database settings form.
  $database['prefix'] = $database['db_prefix'];
  unset($database['db_prefix']);

  $form_state['storage']['database'] = $database;
  $errors = install_database_errors($database, $form_state['values']['settings_file']);
  foreach ($errors as $name => $message) {
    form_set_error($name, $message);
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
