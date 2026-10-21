# hook_field_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 342–357 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L342-L357)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age)
```

## Documentation

```text
Define custom load behavior for this module's field types.

Unlike most other field hooks, this hook operates on multiple entities. The
$entities, $instances and $items parameters are arrays keyed by entity ID.
For performance reasons, information for all available entity should be
loaded in a single query where possible.

Note that the changes made to the field values get cached by the field cache
for subsequent loads. You should never use this hook to load fieldable
entities, since this is likely to cause infinite recursions when
hook_field_load() is run on those as well. Use
hook_field_formatter_prepare_view() instead.

Make changes or additions to field values by altering the $items parameter by
reference. There is no return value.

@param $entity_type
  The type of $entity.
@param $entities
  Array of entities being loaded, keyed by entity ID.
@param $field
  The field structure for the operation.
@param $instances
  Array of instance structures for $field for each entity, keyed by entity
  ID.
@param $langcode
  The language code associated with $items.
@param $items
  Array of field values already loaded for the entities, keyed by entity ID.
  Store your changes in this parameter (passed by reference).
@param $age
  FIELD_LOAD_CURRENT to load the most recent revision for all fields, or
  FIELD_LOAD_REVISION to load the version indicated by each entity.
```

## Code

```php
function hook_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age) {
  // Sample code from text.module: precompute sanitized strings so they are
  // stored in the field cache.
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

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_load()".

- [field_test_field_load()](../tests/field_test.field.inc/field_test_field_load.md) — `modules/field/tests/field_test.field.inc`
- [file_field_load()](../../file/file.field.inc/file_field_load.md) — `modules/file/file.field.inc`
- [image_field_load()](../../image/image.field.inc/image_field_load.md) — `modules/image/image.field.inc`
- [text_field_load()](../modules/text/text.module/text_field_load.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
