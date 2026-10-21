# node_update_7011()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 863–881 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L863-L881)
- **Module/theme:** node
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function node_update_7011()
```

## Documentation

```text
Update the database from Drupal 6 to match the schema.
```

## Code

```php
function node_update_7011() {
  // Drop node moderation field.
  db_drop_field('node', 'moderate');
  db_drop_index('node', 'node_moderate');

  // Change {node_revision}.status field to default to 1.
  db_change_field('node_revision', 'status', 'status', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 1,
  ));

  // Change {node_type}.module field default.
  db_change_field('node_type', 'module', 'module', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
  ));
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
