# system_update_7000()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 1896–1919 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1896-L1919)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7000()
```

## Documentation

```text
Rename blog and forum permissions to be consistent with other content types.
```

## Code

```php
function system_update_7000() {
  $result = db_query("SELECT rid, perm FROM {permission} ORDER BY rid");
  foreach ($result as $role) {
    $renamed_permission = $role->perm;
    $renamed_permission = preg_replace('/(?<=^|,\ )create\ blog\ entries(?=,|$)/', 'create blog content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )edit\ own\ blog\ entries(?=,|$)/', 'edit own blog content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )edit\ any\ blog\ entry(?=,|$)/', 'edit any blog content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )delete\ own\ blog\ entries(?=,|$)/', 'delete own blog content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )delete\ any\ blog\ entry(?=,|$)/', 'delete any blog content', $renamed_permission);

    $renamed_permission = preg_replace('/(?<=^|,\ )create\ forum\ topics(?=,|$)/', 'create forum content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )delete\ any\ forum\ topic(?=,|$)/', 'delete any forum content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )delete\ own\ forum\ topics(?=,|$)/', 'delete own forum content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )edit\ any\ forum\ topic(?=,|$)/', 'edit any forum content', $renamed_permission);
    $renamed_permission = preg_replace('/(?<=^|,\ )edit\ own\ forum\ topics(?=,|$)/', 'edit own forum content', $renamed_permission);

    if ($renamed_permission != $role->perm) {
      db_update('permission')
        ->fields(array('perm' => $renamed_permission))
        ->condition('rid', $role->rid)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
