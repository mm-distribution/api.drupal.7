# TaxonomyTermFieldTestCase::testTaxonomyTermFieldValidation()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1587–1611 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1587-L1611)
- **Class:** [TaxonomyTermFieldTestCase](../TaxonomyTermFieldTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermFieldValidation()
```

## Documentation

```text
Test term field validation.
```

## Code

```php
  function testTaxonomyTermFieldValidation() {
    // Test valid and invalid values with field_attach_validate().
    $langcode = LANGUAGE_NONE;
    $entity = field_test_create_stub_entity();
    $term = $this->createTerm($this->vocabulary);
    $entity->{$this->field_name}[$langcode][0]['tid'] = $term->tid;
    try {
      field_attach_validate('test_entity', $entity);
      $this->pass('Correct term does not cause validation error.');
    }
    catch (FieldValidationException $e) {
      $this->fail('Correct term does not cause validation error.');
    }

    $entity = field_test_create_stub_entity();
    $bad_term = $this->createTerm($this->createVocabulary());
    $entity->{$this->field_name}[$langcode][0]['tid'] = $bad_term->tid;
    try {
      field_attach_validate('test_entity', $entity);
      $this->fail('Wrong term causes validation error.');
    }
    catch (FieldValidationException $e) {
      $this->pass('Wrong term causes validation error.');
    }
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
