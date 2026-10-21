# statistics_schema()

- **Type:** Function
- **File:** [`modules/statistics/statistics.install`](_file.md), lines 26–137 · [local source](../../../../source/modules/statistics/statistics.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.install#L26-L137)
- **Module/theme:** statistics
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function statistics_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function statistics_schema() {
  $schema['accesslog'] = array(
    'description' => 'Stores site access information for statistics.',
    'fields' => array(
      'aid' => array(
        'type' => 'serial',
        'not null' => TRUE,
        'description' => 'Primary Key: Unique accesslog ID.',
      ),
      'sid' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Browser session ID of user that visited page.',
      ),
      'title' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'description' => 'Title of page visited.',
      ),
      'path' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => FALSE,
        'description' => 'Internal path to page visited (relative to Drupal root.)',
      ),
      'url' => array(
        'type' => 'text',
        'not null' => FALSE,
        'description' => 'Referrer URI.',
      ),
      'hostname' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => FALSE,
        'description' => 'Hostname of user that visited the page.',
      ),
      'uid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => FALSE,
        'default' => 0,
        'description' => 'User {users}.uid that visited the page.',
      ),
      'timer' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Time in milliseconds that the page took to load.',
      ),
      'timestamp' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Timestamp of when the page was visited.',
      ),
    ),
    'indexes' => array(
      'accesslog_timestamp' => array('timestamp'),
      'uid' => array('uid'),
    ),
    'primary key' => array('aid'),
    'foreign keys' => array(
      'visitor' => array(
        'table' => 'users',
        'columns' => array('uid' => 'uid'),
      ),
    ),
  );

  $schema['node_counter'] = array(
    'description' => 'Access statistics for {node}s.',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid for these statistics.',
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
      ),
      'totalcount' => array(
        'description' => 'The total number of times the {node} has been viewed.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'size' => 'big',
      ),
      'daycount' => array(
        'description' => 'The total number of times the {node} has been viewed today.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'size' => 'medium',
      ),
      'timestamp' => array(
        'description' => 'The most recent time the {node} has been viewed.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'primary key' => array('nid'),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.install](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.install) · Licensed GPL-2.0-or-later (see LICENSE)._
