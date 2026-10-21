# install_settings_form_submit()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1011–1030 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1011-L1030)

## Signature

```php
function install_settings_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for install_settings_form().

@see install_settings_form_validate()
```

## Code

```php
function install_settings_form_submit($form, &$form_state) {
  global $install_state;

  // Update global settings array and save.
  $settings['databases'] = array(
    'value'    => array('default' => array('default' => $form_state['storage']['database'])),
    'required' => TRUE,
  );
  $settings['drupal_hash_salt'] = array(
    'value'    => drupal_random_key(),
    'required' => TRUE,
  );
  drupal_rewrite_settings($settings);
  // Indicate that the settings file has been verified, and check the database
  // for the last completed task, now that we have a valid connection. This
  // last step is important since we want to trigger an error if the new
  // database already has Drupal installed.
  $install_state['settings_verified'] = TRUE;
  $install_state['completed_task'] = install_verify_completed_task();
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
