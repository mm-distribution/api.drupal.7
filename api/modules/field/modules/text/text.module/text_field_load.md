# text_field_load()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 153–166 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L153-L166)
- **Module/theme:** text
- **Implements:** [hook_field_load()](../../../field.api.php/hook_field_load.md)

## Signature

```php
function text_field_load($entity_type, $entities, $field, $instances, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_load().

Where possible, generate the sanitized version of each field early so that
it is cached in the field cache. This avoids looking up from the filter cache
separately.

@see text_field_formatter_view()
```

## Code

```php
function text_field_load($entity_type, $entities, $field, $instances, $langcode, &$items) {
  foreach ($entities as $id => $entity) {
    foreach ($items[$id] as $delta => $item) {
      // Only process items with a cacheable format, the rest will be handled
      // by formatters if needed.
      if (empty($instances[$id]['settings']['text_processing']) || filter_format_allowcache($item['format'])) {
        $items[$id][$delta]['safe_value'] = isset($item['value']) ? _text_sanitize($instances[$id], $langcode, $item, 'value') : '';
        if ($field['type'] == 'text_with_summary') {
          $items[$id][$delta]['safe_summary'] = isset($item['summary']) ? _text_sanitize($instances[$id], $langcode, $item, 'summary') : '';
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
