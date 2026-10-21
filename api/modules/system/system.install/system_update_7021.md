# system_update_7021()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2276–2281 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2276-L2281)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7021()
```

## Documentation

```text
Change the PHP for settings permission.
```

## Code

```php
function system_update_7021() {
  db_update('role_permission')
    ->fields(array('permission' => 'use PHP for settings'))
    ->condition('permission', 'use PHP for block visibility')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
