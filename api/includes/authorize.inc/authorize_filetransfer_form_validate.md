# authorize_filetransfer_form_validate()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 194–219 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L194-L219)

## Signature

```php
function authorize_filetransfer_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for authorize_filetransfer_form().

@see authorize_filetransfer_form()
@see authorize_filetransfer_submit()
```

## Code

```php
function authorize_filetransfer_form_validate($form, &$form_state) {
  // Only validate the form if we have collected all of the user input and are
  // ready to proceed with updating or installing.
  if ($form_state['triggering_element']['#name'] != 'process_updates') {
    return;
  }

  if (isset($form_state['values']['connection_settings'])) {
    $backend = $form_state['values']['connection_settings']['authorize_filetransfer_default'];
    $filetransfer = authorize_get_filetransfer($backend, $form_state['values']['connection_settings'][$backend]);
    try {
      if (!$filetransfer) {
        throw new Exception(t('Error, this type of connection protocol (%backend) does not exist.', array('%backend' => $backend)));
      }
      $filetransfer->connect();
    }
    catch (Exception $e) {
      // The format of this error message is similar to that used on the
      // database connection form in the installer.
      form_set_error('connection_settings', t('Failed to connect to the server. The server reports the following message: !message For more help installing or updating code on your server, see the <a href="@handbook_url">handbook</a>.', array(
        '!message' => '<p class="error">' . $e->getMessage()  . '</p>',
        '@handbook_url' => 'http://drupal.org/documentation/install/modules-themes',
      )));
    }
  }
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
