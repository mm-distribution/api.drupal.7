# list_allowed_values()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 235–260 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L235-L260)
- **Module/theme:** list

## Signature

```php
function list_allowed_values($field, $instance = NULL, $entity_type = NULL, $entity = NULL)
```

## Documentation

```text
Returns the array of allowed values for a list field.

The strings are not safe for output. Keys and values of the array should be
sanitized through field_filter_xss() before being displayed.

@param $field
  The field definition.
@param $instance
  (optional) A field instance array. Defaults to NULL.
@param $entity_type
  (optional) The type of entity; e.g. 'node' or 'user'. Defaults to NULL.
@param $entity
  (optional) The entity object. Defaults to NULL.

@return
  The array of allowed values. Keys of the array are the raw stored values
  (number or text), values of the array are the display labels.
```

## Code

```php
function list_allowed_values($field, $instance = NULL, $entity_type = NULL, $entity = NULL) {
  $allowed_values = &drupal_static(__FUNCTION__, array());

  if (!isset($allowed_values[$field['id']])) {
    $function = $field['settings']['allowed_values_function'];
    // If $cacheable is FALSE, then the allowed values are not statically
    // cached. See list_test_dynamic_values_callback() for an example of
    // generating dynamic and uncached values.
    $cacheable = TRUE;
    if (!empty($function) && function_exists($function)) {
      $values = $function($field, $instance, $entity_type, $entity, $cacheable);
    }
    else {
      $values = $field['settings']['allowed_values'];
    }

    if ($cacheable) {
      $allowed_values[$field['id']] = $values;
    }
    else {
      return $values;
    }
  }

  return $allowed_values[$field['id']];
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
