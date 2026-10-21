# TaxonomyTermFieldTestCase::testEmptyTaxonomyTermReferenceField()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1691–1708 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1691-L1708)
- **Class:** [TaxonomyTermFieldTestCase](../TaxonomyTermFieldTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testEmptyTaxonomyTermReferenceField()
```

## Documentation

```text
Test empty taxonomy term reference field.
```

## Code

```php
  function testEmptyTaxonomyTermReferenceField() {
    // Test if an empty value in the taxonomy reference field would trigger
    // autocreate or if the value would be saved correctly.
    $langcode = LANGUAGE_NONE;
    $entity = field_test_create_stub_entity(NULL, NULL);
    $entity->{$this->field_name}[$langcode][0]['tid'] = 0;
    field_test_entity_save($entity);
    $entity = field_test_entity_test_load($entity->ftid);
    field_test_entity_save($entity);
    $this->pass('Empty term ID does not trigger autocreate.');

    // Try also NULL value.
    $entity->{$this->field_name}[$langcode][0]['tid'] = NULL;
    field_test_entity_save($entity);
    $this->pass('NULL term ID does not trigger autocreate.');
    field_attach_prepare_view('test_entity', array($entity->ftid => $entity), 'full');
    $this->pass('NULL term ID prepared to display.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
