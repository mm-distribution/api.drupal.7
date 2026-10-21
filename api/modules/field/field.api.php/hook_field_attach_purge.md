# hook_field_attach_purge()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1501–1506 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1501-L1506)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_purge($entity_type, $entity, $field, $instance)
```

## Documentation

```text
Act on field_purge_data().

This hook is invoked in field_purge_data() and allows modules to act on
purging data from a single field pseudo-entity. For example, if a module
relates data in the field with its own data, it may purge its own data
during this process as well.

@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The pseudo-entity whose field data is being purged.
@param $field
  The (possibly deleted) field whose data is being purged.
@param $instance
  The deleted field instance whose data is being purged.

@see @link field_purge Field API bulk data deletion @endlink
@see field_purge_data()
```

## Code

```php
function hook_field_attach_purge($entity_type, $entity, $field, $instance) {
  // find the corresponding data in mymodule and purge it
  if ($entity_type == 'node' && $field->field_name == 'my_field_name') {
    mymodule_remove_mydata($entity->nid);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_purge()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
