# image_schema()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 28–114 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L28-L114)
- **Module/theme:** image
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function image_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function image_schema() {
  $schema = array();

  $schema['cache_image'] = drupal_get_schema_unprocessed('system', 'cache');
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
        'description' => 'The style machine name.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
      ),
      'label' => array(
        'description' => 'The style administrative name.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
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

  return $schema;
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
