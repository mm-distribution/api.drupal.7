# file_field_formatter_view()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 975–1006 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L975-L1006)
- **Module/theme:** file
- **Implements:** [hook_field_formatter_view()](../../field/field.api.php/hook_field_formatter_view.md)

## Signature

```php
function file_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Implements hook_field_formatter_view().
```

## Code

```php
function file_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();

  switch ($display['type']) {
    case 'file_default':
      foreach ($items as $delta => $item) {
        $element[$delta] = array(
          '#theme' => 'file_link',
          '#file' => (object) $item,
        );
      }
      break;

    case 'file_url_plain':
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => empty($item['uri']) ? '' : file_create_url($item['uri']));
      }
      break;

    case 'file_table':
      if (!empty($items)) {
        // Display all values in a single element..
        $element[0] = array(
          '#theme' => 'file_formatter_table',
          '#items' => $items,
        );
      }
      break;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
