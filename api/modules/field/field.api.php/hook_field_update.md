# hook_field_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 541–566 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L541-L566)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_update($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Define custom update behavior for this module's field data.

This hook is invoked from field_attach_update() on the module that defines a
field, during the process of updating an entity object (node, taxonomy term,
etc.). It is invoked just before the data for this field on the particular
entity object is updated into field storage. Only field modules that are
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
@see hook_field_delete()
```

## Code

```php
function hook_field_update($entity_type, $entity, $field, $instance, $langcode, &$items) {
  if (variable_get('taxonomy_maintain_index_table', TRUE) && $field['storage']['type'] == 'field_sql_storage' && $entity_type == 'node') {
    $first_call = &drupal_static(__FUNCTION__, array());

    // We don't maintain data for old revisions, so clear all previous values
    // from the table. Since this hook runs once per field, per object, make
    // sure we only wipe values once.
    if (!isset($first_call[$entity->nid])) {
      $first_call[$entity->nid] = FALSE;
      db_delete('taxonomy_index')->condition('nid', $entity->nid)->execute();
    }
    // Only save data to the table if the node is published.
    if ($entity->status) {
      $query = db_insert('taxonomy_index')->fields(array('nid', 'tid', 'sticky', 'created'));
      foreach ($items as $item) {
        $query->values(array(
          'nid' => $entity->nid,
          'tid' => $item['tid'],
          'sticky' => $entity->sticky,
          'created' => $entity->created,
        ));
      }
      $query->execute();
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_update()".

- [field_test_field_update()](../tests/field_test.field.inc/field_test_field_update.md) — `modules/field/tests/field_test.field.inc`
- [file_field_update()](../../file/file.field.inc/file_field_update.md) — `modules/file/file.field.inc`
- [image_field_update()](../../image/image.field.inc/image_field_update.md) — `modules/image/image.field.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
