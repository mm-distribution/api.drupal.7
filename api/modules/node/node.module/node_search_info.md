# node_search_info()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1636–1641 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1636-L1641)
- **Module/theme:** node
- **Implements:** [hook_search_info()](../../search/search.api.php/hook_search_info.md)

## Signature

```php
function node_search_info()
```

## Documentation

```text
Implements hook_search_info().
```

## Code

```php
function node_search_info() {
  return array(
    'title' => 'Content',
    'path' => 'node',
  );
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
