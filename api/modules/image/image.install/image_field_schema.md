# image_field_schema()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 119–161 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L119-L161)
- **Module/theme:** image
- **Implements:** [hook_field_schema()](../../field/field.api.php/hook_field_schema.md)

## Signature

```php
function image_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function image_field_schema($field) {
  return array(
    'columns' => array(
      'fid' => array(
        'description' => 'The {file_managed}.fid being referenced in this field.',
        'type' => 'int',
        'not null' => FALSE,
        'unsigned' => TRUE,
      ),
      'alt' => array(
        'description' => "Alternative image text, for the image's 'alt' attribute.",
        'type' => 'varchar',
        'length' => 512,
        'not null' => FALSE,
      ),
      'title' => array(
        'description' => "Image title text, for the image's 'title' attribute.",
        'type' => 'varchar',
        'length' => 1024,
        'not null' => FALSE,
      ),
      'width' => array(
        'description' => 'The width of the image in pixels.',
        'type' => 'int',
        'unsigned' => TRUE,
      ),
      'height' => array(
        'description' => 'The height of the image in pixels.',
        'type' => 'int',
        'unsigned' => TRUE,
      ),
    ),
    'indexes' => array(
      'fid' => array('fid'),
    ),
    'foreign keys' => array(
      'fid' => array(
        'table' => 'file_managed',
        'columns' => array('fid' => 'fid'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
