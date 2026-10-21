# hook_field_storage_pre_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2257–2275 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2257-L2275)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_pre_insert($entity_type, $entity, &$skip_fields)
```

## Documentation

```text
Act before the storage backends insert field data.

This hook allows modules to store data before the Field Storage API,
optionally preventing the field storage module from doing so.

@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The entity with fields to save.
@param $skip_fields
  An array keyed by field IDs whose data has already been written and
  therefore should not be written again. The values associated with these
  keys are not specified.
@return
  Saved field IDs are set set as keys in $skip_fields.
```

## Code

```php
function hook_field_storage_pre_insert($entity_type, $entity, &$skip_fields) {
  if ($entity_type == 'node' && $entity->status && _forum_node_check_node_type($entity)) {
    $query = db_insert('forum_index')->fields(array('nid', 'title', 'tid', 'sticky', 'created', 'comment_count', 'last_comment_timestamp'));
    foreach ($entity->taxonomy_forums as $language) {
      foreach ($language as $delta) {
        $query->values(array(
          'nid' => $entity->nid,
          'title' => $entity->title,
          'tid' => $delta['value'],
          'sticky' => $entity->sticky,
          'created' => $entity->created,
          'comment_count' => 0,
          'last_comment_timestamp' => $entity->created,
        ));
      }
    }
    $query->execute();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_pre_insert()".

- [forum_field_storage_pre_insert()](../../forum/forum.module/forum_field_storage_pre_insert.md) — `modules/forum/forum.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
