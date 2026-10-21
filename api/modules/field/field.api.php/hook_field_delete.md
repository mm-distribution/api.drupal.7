# hook_field_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 630–641 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L630-L641)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_delete($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Define custom delete behavior for this module's field data.

This hook is invoked from field_attach_delete() on the module that defines a
field, during the process of deleting an entity object (node, taxonomy term,
etc.). It is invoked just before the data for this field on the particular
entity object is deleted from field storage. Only field modules that are
storing or tracking information outside the standard field storage mechanism
need to implement this hook.

@param $entity_type
  The type of $entity.
@param $entity
  The entity for the operation.
@param $field
  The field structure for the operation.
@param $instance
  The instance structure for $field on $entity's bundle.
@param $langcode
  The language associated with $items.
@param $items
  $entity->{$field['field_name']}[$langcode], or an empty array if unset.

@see hook_field_insert()
@see hook_field_update()
```

## Code

```php
function hook_field_delete($entity_type, $entity, $field, $instance, $langcode, &$items) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
  foreach ($items as $delta => $item) {
    // For hook_file_references(), remember that this is being deleted.
    $item['file_field_name'] = $field['field_name'];
    // Pass in the ID of the object that is being removed so all references can
    // be counted in hook_file_references().
    $item['file_field_type'] = $entity_type;
    $item['file_field_id'] = $id;
    file_field_delete_file($item, $field, $entity_type, $id);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_delete()".

- [field_test_field_delete()](../tests/field_test.field.inc/field_test_field_delete.md) — `modules/field/tests/field_test.field.inc`
- [file_field_delete()](../../file/file.field.inc/file_field_delete.md) — `modules/file/file.field.inc`
- [image_field_delete()](../../image/image.field.inc/image_field_delete.md) — `modules/image/image.field.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
