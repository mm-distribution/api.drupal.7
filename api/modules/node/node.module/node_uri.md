# node_uri()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 249–253 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L249-L253)
- **Module/theme:** node

## Signature

```php
function node_uri($node)
```

## Documentation

```text
Implements callback_entity_info_uri().
```

## Code

```php
function node_uri($node) {
  return array(
    'path' => 'node/' . $node->nid,
  );
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
