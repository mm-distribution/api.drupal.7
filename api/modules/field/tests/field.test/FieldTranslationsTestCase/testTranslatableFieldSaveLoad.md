# FieldTranslationsTestCase::testTranslatableFieldSaveLoad()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3341–3373 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3341-L3373)
- **Class:** [FieldTranslationsTestCase](../FieldTranslationsTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testTranslatableFieldSaveLoad()
```

## Documentation

```text
Test translatable fields storage/retrieval.
```

## Code

```php
  function testTranslatableFieldSaveLoad() {
    // Enable field translations for nodes.
    field_test_entity_info_translatable('node', TRUE);
    $entity_info = entity_get_info('node');
    $this->assertTrue(count($entity_info['translation']), 'Nodes are translatable.');

    // Prepare the field translations.
    field_test_entity_info_translatable('test_entity', TRUE);
    $eid = $evid = 1;
    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity($eid, $evid, $this->instance['bundle']);
    $field_translations = array();
    $available_languages = field_available_languages($entity_type, $this->field);
    $this->assertTrue(count($available_languages) > 1, 'Field is translatable.');
    foreach ($available_languages as $langcode) {
      $field_translations[$langcode] = $this->_generateTestFieldValues($this->field['cardinality']);
    }

    // Save and reload the field translations.
    $entity->{$this->field_name} = $field_translations;
    field_attach_insert($entity_type, $entity);
    unset($entity->{$this->field_name});
    field_attach_load($entity_type, array($eid => $entity));

    // Check if the correct values were saved/loaded.
    foreach ($field_translations as $langcode => $items) {
      $result = TRUE;
      foreach ($items as $delta => $item) {
        $result = $result && $item['value'] == $entity->{$this->field_name}[$langcode][$delta]['value'];
      }
      $this->assertTrue($result, format_string('%language translation correctly handled.', array('%language' => $langcode)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
