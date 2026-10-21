# FieldTranslationsTestCase::testFieldAvailableLanguages()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3199–3225 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3199-L3225)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAvailableLanguages()
```

## Documentation

```text
Ensures that only valid values are returned by field_available_languages().
```

## Code

```php
  function testFieldAvailableLanguages() {
    // Test 'translatable' fieldable info.
    field_test_entity_info_translatable('test_entity', FALSE);
    $field = $this->field;
    $field['field_name'] .= '_untranslatable';

    // Enable field translations for the entity.
    field_test_entity_info_translatable('test_entity', TRUE);

    // Test hook_field_languages() invocation on a translatable field.
    variable_set('field_test_field_available_languages_alter', TRUE);
    $enabled_languages = field_content_languages();
    $available_languages = field_available_languages($this->entity_type, $this->field);
    foreach ($available_languages as $delta => $langcode) {
      if ($langcode != 'xx' && $langcode != 'en') {
        $this->assertTrue(in_array($langcode, $enabled_languages), format_string('%language is an enabled language.', array('%language' => $langcode)));
      }
    }
    $this->assertTrue(in_array('xx', $available_languages), format_string('%language was made available.', array('%language' => 'xx')));
    $this->assertFalse(in_array('en', $available_languages), format_string('%language was made unavailable.', array('%language' => 'en')));

    // Test field_available_languages() behavior for untranslatable fields.
    $this->field['translatable'] = FALSE;
    field_update_field($this->field);
    $available_languages = field_available_languages($this->entity_type, $this->field);
    $this->assertTrue(count($available_languages) == 1 && $available_languages[0] === LANGUAGE_NONE, 'For untranslatable fields only LANGUAGE_NONE is available.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
