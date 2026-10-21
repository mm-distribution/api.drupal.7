# field_test_entity_save()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 282–321 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L282-L321)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_save(&$entity)
```

## Documentation

```text
Saves a test_entity.

A new entity is created if $entity->ftid and $entity->is_new are both empty.
A new revision is created if $entity->revision is not empty.

@param $entity
  The entity to save.
```

## Code

```php
function field_test_entity_save(&$entity) {
  field_attach_presave('test_entity', $entity);

  if (!isset($entity->is_new)) {
    $entity->is_new = empty($entity->ftid);
  }

  if (!$entity->is_new && !empty($entity->revision)) {
    $entity->old_ftvid = $entity->ftvid;
    unset($entity->ftvid);
  }

  $update_entity = TRUE;
  if ($entity->is_new) {
    drupal_write_record('test_entity', $entity);
    drupal_write_record('test_entity_revision', $entity);
    $op = 'insert';
  }
  else {
    drupal_write_record('test_entity', $entity, 'ftid');
    if (!empty($entity->revision)) {
      drupal_write_record('test_entity_revision', $entity);
    }
    else {
      drupal_write_record('test_entity_revision', $entity, 'ftvid');
      $update_entity = FALSE;
    }
    $op = 'update';
  }
  if ($update_entity) {
    db_update('test_entity')
      ->fields(array('ftvid' => $entity->ftvid))
      ->condition('ftid', $entity->ftid)
      ->execute();
  }

  // Save fields.
  $function = "field_attach_$op";
  $function('test_entity', $entity);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
