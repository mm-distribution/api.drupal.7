# tracker_update_7000()

- **Type:** Function
- **File:** [`modules/tracker/tracker.install`](_file.md), lines 128–221 · [local source](../../../../source/modules/tracker/tracker.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.install#L128-L221)
- **Module/theme:** tracker
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function tracker_update_7000()
```

## Documentation

```text
Create new tracker_node and tracker_user tables.
```

## Code

```php
function tracker_update_7000() {
  $schema['tracker_node'] = array(
    'description' => 'Tracks when nodes were last changed or commented on',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid this record tracks.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'published' => array(
        'description' => 'Boolean indicating whether the node is published.',
        'type' => 'int',
        'not null' => FALSE,
        'default' => 0,
        'size' => 'tiny',
      ),
      'changed' => array(
        'description' => 'The Unix timestamp when the node was most recently saved or commented on.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'indexes' => array(
      'tracker' => array('published', 'changed'),
    ),
    'primary key' => array('nid'),
    'foreign keys' => array(
      'tracked_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
    ),
  );

  $schema['tracker_user'] = array(
    'description' => 'Tracks when nodes were last changed or commented on, for each user that authored the node or one of its comments.',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid this record tracks.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'uid' => array(
        'description' => 'The {users}.uid of the node author or commenter.',
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
      ),
      'published' => array(
        'description' => 'Boolean indicating whether the node is published.',
        'type' => 'int',
        'not null' => FALSE,
        'default' => 0,
        'size' => 'tiny',
      ),
      'changed' => array(
        'description' => 'The Unix timestamp when the node was most recently saved or commented on.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'indexes' => array(
      'tracker' => array('uid', 'published', 'changed'),
    ),
    'primary key' => array('nid', 'uid'),
    'foreign keys' => array(
      'tracked_node' => array(
        'table' => 'node',
        'columns' => array('nid' => 'nid'),
      ),
      'tracked_user' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
    ),
  );

  foreach ($schema as $name => $table) {
    db_create_table($name, $table);
  }

  $max_nid = db_query('SELECT MAX(nid) FROM {node}')->fetchField();
  if ($max_nid != 0) {
    variable_set('tracker_index_nid', $max_nid);
  }
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.install](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.install) · Licensed GPL-2.0-or-later (see LICENSE)._
