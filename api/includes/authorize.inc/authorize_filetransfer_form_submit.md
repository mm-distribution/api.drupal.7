# authorize_filetransfer_form_submit()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 227–282 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L227-L282)

## Signature

```php
function authorize_filetransfer_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for authorize_filetransfer_form().

@see authorize_filetransfer_form()
@see authorize_filetransfer_validate()
```

## Code

```php
function authorize_filetransfer_form_submit($form, &$form_state) {
  global $base_url;
  switch ($form_state['triggering_element']['#name']) {
    case 'process_updates':

      // Save the connection settings to the DB.
      $filetransfer_backend = $form_state['values']['connection_settings']['authorize_filetransfer_default'];

      // If the database is available then try to save our settings. We have
      // to make sure it is available since this code could potentially (will
      // likely) be called during the installation process, before the
      // database is set up.
      try {
        $connection_settings = array();
        foreach ($form_state['values']['connection_settings'][$filetransfer_backend] as $key => $value) {
          // We do *not* want to store passwords in the database, unless the
          // backend explicitly says so via the magic #filetransfer_save form
          // property. Otherwise, we store everything that's not explicitly
          // marked with #filetransfer_save set to FALSE.
          if (!isset($form['connection_settings'][$filetransfer_backend][$key]['#filetransfer_save'])) {
            if ($form['connection_settings'][$filetransfer_backend][$key]['#type'] != 'password') {
              $connection_settings[$key] = $value;
            }
          }
          // The attribute is defined, so only save if set to TRUE.
          elseif ($form['connection_settings'][$filetransfer_backend][$key]['#filetransfer_save']) {
            $connection_settings[$key] = $value;
          }
        }
        // Set this one as the default authorize method.
        variable_set('authorize_filetransfer_default', $filetransfer_backend);
        // Save the connection settings minus the password.
        variable_set('authorize_filetransfer_connection_settings_' . $filetransfer_backend, $connection_settings);

        $filetransfer = authorize_get_filetransfer($filetransfer_backend, $form_state['values']['connection_settings'][$filetransfer_backend]);

        // Now run the operation.
        authorize_run_operation($filetransfer);
      }
      catch (Exception $e) {
        // If there is no database available, we don't care and just skip
        // this part entirely.
      }

      break;

    case 'enter_connection_settings':
      $form_state['rebuild'] = TRUE;
      break;

    case 'change_connection_type':
      $form_state['rebuild'] = TRUE;
      unset($form_state['values']['connection_settings']['authorize_filetransfer_default']);
      break;
  }
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
