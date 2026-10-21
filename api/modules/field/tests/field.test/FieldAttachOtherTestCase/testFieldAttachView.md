# FieldAttachOtherTestCase::testFieldAttachView()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 730–887 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L730-L887)
- **Class:** [FieldAttachOtherTestCase](../FieldAttachOtherTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachView()
```

## Documentation

```text
Test field_attach_view() and field_attach_prepare_view().
```

## Code

```php
  function testFieldAttachView() {
    $this->createFieldWithInstance('_2');

    $entity_type = 'test_entity';
    $entity_init = field_test_create_stub_entity();
    $langcode = LANGUAGE_NONE;
    $options = array('field_name' => $this->field_name_2);

    // Populate values to be displayed.
    $values = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity_init->{$this->field_name}[$langcode] = $values;
    $values_2 = $this->_generateTestFieldValues($this->field_2['cardinality']);
    $entity_init->{$this->field_name_2}[$langcode] = $values_2;

    // Simple formatter, label displayed.
    $entity = clone($entity_init);
    $formatter_setting = $this->randomName();
    $this->instance['display'] = array(
      'full' => array(
        'label' => 'above',
        'type' => 'field_test_default',
        'settings' => array(
          'test_formatter_setting' => $formatter_setting,
        )
      ),
    );
    field_update_instance($this->instance);
    $formatter_setting_2 = $this->randomName();
    $this->instance_2['display'] = array(
      'full' => array(
        'label' => 'above',
        'type' => 'field_test_default',
        'settings' => array(
          'test_formatter_setting' => $formatter_setting_2,
        )
      ),
    );
    field_update_instance($this->instance_2);
    // View all fields.
    field_attach_prepare_view($entity_type, array($entity->ftid => $entity), 'full');
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $output = drupal_render($entity->content);
    $this->content = $output;
    $this->assertRaw($this->instance['label'], "First field's label is displayed.");
    foreach ($values as $delta => $value) {
      $this->content = $output;
      $this->assertRaw("$formatter_setting|{$value['value']}", "Value $delta is displayed, formatter settings are applied.");
    }
    $this->assertRaw($this->instance_2['label'], "Second field's label is displayed.");
    foreach ($values_2 as $delta => $value) {
      $this->content = $output;
      $this->assertRaw("$formatter_setting_2|{$value['value']}", "Value $delta is displayed, formatter settings are applied.");
    }
    // View single field (the second field).
    field_attach_prepare_view($entity_type, array($entity->ftid => $entity), 'full', $langcode, $options);
    $entity->content = field_attach_view($entity_type, $entity, 'full', $langcode, $options);
    $output = drupal_render($entity->content);
    $this->content = $output;
    $this->assertNoRaw($this->instance['label'], "First field's label is not displayed.");
    foreach ($values as $delta => $value) {
      $this->content = $output;
      $this->assertNoRaw("$formatter_setting|{$value['value']}", "Value $delta is displayed, formatter settings are applied.");
    }
    $this->assertRaw($this->instance_2['label'], "Second field's label is displayed.");
    foreach ($values_2 as $delta => $value) {
      $this->content = $output;
      $this->assertRaw("$formatter_setting_2|{$value['value']}", "Value $delta is displayed, formatter settings are applied.");
    }

    // Label hidden.
    $entity = clone($entity_init);
    $this->instance['display']['full']['label'] = 'hidden';
    field_update_instance($this->instance);
    field_attach_prepare_view($entity_type, array($entity->ftid => $entity), 'full');
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $output = drupal_render($entity->content);
    $this->content = $output;
    $this->assertNoRaw($this->instance['label'], "Hidden label: label is not displayed.");

    // Field hidden.
    $entity = clone($entity_init);
    $this->instance['display'] = array(
      'full' => array(
        'label' => 'above',
        'type' => 'hidden',
      ),
    );
    field_update_instance($this->instance);
    field_attach_prepare_view($entity_type, array($entity->ftid => $entity), 'full');
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $output = drupal_render($entity->content);
    $this->content = $output;
    $this->assertNoRaw($this->instance['label'], "Hidden field: label is not displayed.");
    foreach ($values as $delta => $value) {
      $this->assertNoRaw("$formatter_setting|{$value['value']}", "Hidden field: value $delta is not displayed.");
    }

    // Multiple formatter.
    $entity = clone($entity_init);
    $formatter_setting = $this->randomName();
    $this->instance['display'] = array(
      'full' => array(
        'label' => 'above',
        'type' => 'field_test_multiple',
        'settings' => array(
          'test_formatter_setting_multiple' => $formatter_setting,
        )
      ),
    );
    field_update_instance($this->instance);
    field_attach_prepare_view($entity_type, array($entity->ftid => $entity), 'full');
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $output = drupal_render($entity->content);
    $display = $formatter_setting;
    foreach ($values as $delta => $value) {
      $display .= "|$delta:{$value['value']}";
    }
    $this->content = $output;
    $this->assertRaw($display, "Multiple formatter: all values are displayed, formatter settings are applied.");

    // Test a formatter that uses hook_field_formatter_prepare_view().
    $entity = clone($entity_init);
    $formatter_setting = $this->randomName();
    $this->instance['display'] = array(
      'full' => array(
        'label' => 'above',
        'type' => 'field_test_with_prepare_view',
        'settings' => array(
          'test_formatter_setting_additional' => $formatter_setting,
        )
      ),
    );
    field_update_instance($this->instance);
    field_attach_prepare_view($entity_type, array($entity->ftid => $entity), 'full');
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $output = drupal_render($entity->content);
    $this->content = $output;
    foreach ($values as $delta => $value) {
      $this->content = $output;
      $expected = $formatter_setting . '|' . $value['value'] . '|' . ($value['value'] + 1);
      $this->assertRaw($expected, "Value $delta is displayed, formatter settings are applied.");
    }

    // TODO:
    // - check display order with several fields

    // Preprocess template.
    $variables = array();
    field_attach_preprocess($entity_type, $entity, $entity->content, $variables);
    $result = TRUE;
    foreach ($values as $delta => $item) {
      if ($variables[$this->field_name][$delta]['value'] !== $item['value']) {
        $result = FALSE;
        break;
      }
    }
    $this->assertTrue($result, format_string('Variable $@field_name correctly populated.', array('@field_name' => $this->field_name)));
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
