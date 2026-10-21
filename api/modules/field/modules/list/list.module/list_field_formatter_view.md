# list_field_formatter_view()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 461–487 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L461-L487)
- **Module/theme:** list
- **Implements:** [hook_field_formatter_view()](../../../field.api.php/hook_field_formatter_view.md)

## Signature

```php
function list_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Implements hook_field_formatter_view().
```

## Code

```php
function list_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();

  switch ($display['type']) {
    case 'list_default':
      $allowed_values = list_allowed_values($field, $instance, $entity_type, $entity);
      foreach ($items as $delta => $item) {
        if (isset($allowed_values[$item['value']])) {
          $output = field_filter_xss($allowed_values[$item['value']]);
        }
        else {
          // If no match was found in allowed values, fall back to the key.
          $output = field_filter_xss($item['value']);
        }
        $element[$delta] = array('#markup' => $output);
      }
      break;

    case 'list_key':
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => field_filter_xss($item['value']));
      }
      break;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
