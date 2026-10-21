# field_test_entity_add()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 326–331 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L326-L331)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_add($fttype)
```

## Documentation

```text
Menu callback: displays the 'Add new test_entity' form.
```

## Code

```php
function field_test_entity_add($fttype) {
  $fttype = str_replace('-', '_', $fttype);
  $entity = (object)array('fttype' => $fttype);
  drupal_set_title(t('Create test_entity @bundle', array('@bundle' => $fttype)), PASS_THROUGH);
  return drupal_get_form('field_test_entity_form', $entity, TRUE);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
