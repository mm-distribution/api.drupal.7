# user_update_dependencies()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 356–387 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L356-L387)
- **Module/theme:** user
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function user_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function user_update_dependencies() {
  // user_update_7006() updates data in the {role_permission} table, so it must
  // run after system_update_7007(), which populates that table.
  $dependencies['user'][7006] = array(
    'system' => 7007,
  );

  // user_update_7010() needs to query the {filter_format} table to get a list
  // of existing text formats, so it must run after filter_update_7000(), which
  // creates that table.
  $dependencies['user'][7010] = array(
    'filter' => 7000,
  );

  // user_update_7012() uses the file API and inserts records into the
  // {file_managed} table, so it therefore must run after system_update_7061(),
  // which inserts files with specific IDs into the table and therefore relies
  // on the table being empty (otherwise it would accidentally overwrite
  // existing records).
  $dependencies['user'][7012] = array(
    'system' => 7061,
  );

  // user_update_7013() uses the file usage API, which relies on the
  // {file_usage} table, so it must run after system_update_7059(), which
  // creates that table.
  $dependencies['user'][7013] = array(
    'system' => 7059,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
