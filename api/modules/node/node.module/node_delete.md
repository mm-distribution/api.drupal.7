# node_delete()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1234–1236 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1234-L1236)
- **Module/theme:** node

## Signature

```php
function node_delete($nid)
```

## Documentation

```text
Deletes a node.

@param $nid
  A node ID.
```

## Code

```php
function node_delete($nid) {
  node_delete_multiple(array($nid));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
