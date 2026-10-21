# element_info_property()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6679–6681 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6679-L6681)

## Signature

```php
function element_info_property($type, $property_name, $default = NULL)
```

## Documentation

```text
Retrieves a single property for the defined element type.

@param $type
  An element type as defined by hook_element_info().
@param $property_name
  The property within the element type that should be returned.
@param $default
  (Optional) The value to return if the element type does not specify a
  value for the property. Defaults to NULL.
```

## Code

```php
function element_info_property($type, $property_name, $default = NULL) {
  return (($info = element_info($type)) && array_key_exists($property_name, $info)) ? $info[$property_name] : $default;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
