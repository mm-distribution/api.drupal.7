# field_read_instance()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 707–710 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L707-L710)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_read_instance($entity_type, $field_name, $bundle, $include_additional = array())
```

## Documentation

```text
Reads a single instance record from the database.

Generally, you should use field_info_instance() instead, as it
provides caching and allows other modules the opportunity to
append additional formatters, widgets, and other information.

@param $entity_type
  The type of entity to which the field is bound.
@param $field_name
  The field name to read.
@param $bundle
  The bundle to which the field is bound.
@param array $include_additional
  The default behavior of this function is to not return an instance that
  has been deleted, or whose field is inactive. Setting
  $include_additional['include_inactive'] or
  $include_additional['include_deleted'] to TRUE will override this
  behavior.
@return
  An instance structure, or FALSE.
```

## Code

```php
function field_read_instance($entity_type, $field_name, $bundle, $include_additional = array()) {
  $instances = field_read_instances(array('entity_type' => $entity_type, 'field_name' => $field_name, 'bundle' => $bundle), $include_additional);
  return $instances ? current($instances) : FALSE;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
