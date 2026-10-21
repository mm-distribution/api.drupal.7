# field_info_field_map()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 468–471 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L468-L471)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_field_map()
```

## Documentation

```text
Returns a lightweight map of fields across bundles.

The function only returns active, non deleted fields.

@return
  An array keyed by field name. Each value is an array with two entries:
  - type: The field type.
  - bundles: The bundles in which the field appears, as an array with entity
    types as keys and the array of bundle names as values.
Example:
@code
array(
  'body' => array(
    'bundles' => array(
      'node' => array('page', 'article'),
    ),
    'type' => 'text_with_summary',
  ),
);
@endcode
```

## Code

```php
function field_info_field_map() {
  $cache = _field_info_field_cache();
  return $cache->getFieldMap();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
