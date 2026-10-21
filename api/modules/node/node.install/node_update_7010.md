# node_update_7010()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 819–849 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L819-L849)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7010()
```

## Documentation

```text
Add the {block_node_type} table.
```

## Code

```php
function node_update_7010() {
  $schema['block_node_type'] = array(
    'description' => 'Sets up display criteria for blocks based on content types',
    'fields' => array(
      'module' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'description' => "The block's origin module, from {block}.module.",
      ),
      'delta' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'description' => "The block's unique delta within module, from {block}.delta.",
      ),
      'type' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'description' => "The machine-readable name of this type from {node_type}.type.",
      ),
    ),
    'primary key' => array('module', 'delta', 'type'),
    'indexes' => array(
      'type' => array('type'),
    ),
  );

  db_create_table('block_node_type', $schema['block_node_type']);
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
