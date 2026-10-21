# FieldTranslationsTestCase::testFieldDisplayLanguage()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3378–3455 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3378-L3455)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldDisplayLanguage()
```

## Documentation

```text
Tests display language logic for translatable fields.
```

## Code

```php
  function testFieldDisplayLanguage() {
    $field_name = drupal_strtolower($this->randomName() . '_field_name');
    $entity_type = 'test_entity';

    // We need an additional field here to properly test display language
    // suggestions.
    $field = array(
      'field_name' => $field_name,
      'type' => 'test_field',
      'cardinality' => 2,
      'translatable' => TRUE,
    );
    field_create_field($field);

    $instance = array(
      'field_name' => $field['field_name'],
      'entity_type' => $entity_type,
      'bundle' => 'test_bundle',
    );
    field_create_instance($instance);

    $entity = field_test_create_stub_entity(1, 1, $this->instance['bundle']);
    $instances = field_info_instances($entity_type, $this->instance['bundle']);

    $enabled_languages = field_content_languages();
    $languages = array();

    // Generate field translations for languages different from the first
    // enabled.
    foreach ($instances as $instance) {
      $field_name = $instance['field_name'];
      $field = field_info_field($field_name);
      do {
        // Index 0 is reserved for the requested language, this way we ensure
        // that no field is actually populated with it.
        $langcode = $enabled_languages[mt_rand(1, count($enabled_languages) - 1)];
      }
      while (isset($languages[$langcode]));
      $languages[$langcode] = TRUE;
      $entity->{$field_name}[$langcode] = $this->_generateTestFieldValues($field['cardinality']);
    }

    // Test multiple-fields display languages for untranslatable entities.
    field_test_entity_info_translatable($entity_type, FALSE);
    drupal_static_reset('field_language');
    $requested_language = $enabled_languages[0];
    $display_language = field_language($entity_type, $entity, NULL, $requested_language);
    foreach ($instances as $instance) {
      $field_name = $instance['field_name'];
      $this->assertTrue($display_language[$field_name] == LANGUAGE_NONE, format_string('The display language for field %field_name is %language.', array('%field_name' => $field_name, '%language' => LANGUAGE_NONE)));
    }

    // Test multiple-fields display languages for translatable entities.
    field_test_entity_info_translatable($entity_type, TRUE);
    drupal_static_reset('field_language');
    $display_language = field_language($entity_type, $entity, NULL, $requested_language);

    foreach ($instances as $instance) {
      $field_name = $instance['field_name'];
      $langcode = $display_language[$field_name];
      // As the requested language was not assinged to any field, if the
      // returned language is defined for the current field, core fallback rules
      // were successfully applied.
      $this->assertTrue(isset($entity->{$field_name}[$langcode]) && $langcode != $requested_language, format_string('The display language for the field %field_name is %language.', array('%field_name' => $field_name, '%language' => $langcode)));
    }

    // Test single-field display language.
    drupal_static_reset('field_language');
    $langcode = field_language($entity_type, $entity, $this->field_name, $requested_language);
    $this->assertTrue(isset($entity->{$this->field_name}[$langcode]) && $langcode != $requested_language, format_string('The display language for the (single) field %field_name is %language.', array('%field_name' => $field_name, '%language' => $langcode)));

    // Test field_language() basic behavior without language fallback.
    variable_set('field_test_language_fallback', FALSE);
    $entity->{$this->field_name}[$requested_language] = mt_rand(1, 127);
    drupal_static_reset('field_language');
    $display_language = field_language($entity_type, $entity, $this->field_name, $requested_language);
    $this->assertEqual($display_language, $requested_language, 'Display language behave correctly when language fallback is disabled');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
