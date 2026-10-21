# filter_schema()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 11–112 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L11-L112)
- **Module/theme:** filter
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function filter_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function filter_schema() {
  $schema['filter'] = array(
    'description' => 'Table that maps filters (HTML corrector) to text formats (Filtered HTML).',
    'fields' => array(
      'format' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'description' => 'Foreign key: The {filter_format}.format to which this filter is assigned.',
      ),
      'module' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The origin module of the filter.',
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Name of the filter being referenced.',
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Weight of filter within format.',
      ),
      'status' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Filter enabled status. (1 = enabled, 0 = disabled)',
      ),
      'settings' => array(
        'type' => 'blob',
        'not null' => FALSE,
        'size' => 'big',
        'serialize' => TRUE,
        'description' => 'A serialized array of name value pairs that store the filter settings for the specific format.',
      ),
    ),
    'primary key' => array('format', 'name'),
    'indexes' => array(
      'list' => array('weight', 'module', 'name'),
    ),
  );
  $schema['filter_format'] = array(
    'description' => 'Stores text formats: custom groupings of filters, such as Filtered HTML.',
    'fields' => array(
      'format' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'description' => 'Primary Key: Unique machine name of the format.',
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Name of the text format (Filtered HTML).',
        'translatable' => TRUE,
      ),
      'cache' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'size' => 'tiny',
        'description' => 'Flag to indicate whether format is cacheable. (1 = cacheable, 0 = not cacheable)',
      ),
      'status' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 1,
        'size' => 'tiny',
        'description' => 'The status of the text format. (1 = enabled, 0 = disabled)',
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Weight of text format to use when listing.',
      ),
    ),
    'primary key' => array('format'),
    'unique keys' => array(
      'name' => array('name'),
    ),
    'indexes' => array(
      'status_weight' => array('status', 'weight'),
    ),
  );

  $schema['cache_filter'] = drupal_get_schema_unprocessed('system', 'cache');
  $schema['cache_filter']['description'] = 'Cache table for the Filter module to store already filtered pieces of text, identified by text format and hash of the text.';

  return $schema;
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
