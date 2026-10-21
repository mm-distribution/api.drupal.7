# update_settings_validate()

- **Type:** Function
- **File:** [`modules/update/update.settings.inc`](_file.md), lines 70–95 · [local source](../../../../source/modules/update/update.settings.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.settings.inc#L70-L95)
- **Module/theme:** update

## Signature

```php
function update_settings_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for update_settings().

Validates the e-mail addresses and ensures the field is formatted correctly.

@see update_settings_submit()
```

## Code

```php
function update_settings_validate($form, &$form_state) {
  if (!empty($form_state['values']['update_notify_emails'])) {
    $valid = array();
    $invalid = array();
    foreach (explode("\n", trim($form_state['values']['update_notify_emails'])) as $email) {
      $email = trim($email);
      if (!empty($email)) {
        if (valid_email_address($email)) {
          $valid[] = $email;
        }
        else {
          $invalid[] = $email;
        }
      }
    }
    if (empty($invalid)) {
      $form_state['notify_emails'] = $valid;
    }
    elseif (count($invalid) == 1) {
      form_set_error('update_notify_emails', t('%email is not a valid e-mail address.', array('%email' => reset($invalid))));
    }
    else {
      form_set_error('update_notify_emails', t('%emails are not valid e-mail addresses.', array('%emails' => implode(', ', $invalid))));
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.settings.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.settings.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
