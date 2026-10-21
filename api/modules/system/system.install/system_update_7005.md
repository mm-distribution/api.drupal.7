# system_update_7005()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2054–2061 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2054-L2061)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7005()
```

## Documentation

```text
Remove throttle columns and variables.
```

## Code

```php
function system_update_7005() {
  db_drop_field('blocks', 'throttle');
  db_drop_field('system', 'throttle');
  variable_del('throttle_user');
  variable_del('throttle_anonymous');
  variable_del('throttle_level');
  variable_del('throttle_probability_limiter');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
