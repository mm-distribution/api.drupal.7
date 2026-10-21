# system_update_7081()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3347–3357 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3347-L3357)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7081()
```

## Documentation

```text
Remove the Drupal 6 default install profile if it is still in the database.
```

## Code

```php
function system_update_7081() {
  // Sites which used the default install profile in Drupal 6 and then updated
  // to Drupal 7.44 or earlier will still have a record of this install profile
  // in the database that needs to be deleted.
  db_delete('system')
    ->condition('filename', 'profiles/default/default.profile')
    ->condition('type', 'module')
    ->condition('status', 0)
    ->condition('schema_version', 0)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
