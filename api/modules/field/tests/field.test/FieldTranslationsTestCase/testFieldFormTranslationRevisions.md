# FieldTranslationsTestCase::testFieldFormTranslationRevisions()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3460–3487 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3460-L3487)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormTranslationRevisions()
```

## Documentation

```text
Tests field translations when creating a new revision.
```

## Code

```php
  function testFieldFormTranslationRevisions() {
    $web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content'));
    $this->drupalLogin($web_user);

    // Prepare the field translations.
    field_test_entity_info_translatable($this->entity_type, TRUE);
    $eid = 1;
    $entity = field_test_create_stub_entity($eid, $eid, $this->instance['bundle']);
    $available_languages = array_flip(field_available_languages($this->entity_type, $this->field));
    unset($available_languages[LANGUAGE_NONE]);
    $field_name = $this->field['field_name'];

    // Store the field translations.
    $entity->is_new = TRUE;
    foreach ($available_languages as $langcode => $value) {
      $entity->{$field_name}[$langcode][0]['value'] = $value + 1;
    }
    field_test_entity_save($entity);

    // Create a new revision.
    $langcode = field_valid_language(NULL);
    $edit = array("{$field_name}[$langcode][0][value]" => $entity->{$field_name}[$langcode][0]['value'], 'revision' => TRUE);
    $this->drupalPost('test-entity/manage/' . $eid . '/edit', $edit, t('Save'));

    // Check translation revisions.
    $this->checkTranslationRevisions($eid, $eid, $available_languages);
    $this->checkTranslationRevisions($eid, $eid + 1, $available_languages);
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
