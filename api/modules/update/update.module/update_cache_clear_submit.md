# update_cache_clear_submit()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 360–363 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L360-L363)
- **Module/theme:** update

## Signature

```php
function update_cache_clear_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for system_modules().

@see update_form_system_modules_alter()
```

## Code

```php
function update_cache_clear_submit($form, &$form_state) {
  // Clear all update module caches.
  _update_cache_clear();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
