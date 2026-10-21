# system_update_7036()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2420–2435 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2420-L2435)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7036()
```

## Documentation

```text
Split the 'access site in maintenance mode' permission from 'administer site configuration'.
```

## Code

```php
function system_update_7036() {
  // Get existing roles that can 'administer site configuration'.
  $rids = db_query("SELECT rid FROM {role_permission} WHERE permission = :perm", array(':perm' => 'administer site configuration'))->fetchCol();
  // None found.
  if (empty($rids)) {
    return;
  }
  $insert = db_insert('role_permission')->fields(array('rid', 'permission'));
  foreach ($rids as $rid) {
    $insert->values(array(
      'rid' => $rid,
      'permission' => 'access site in maintenance mode',
    ));
  }
  $insert->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
