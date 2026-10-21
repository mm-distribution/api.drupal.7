# _authorize_filetransfer_connection_settings()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 141–153 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L141-L153)

## Signature

```php
function _authorize_filetransfer_connection_settings($backend)
```

## Documentation

```text
Generates the Form API array for a given connection backend's settings.

@param $backend
  The name of the backend (e.g. 'ftp', 'ssh', etc).

@return
  Form API array of connection settings for the given backend.

@see hook_filetransfer_backends()
```

## Code

```php
function _authorize_filetransfer_connection_settings($backend) {
  $defaults = variable_get('authorize_filetransfer_connection_settings_' . $backend, array());
  $form = array();

  // Create an instance of the file transfer class to get its settings form.
  $filetransfer = authorize_get_filetransfer($backend);
  if ($filetransfer) {
    $form = $filetransfer->getSettingsForm();
  }
  // Fill in the defaults based on the saved settings, if any.
  _authorize_filetransfer_connection_settings_set_defaults($form, NULL, $defaults);
  return $form;
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
