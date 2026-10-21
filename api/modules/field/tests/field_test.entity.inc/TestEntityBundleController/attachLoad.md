# TestEntityBundleController::attachLoad()

- **Type:** Method
- **File:** [`modules/field/tests/field_test.entity.inc`](../_file.md), lines 492–499 · [local source](../../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L492-L499)
- **Class:** [TestEntityBundleController](../TestEntityBundleController.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
protected function attachLoad(&$entities, $revision_id = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function attachLoad(&$entities, $revision_id = FALSE) {
    // Add bundle information.
    foreach ($entities as $key => $entity) {
      $entity->fttype = 'test_entity_bundle';
      $entities[$key] = $entity;
    }
    parent::attachLoad($entities, $revision_id);
  }
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
