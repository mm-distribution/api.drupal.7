# text_field_formatter_view()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 259–295 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L259-L295)
- **Module/theme:** text
- **Implements:** [hook_field_formatter_view()](../../../field.api.php/hook_field_formatter_view.md)

## Signature

```php
function text_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Implements hook_field_formatter_view().
```

## Code

```php
function text_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();

  switch ($display['type']) {
    case 'text_default':
    case 'text_trimmed':
      foreach ($items as $delta => $item) {
        $output = _text_sanitize($instance, $langcode, $item, 'value');
        if ($display['type'] == 'text_trimmed') {
          $output = text_summary($output, $instance['settings']['text_processing'] ? $item['format'] : NULL, $display['settings']['trim_length']);
        }
        $element[$delta] = array('#markup' => $output);
      }
      break;

    case 'text_summary_or_trimmed':
      foreach ($items as $delta => $item) {
        if (!empty($item['summary'])) {
          $output = _text_sanitize($instance, $langcode, $item, 'summary');
        }
        else {
          $output = _text_sanitize($instance, $langcode, $item, 'value');
          $output = text_summary($output, $instance['settings']['text_processing'] ? $item['format'] : NULL, $display['settings']['trim_length']);
        }
        $element[$delta] = array('#markup' => $output);
      }
      break;

    case 'text_plain':
      foreach ($items as $delta => $item) {
        $element[$delta] = array('#markup' => strip_tags($item['value']));
      }
      break;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
