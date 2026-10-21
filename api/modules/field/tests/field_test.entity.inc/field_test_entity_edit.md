# field_test_entity_edit()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 336–339 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L336-L339)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_edit($entity)
```

## Documentation

```text
Menu callback: displays the 'Edit exiisting test_entity' form.
```

## Code

```php
function field_test_entity_edit($entity) {
  drupal_set_title(t('test_entity @ftid revision @ftvid', array('@ftid' => $entity->ftid, '@ftvid' => $entity->ftvid)), PASS_THROUGH);
  return drupal_get_form('field_test_entity_form', $entity);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
