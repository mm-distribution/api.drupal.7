# node_install()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 436–448 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L436-L448)
- **Module/theme:** node
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function node_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function node_install() {
  // Populate the node access table.
  db_insert('node_access')
    ->fields(array(
      'nid' => 0,
      'gid' => 0,
      'realm' => 'all',
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
