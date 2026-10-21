# EntityFieldQueryTestCase::testEntityFieldQueryMetaConditions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1121–1303 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1121-L1303)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryMetaConditions()
```

## Documentation

```text
Tests field meta conditions.
```

## Code

```php
  function testEntityFieldQueryMetaConditions() {
    // Make a test field translatable.
    $this->fields[0]['translatable'] = TRUE;
    field_update_field($this->fields[0]);
    field_test_entity_info_translatable('test_entity', TRUE);

    // Create more items with different languages.
    $entity = new stdClass();
    $entity->ftid = 1;
    $entity->ftvid = 1;
    $entity->fttype = 'test_bundle';
    $j = 0;

    foreach (array(LANGUAGE_NONE, 'en') as $langcode) {
      for ($i = 0; $i < 4; $i++) {
        $entity->{$this->field_names[0]}[$langcode][$i]['value'] = $i + $j;
      }
      $j += 4;
    }

    field_attach_update('test_entity', $entity);

    // Test delta field meta condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldDeltaCondition($this->fields[0], 0, '>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a delta meta condition.');

    // Test language field meta condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '<>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a language meta condition.');

    // Test language field meta condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '!=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a language meta condition.');

    // Test delta grouping.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'group')
      ->fieldDeltaCondition($this->fields[0], 1, '<', 'group');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a grouped delta meta condition.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'group')
      ->fieldDeltaCondition($this->fields[0], 1, '>=', 'group');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta meta condition (empty result set).');

    // Test language grouping.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', NULL, 'group')
      ->fieldLanguageCondition($this->fields[0], 'en', '<>', NULL, 'group');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a grouped language meta condition.');

    // Test language grouping.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', NULL, 'group')
      ->fieldLanguageCondition($this->fields[0], 'en', '!=', NULL, 'group');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a grouped language meta condition.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', NULL, 'group')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '<>', NULL, 'group');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped language meta condition (empty result set).');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', NULL, 'group')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '!=', NULL, 'group');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped language meta condition (empty result set).');

    // Test delta and language grouping.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '<', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], 'en', '<>', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a grouped delta + language meta condition.');

    // Test delta and language grouping.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '<', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], 'en', '!=', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
    ), 'Test with a grouped delta + language meta condition.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '>=', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], 'en', '<>', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta + language meta condition (empty result set, delta condition unsatisifed).');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '>=', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], 'en', '!=', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta + language meta condition (empty result set, delta condition unsatisifed).');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '<', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '<>', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta + language meta condition (empty result set, language condition unsatisifed).');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '<', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '!=', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta + language meta condition (empty result set, language condition unsatisifed).');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '>=', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '<>', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta + language meta condition (empty result set, both conditions unsatisifed).');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity', '=')
      ->fieldCondition($this->fields[0], 'value', 0, '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[0], 1, '>=', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[0], LANGUAGE_NONE, '!=', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(), 'Test with a grouped delta + language meta condition (empty result set, both conditions unsatisifed).');

    // Test grouping with another field to ensure that grouping cache is reset
    // properly.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle', '=')
      ->fieldCondition($this->fields[1], 'shape', 'circle', '=', 'delta', 'language')
      ->fieldCondition($this->fields[1], 'color', 'blue', '=', 'delta', 'language')
      ->fieldDeltaCondition($this->fields[1], 1, '=', 'delta', 'language')
      ->fieldLanguageCondition($this->fields[1], LANGUAGE_NONE, '=', 'delta', 'language');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle', 5),
    ), 'Test grouping cache.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
