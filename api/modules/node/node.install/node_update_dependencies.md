# node_update_dependencies()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 453–472 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L453-L472)
- **Module/theme:** node
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function node_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function node_update_dependencies() {
  // node_update_7006() migrates node data to fields and therefore must run
  // after all Field modules have been enabled, which happens in
  // system_update_7027(). It also needs to query the {filter_format} table to
  // get a list of existing text formats, so it must run after
  // filter_update_7000(), which creates that table.
  $dependencies['node'][7006] = array(
    'system' => 7027,
    'filter' => 7000,
  );

  // node_update_7008() migrates role permissions and therefore must run after
  // the {role} and {role_permission} tables are properly set up, which happens
  // in user_update_7007().
  $dependencies['node'][7008] = array(
    'user' => 7007,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
