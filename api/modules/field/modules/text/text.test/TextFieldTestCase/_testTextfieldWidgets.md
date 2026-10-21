# TextFieldTestCase::_testTextfieldWidgets()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 87–133 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L87-L133)
- **Class:** [TextFieldTestCase](../TextFieldTestCase.md)
- **Module/theme:** text

## Signature

```php
function _testTextfieldWidgets($field_type, $widget_type)
```

## Documentation

```text
Helper function for testTextfieldWidgets().
```

## Code

```php
  function _testTextfieldWidgets($field_type, $widget_type) {
    // Setup a field and instance
    $entity_type = 'test_entity';
    $this->field_name = drupal_strtolower($this->randomName());
    $this->field = array('field_name' => $this->field_name, 'type' => $field_type);
    field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'label' => $this->randomName() . '_label',
      'settings' => array(
        'text_processing' => TRUE,
      ),
      'widget' => array(
        'type' => $widget_type,
      ),
      'display' => array(
        'full' => array(
          'type' => 'text_default',
        ),
      ),
    );
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Display creation form.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", '', 'Widget is displayed');
    $this->assertNoFieldByName("{$this->field_name}[$langcode][0][format]", '1', 'Format selector is not displayed');

    // Submit with some value.
    $value = $this->randomName();
    $edit = array(
      "{$this->field_name}[$langcode][0][value]" => $value,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created');

    // Display the entity.
    $entity = field_test_entity_test_load($id);
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $this->content = drupal_render($entity->content);
    $this->assertText($value, 'Filtered tags are not displayed');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
