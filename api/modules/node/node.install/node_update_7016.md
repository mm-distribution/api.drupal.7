# node_update_7016()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 950–962 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L950-L962)
- **Module/theme:** node
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function node_update_7016()
```

## Documentation

```text
Change {history}.nid to an unsigned int in order to match {node}.nid.
```

## Code

```php
function node_update_7016() {
  db_drop_primary_key('history');
  db_drop_index('history', 'nid');
  db_change_field('history', 'nid', 'nid', array(
    'description' => 'The {node}.nid that was read.',
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => TRUE,
    'default' => 0,
  ));
  db_add_primary_key('history', array('uid', 'nid'));
  db_add_index('history', 'nid', array('nid'));
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
