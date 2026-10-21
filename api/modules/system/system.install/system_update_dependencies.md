# system_update_dependencies()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 1864–1885 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1864-L1885)
- **Module/theme:** system
- **Implements:** [hook_update_dependencies()](../system.api.php/hook_update_dependencies.md)

## Signature

```php
function system_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function system_update_dependencies() {
  // system_update_7053() queries the {block} table, so it must run after
  // block_update_7002(), which creates that table.
  $dependencies['system'][7053] = array(
    'block' => 7002,
  );

  // system_update_7061() queries the {node_revision} table, so it must run
  // after node_update_7001(), which renames the {node_revisions} table.
  $dependencies['system'][7061] = array(
    'node' => 7001,
  );

  // system_update_7067() migrates role permissions and therefore must run
  // after the {role} and {role_permission} tables are properly set up, which
  // happens in user_update_7007().
  $dependencies['system'][7067] = array(
    'user' => 7007,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
