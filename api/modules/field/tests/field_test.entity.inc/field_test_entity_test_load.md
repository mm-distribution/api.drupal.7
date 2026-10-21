# field_test_entity_test_load()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 244–271 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L244-L271)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_test_load($ftid, $ftvid = NULL)
```

## Documentation

```text
Loads a test_entity.

@param $ftid
  The id of the entity to load.
@param $ftvid
  (Optional) The revision id of the entity to load. If not specified, the
  current revision will be used.
@return
  The loaded entity.
```

## Code

```php
function field_test_entity_test_load($ftid, $ftvid = NULL) {
  // Load basic strucure.
  $query = db_select('test_entity', 'fte', array())
    ->condition('fte.ftid', $ftid);

  if ($ftvid) {
    $query->join('test_entity_revision', 'fter', 'fte.ftid = fter.ftid');
    $query->addField('fte', 'ftid');
    $query->addField('fte', 'fttype');
    $query->addField('fter', 'ftvid');
    $query->condition('fter.ftvid', $ftvid);
  }
  else {
    $query->fields('fte');
  }

  $entities = $query->execute()->fetchAllAssoc('ftid');

  // Attach fields.
  if ($ftvid) {
    field_attach_load_revision('test_entity', $entities);
  }
  else {
    field_attach_load('test_entity', $entities);
  }

  return $entities[$ftid];
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
