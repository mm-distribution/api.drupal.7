# FieldTranslationsTestCase::checkTranslationRevisions()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3493–3500 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3493-L3500)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
private function checkTranslationRevisions($eid, $evid, $available_languages)
```

## Documentation

```text
Check if the field translation attached to the entity revision identified
by the passed arguments were correctly stored.
```

## Code

```php
  private function checkTranslationRevisions($eid, $evid, $available_languages) {
    $field_name = $this->field['field_name'];
    $entity = field_test_entity_test_load($eid, $evid);
    foreach ($available_languages as $langcode => $value) {
      $passed = isset($entity->{$field_name}[$langcode]) && $entity->{$field_name}[$langcode][0]['value'] == $value + 1;
      $this->assertTrue($passed, format_string('The @language translation for revision @revision was correctly stored', array('@language' => $langcode, '@revision' => $entity->ftvid)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
