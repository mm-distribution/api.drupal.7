# image_update_7005()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 461–480 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L461-L480)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function image_update_7005()
```

## Documentation

```text
Add a column to the 'image_style' table to store administrative labels.
```

## Code

```php
function image_update_7005() {
  $field = array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
    'description' => 'The style administrative name.',
  );
  db_add_field('image_styles', 'label', $field);

  // Do a direct query here, rather than calling image_styles(),
  // in case Image module is disabled.
  $styles = db_query('SELECT name FROM {image_styles}')->fetchCol();
  foreach ($styles as $style) {
    db_update('image_styles')
      ->fields(array('label' => $style))
      ->condition('name', $style)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
