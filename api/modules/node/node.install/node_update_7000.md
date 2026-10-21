# node_update_7000()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 512–544 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L512-L544)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7000()
```

## Documentation

```text
Upgrade the node type table and fix node type 'module' attribute to avoid name-space conflicts.
```

## Code

```php
function node_update_7000() {
  // Rename the module column to base.
  db_change_field('node_type', 'module', 'base', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE));

  db_add_field('node_type', 'module', array(
    'description' => 'The module defining this node type.',
    'type' => 'varchar',
    'default' => '',
    'length' => 255,
    'not null' => TRUE,
  ));

  db_add_field('node_type', 'disabled', array(
    'description' => 'A boolean indicating whether the node type is disabled.',
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'size' => 'tiny'
  ));

  $modules = db_select('system', 's')
    ->fields('s', array('name'))
    ->condition('type', 'module');
  db_update('node_type')
    ->expression('module', 'base')
    ->condition('base', $modules, 'IN')
    ->execute();

  db_update('node_type')
    ->fields(array('base' => 'node_content'))
    ->condition('base', 'node')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
