# dblog_update_7001()

- **Type:** Function
- **File:** [`modules/dblog/dblog.install`](_file.md), lines 110–139 · [local source](../../../../source/modules/dblog/dblog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install#L110-L139)
- **Module/theme:** dblog
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function dblog_update_7001()
```

## Documentation

```text
Update the {watchdog} table.
```

## Code

```php
function dblog_update_7001() {
  // Allow NULL values for links.
  db_change_field('watchdog', 'link', 'link', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => FALSE,
    'default' => '',
    'description' => 'Link to view the result of the event.',
  ));

  // Add an index on uid.
  db_add_index('watchdog', 'uid', array('uid'));

  // Allow longer type values.
  db_change_field('watchdog', 'type', 'type', array(
    'type' => 'varchar',
    'length' => 64,
    'not null' => TRUE,
    'default' => '',
    'description' => 'Type of log message, for example "user" or "page not found."',
  ));

  // Convert the variables field (that stores serialized variables) from text to blob.
  db_change_field('watchdog', 'variables', 'variables', array(
    'type' => 'blob',
    'not null' => TRUE,
    'size' => 'big',
    'description' => 'Serialized array of variables that match the message string and that is passed into the t() function.',
  ));
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.install](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
