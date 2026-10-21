# EntityFieldQueryTestCase::testEntityFieldQueryTranslatable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1083–1116 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1083-L1116)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryTranslatable()
```

## Documentation

```text
Tests querying translatable fields.
```

## Code

```php
  function testEntityFieldQueryTranslatable() {

    // Make a test field translatable AND cardinality one.
    $this->fields[0]['translatable'] = TRUE;
    $this->fields[0]['cardinality'] = 1;
    field_update_field($this->fields[0]);
    field_test_entity_info_translatable('test_entity', TRUE);

    // Create more items with different languages.
    $entity = new stdClass();
    $entity->ftid = 1;
    $entity->ftvid = 1;
    $entity->fttype = 'test_bundle';

    // Set fields in two languages with one field value.
    foreach (array(LANGUAGE_NONE, 'en') as $langcode) {
      $entity->{$this->field_names[0]}[$langcode][0]['value'] = 1234;
    }

    field_attach_update('test_entity', $entity);

    // Look up number of results when querying a single entity with multilingual
    // field values.
    $query = new EntityFieldQuery();
    $query_count = $query
      ->entityCondition('entity_type', 'test_entity')
      ->entityCondition('bundle', 'test_bundle')
      ->entityCondition('entity_id', '1')
      ->fieldCondition($this->fields[0])
      ->count()
      ->execute();

    $this->assertEqual($query_count, 1, "Count on translatable cardinality one field is correct.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
