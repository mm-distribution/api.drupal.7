# number_field_formatter_view()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 297–325 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L297-L325)
- **Module/theme:** number
- **Implements:** [hook_field_formatter_view()](../../../field.api.php/hook_field_formatter_view.md)

## Signature

```php
function number_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Implements hook_field_formatter_view().
```

## Code

```php
function number_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();
  $settings = $display['settings'];

  switch ($display['type']) {
    case 'number_integer':
    case 'number_decimal':
      foreach ($items as $delta => $item) {
        $output = number_format($item['value'], $settings['scale'], $settings['decimal_separator'], $settings['thousand_separator']);
        if ($settings['prefix_suffix']) {
          $prefixes = isset($instance['settings']['prefix']) ? array_map('field_filter_xss', explode('|', $instance['settings']['prefix'])) : array('');
          $suffixes = isset($instance['settings']['suffix']) ? array_map('field_filter_xss', explode('|', $instance['settings']['suffix'])) : array('');
          $prefix = (count($prefixes) > 1) ? format_plural($item['value'], $prefixes[0], $prefixes[1]) : $prefixes[0];
          $suffix = (count($suffixes) > 1) ? format_plural($item['value'], $suffixes[0], $suffixes[1]) : $suffixes[0];
          $output = $prefix . $output . $suffix;
        }
        $element[$delta] = array('#markup' => $output);
      }
      break;

    case 'number_unformatted':
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => $item['value']);
      }
      break;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
