# block_update_dependencies()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 192–201 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L192-L201)
- **Module/theme:** block
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function block_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function block_update_dependencies() {
  // block_update_7005() needs to query the {filter_format} table to get a list
  // of existing text formats, so it must run after filter_update_7000(), which
  // creates that table.
  $dependencies['block'][7005] = array(
    'filter' => 7000,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
