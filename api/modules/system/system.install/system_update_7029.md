# system_update_7029()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2295–2302 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2295-L2302)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7029()
```

## Documentation

```text
Add new 'view own unpublished content' permission for authenticated users.
Preserves legacy behavior from Drupal 6.x.
```

## Code

```php
function system_update_7029() {
  db_insert('role_permission')
    ->fields(array(
      'rid' => DRUPAL_AUTHENTICATED_RID,
      'permission' => 'view own unpublished content',
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
