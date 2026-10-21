# FieldTranslationsTestCase::testFieldInvokeMultiple()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3268–3336 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3268-L3336)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldInvokeMultiple()
```

## Documentation

```text
Test the multilanguage logic of _field_invoke_multiple().
```

## Code

```php
  function testFieldInvokeMultiple() {
    // Enable field translations for the entity.
    field_test_entity_info_translatable('test_entity', TRUE);

    $values = array();
    $options = array();
    $entities = array();
    $entity_type = 'test_entity';
    $entity_count = 5;
    $available_languages = field_available_languages($this->entity_type, $this->field);

    for ($id = 1; $id <= $entity_count; ++$id) {
      $entity = field_test_create_stub_entity($id, $id, $this->instance['bundle']);
      $languages = $available_languages;

      // Populate some extra languages to check whether _field_invoke()
      // correctly uses the result of field_available_languages().
      $extra_languages = mt_rand(1, 4);
      for ($i = 0; $i < $extra_languages; ++$i) {
        $languages[] = $this->randomName(2);
      }

      // For each given language provide some random values.
      $language_count = count($languages);
      for ($i = 0; $i < $language_count; ++$i) {
        $langcode = $languages[$i];
        // Avoid to populate at least one field translation to check that
        // per-entity language suggestions work even when available field values
        // are different for each language.
        if ($i !== $id) {
          for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
            $values[$id][$langcode][$delta]['value'] = mt_rand(1, 127);
          }
        }
        // Ensure that a language for which there is no field translation is
        // used as display language to prepare per-entity language suggestions.
        elseif (!isset($display_language)) {
          $display_language = $langcode;
        }
      }

      $entity->{$this->field_name} = $values[$id];
      $entities[$id] = $entity;

      // Store per-entity language suggestions.
      $options['language'][$id] = field_language($entity_type, $entity, NULL, $display_language);
    }

    $grouped_results = _field_invoke_multiple('test_op_multiple', $entity_type, $entities);
    foreach ($grouped_results as $id => $results) {
      foreach ($results as $langcode => $result) {
        if (isset($values[$id][$langcode])) {
          $hash = hash('sha256', serialize(array($entity_type, $entities[$id], $this->field_name, $langcode, $values[$id][$langcode])));
          // Check whether the parameters passed to _field_invoke_multiple()
          // were correctly forwarded to the callback function.
          $this->assertEqual($hash, $result, format_string('The result for entity %id/%language is correctly stored.', array('%id' => $id, '%language' => $langcode)));
        }
      }
      $this->assertEqual(count($results), count($available_languages), format_string('No unavailable language has been processed for entity %id.', array('%id' => $id)));
    }

    $null = NULL;
    $grouped_results = _field_invoke_multiple('test_op_multiple', $entity_type, $entities, $null, $null, $options);
    foreach ($grouped_results as $id => $results) {
      foreach ($results as $langcode => $result) {
        $this->assertTrue(isset($options['language'][$id]), format_string('The result language %language for entity %id was correctly suggested (display language: %display_language).', array('%id' => $id, '%language' => $langcode, '%display_language' => $display_language)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
