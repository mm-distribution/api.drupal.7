# field_info_formatter_types()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 383–394 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L383-L394)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_formatter_types($formatter_type = NULL)
```

## Documentation

```text
Returns information about field formatters from hook_field_formatter_info().

@param $formatter_type
  (optional) A formatter type name. If omitted, all formatter types will be
  returned.

@return
  Either a single formatter type description, as provided by
  hook_field_formatter_info(), or an array of all existing formatter types,
  keyed by formatter type name.
```

## Code

```php
function field_info_formatter_types($formatter_type = NULL) {
  $info = _field_info_collate_types();
  $formatter_types = $info['formatter types'];
  if ($formatter_type) {
    if (isset($formatter_types[$formatter_type])) {
      return $formatter_types[$formatter_type];
    }
  }
  else {
    return $formatter_types;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
