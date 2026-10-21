# node_access_test_schema()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.install`](_file.md), lines 11–42 · [local source](../../../../../source/modules/node/tests/node_access_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.install#L11-L42)
- **Module/theme:** node_test
- **Implements:** [hook_schema()](../../../system/system.api.php/hook_schema.md)

## Signature

```php
function node_access_test_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function node_access_test_schema() {
  $schema['node_access_test'] = array(
    'description' => 'The base table for node_access_test.',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid this record affects.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'private' => array(
        'description' => 'Boolean indicating whether the node is private (visible to administrator) or not (visible to non-administrators).',
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'indexes' => array(
      'nid' => array('nid'),
    ),
    'primary key' => array('nid'),
    'foreign keys' => array(
      'versioned_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.install](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
