# system_update_7011()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2100–2116 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2100-L2116)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7011()
```

## Documentation

```text
Split the 'bypass node access' permission from 'administer nodes'.
```

## Code

```php
function system_update_7011() {
  // Get existing roles that can 'administer nodes'.
  $rids = array();
  $rids = db_query("SELECT rid FROM {role_permission} WHERE permission = :perm", array(':perm' => 'administer nodes'))->fetchCol();
  // None found.
  if (empty($rids)) {
    return;
  }
  $insert = db_insert('role_permission')->fields(array('rid', 'permission'));
  foreach ($rids as $rid) {
    $insert->values(array(
    'rid' => $rid,
    'permission' => 'bypass node access',
    ));
  }
  $insert->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
