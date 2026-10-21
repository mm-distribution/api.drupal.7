# FieldTranslationsTestCase::testFieldInvoke()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3230–3263 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3230-L3263)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldInvoke()
```

## Documentation

```text
Test the multilanguage logic of _field_invoke().
```

## Code

```php
  function testFieldInvoke() {
    // Enable field translations for the entity.
    field_test_entity_info_translatable('test_entity', TRUE);

    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);

    // Populate some extra languages to check if _field_invoke() correctly uses
    // the result of field_available_languages().
    $values = array();
    $extra_languages = mt_rand(1, 4);
    $languages = $available_languages = field_available_languages($this->entity_type, $this->field);
    for ($i = 0; $i < $extra_languages; ++$i) {
      $languages[] = $this->randomName(2);
    }

    // For each given language provide some random values.
    foreach ($languages as $langcode) {
      for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
        $values[$langcode][$delta]['value'] = mt_rand(1, 127);
      }
    }
    $entity->{$this->field_name} = $values;

    $results = _field_invoke('test_op', $entity_type, $entity);
    foreach ($results as $langcode => $result) {
      $hash = hash('sha256', serialize(array($entity_type, $entity, $this->field_name, $langcode, $values[$langcode])));
      // Check whether the parameters passed to _field_invoke() were correctly
      // forwarded to the callback function.
      $this->assertEqual($hash, $result, format_string('The result for %language is correctly stored.', array('%language' => $langcode)));
    }

    $this->assertEqual(count($results), count($available_languages), 'No unavailable language has been processed.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
