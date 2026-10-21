# system_modules_uninstall_validate()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1367–1373 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1367-L1373)
- **Module/theme:** system

## Signature

```php
function system_modules_uninstall_validate($form, &$form_state)
```

## Documentation

```text
Validates the submitted uninstall form.
```

## Code

```php
function system_modules_uninstall_validate($form, &$form_state) {
  // Form submitted, but no modules selected.
  if (!count(array_filter($form_state['values']['uninstall']))) {
    drupal_set_message(t('No modules selected.'), 'error');
    drupal_goto('admin/modules/uninstall');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
