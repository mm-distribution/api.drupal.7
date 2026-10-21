# _field_info_field_cache()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 14–32 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L14-L32)
- **Module/theme:** field

## Signature

```php
function _field_info_field_cache()
```

## Documentation

```text
Retrieves the FieldInfo object for the current request.

@return FieldInfo
  An instance of the FieldInfo class.
```

## Code

```php
function _field_info_field_cache() {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;

  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['field_info_field_cache'] = &drupal_static(__FUNCTION__);
  }
  $field_info = &$drupal_static_fast['field_info_field_cache'];

  if (!isset($field_info)) {
    // @todo The registry should save the need for an explicit include, but not
    // a couple upgrade tests (DisabledNodeTypeTestCase,
    // FilterFormatUpgradePathTestCase...) break in a strange way without it.
    include_once dirname(__FILE__) . '/field.info.class.inc';
    $field_info = new FieldInfo();
  }

  return $field_info;
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
