# node_update_7002()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 556–559 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L556-L559)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7002()
```

## Documentation

```text
Extend the node_promote_status index to include all fields required for the node page query.
```

## Code

```php
function node_update_7002() {
  db_drop_index('node', 'node_promote_status');
  db_add_index('node', 'node_frontpage', array('promote', 'status', 'sticky', 'created'));
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
