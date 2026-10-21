# node_update_7013()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 918–928 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L918-L928)
- **Module/theme:** node
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function node_update_7013()
```

## Documentation

```text
Change {node}.vid default value from 0 to NULL to avoid deadlock issues on MySQL.
```

## Code

```php
function node_update_7013() {
  db_drop_unique_key('node', 'vid');
  db_change_field('node', 'vid', 'vid', array(
    'description' => 'The current {node_revision}.vid version identifier.',
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => FALSE,
    'default' => NULL,
  ));
  db_add_unique_key('node', 'vid', array('vid'));
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
