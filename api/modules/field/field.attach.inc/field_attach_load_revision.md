# field_attach_load_revision()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 757–759 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L757-L759)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_load_revision($entity_type, $entities, $options = array())
```

## Documentation

```text
Load all fields for previous versions of a group of entities.

Loading different versions of the same entities is not supported, and should
be done by separate calls to the function.

field_attach_load_revision() is automatically called by the default entity
controller class, and thus, in most cases, doesn't need to be explicitly
called by the entity type module.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entities
  An array of entities for which to load fields, keyed by entity ID. Each
  entity needs to have its 'bundle', 'id' and (if applicable) 'revision'
  keys filled. The function adds the loaded field data directly in the
  entity objects of the $entities array.
@param $options
  An associative array of additional options. See field_attach_load() for
  details.
```

## Code

```php
function field_attach_load_revision($entity_type, $entities, $options = array()) {
  return field_attach_load($entity_type, $entities, FIELD_LOAD_REVISION, $options);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
