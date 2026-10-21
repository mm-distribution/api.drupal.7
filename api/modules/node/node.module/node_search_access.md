# node_search_access()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1646–1648 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1646-L1648)
- **Module/theme:** node
- **Implements:** [hook_search_access()](../../search/search.api.php/hook_search_access.md)

## Signature

```php
function node_search_access()
```

## Documentation

```text
Implements hook_search_access().
```

## Code

```php
function node_search_access() {
  return user_access('access content');
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
