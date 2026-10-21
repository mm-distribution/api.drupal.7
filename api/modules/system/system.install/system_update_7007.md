# system_update_7007()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2066–2084 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2066-L2084)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7007()
```

## Documentation

```text
Convert to new method of storing permissions.
```

## Code

```php
function system_update_7007() {
  // Copy the permissions from the old {permission} table to the new {role_permission} table.
  $messages = array();
  $result = db_query("SELECT rid, perm FROM {permission} ORDER BY rid ASC");
  $query = db_insert('role_permission')->fields(array('rid', 'permission'));
  foreach ($result as $role) {
    foreach (array_unique(explode(', ', $role->perm)) as $perm) {
      $query->values(array(
        'rid' => $role->rid,
        'permission' => $perm,
      ));
    }
    $messages[] = t('Inserted into {role_permission} the permissions for role ID !id', array('!id' => $role->rid));
  }
  $query->execute();
  db_drop_table('permission');

  return implode(', ', $messages);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
