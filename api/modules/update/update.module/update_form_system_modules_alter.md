# update_form_system_modules_alter()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 351–353 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L351-L353)
- **Module/theme:** update
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function update_form_system_modules_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for system_modules().

Adds a form submission handler to the system modules form, so that if a site
admin saves the form, we invalidate the cache of available updates.

@see _update_cache_clear()
```

## Code

```php
function update_form_system_modules_alter(&$form, $form_state) {
  $form['#submit'][] = 'update_cache_clear_submit';
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
