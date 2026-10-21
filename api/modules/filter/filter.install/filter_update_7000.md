# filter_update_7000()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 172–194 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L172-L194)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7000()
```

## Documentation

```text
Upgrade the {filter_formats} table and rename it to {filter_format}.
```

## Code

```php
function filter_update_7000() {
  db_rename_table('filter_formats', 'filter_format');

  // Add the new {filter_format}.status and {filter_format}.weight column.
  db_add_field('filter_format', 'status', array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => TRUE,
    'default' => 1,
    'size' => 'tiny',
    'description' => 'The status of the text format. (1 = enabled, 0 = disabled)',
  ));
  db_add_field('filter_format', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'Weight of text format to use when listing.',
  ), array(
    'indexes' => array(
      'status_weight' => array('status', 'weight'),
    ),
  ));
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
