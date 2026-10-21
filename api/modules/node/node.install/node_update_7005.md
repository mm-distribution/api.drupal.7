# node_update_7005()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 594–602 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L594-L602)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7005()
```

## Documentation

```text
Add status/comment/promote and sticky columns to the {node_revision} table.
```

## Code

```php
function node_update_7005() {
  foreach (array('status', 'comment', 'promote', 'sticky') as $column) {
    db_add_field('node_revision', $column, array(
      'type' => 'int',
      'not null' => TRUE,
      'default' => 0,
    ));
  }
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
