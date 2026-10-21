# node_update_7001()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 549–551 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L549-L551)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7001()
```

## Documentation

```text
Rename {node_revisions} table to {node_revision}.
```

## Code

```php
function node_update_7001() {
  db_rename_table('node_revisions', 'node_revision');
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
