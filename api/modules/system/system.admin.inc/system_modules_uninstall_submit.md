# system_modules_uninstall_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1378–1394 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1378-L1394)
- **Module/theme:** system

## Signature

```php
function system_modules_uninstall_submit($form, &$form_state)
```

## Documentation

```text
Processes the submitted uninstall form.
```

## Code

```php
function system_modules_uninstall_submit($form, &$form_state) {
  // Make sure the install API is available.
  include_once DRUPAL_ROOT . '/includes/install.inc';

  if (!empty($form['#confirmed'])) {
    // Call the uninstall routine for each selected module.
    $modules = array_keys($form_state['values']['uninstall']);
    drupal_uninstall_modules($modules);
    drupal_set_message(t('The selected modules have been uninstalled.'));

    $form_state['redirect'] = 'admin/modules/uninstall';
  }
  else {
    $form_state['storage'] = $form_state['values'];
    $form_state['rebuild'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
