# _field_invoke_multiple_default()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 397–400 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L397-L400)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function _field_invoke_multiple_default($op, $entity_type, $entities, &$a = NULL, &$b = NULL, $options = array())
```

## Documentation

```text
Invoke field.module's version of a field hook on multiple entities.

This function invokes the field_default_[op]() function.
Use _field_invoke_multiple() to invoke the field type implementation,
hook_field_[op]().

@see _field_invoke_multiple()
```

## Code

```php
function _field_invoke_multiple_default($op, $entity_type, $entities, &$a = NULL, &$b = NULL, $options = array()) {
  $options['default'] = TRUE;
  return _field_invoke_multiple($op, $entity_type, $entities, $a, $b, $options);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
