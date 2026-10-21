# image_update_7000()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 178–261 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L178-L261)
- **Module/theme:** image

## Signature

```php
function image_update_7000()
```

## Documentation

```text
Install the schema for users upgrading from the contributed module.
```

## Code

```php
function image_update_7000() {
  if (!db_table_exists('image_styles')) {
    $schema = array();

    $schema['cache_image'] = system_schema_cache_7054();
    $schema['cache_image']['description'] = 'Cache table used to store information about image manipulations that are in-progress.';

    $schema['image_styles'] = array(
      'description' => 'Stores configuration options for image styles.',
      'fields' => array(
        'isid' => array(
          'description' => 'The primary identifier for an image style.',
          'type' => 'serial',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
        'name' => array(
          'description' => 'The style name.',
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
        ),
      ),
      'primary key' => array('isid'),
      'unique keys' => array(
        'name' => array('name'),
      ),
    );

    $schema['image_effects'] = array(
      'description' => 'Stores configuration options for image effects.',
      'fields' => array(
        'ieid' => array(
          'description' => 'The primary identifier for an image effect.',
          'type' => 'serial',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
        'isid' => array(
          'description' => 'The {image_styles}.isid for an image style.',
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => TRUE,
          'default' => 0,
        ),
        'weight' => array(
          'description' => 'The weight of the effect in the style.',
          'type' => 'int',
          'unsigned' => FALSE,
          'not null' => TRUE,
          'default' => 0,
        ),
        'name' => array(
          'description' => 'The unique name of the effect to be executed.',
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
        ),
        'data' => array(
          'description' => 'The configuration data for the effect.',
          'type' => 'blob',
          'not null' => TRUE,
          'size' => 'big',
          'serialize' => TRUE,
        ),
      ),
      'primary key' => array('ieid'),
      'indexes' => array(
        'isid' => array('isid'),
        'weight' => array('weight'),
      ),
      'foreign keys' => array(
        'image_style' => array(
          'table' => 'image_styles',
          'columns' => array('isid' => 'isid'),
        ),
      ),
    );

    db_create_table('cache_image', $schema['cache_image']);
    db_create_table('image_styles', $schema['image_styles']);
    db_create_table('image_effects', $schema['image_effects']);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
