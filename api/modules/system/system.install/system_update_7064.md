# system_update_7064()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3114–3116 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3114-L3116)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7064()
```

## Documentation

```text
Remove block_callback field from {menu_router}.
```

## Code

```php
function system_update_7064() {
  db_drop_field('menu_router', 'block_callback');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
