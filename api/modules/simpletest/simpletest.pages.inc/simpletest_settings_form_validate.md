# simpletest_settings_form_validate()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 500–512 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L500-L512)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_settings_form_validate($form, &$form_state)
```

## Documentation

```text
Validation handler for simpletest_settings_form().
```

## Code

```php
function simpletest_settings_form_validate($form, &$form_state) {
  // If a username was provided but a password wasn't, preserve the existing
  // password.
  if (!empty($form_state['values']['simpletest_httpauth_username']) && empty($form_state['values']['simpletest_httpauth_password'])) {
    $form_state['values']['simpletest_httpauth_password'] = variable_get('simpletest_httpauth_password', '');
  }

  // If a password was provided but a username wasn't, the credentials are
  // incorrect, so throw an error.
  if (empty($form_state['values']['simpletest_httpauth_username']) && !empty($form_state['values']['simpletest_httpauth_password'])) {
    form_set_error('simpletest_httpauth_username', t('HTTP authentication credentials must include a username in addition to a password.'));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
