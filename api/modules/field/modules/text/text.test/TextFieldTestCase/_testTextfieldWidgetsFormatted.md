# TextFieldTestCase::_testTextfieldWidgetsFormatted()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 146–239 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L146-L239)
- **Class:** [TextFieldTestCase](../TextFieldTestCase.md)
- **Module/theme:** text

## Signature

```php
function _testTextfieldWidgetsFormatted($field_type, $widget_type)
```

## Documentation

```text
Helper function for testTextfieldWidgetsFormatted().
```

## Code

```php
  function _testTextfieldWidgetsFormatted($field_type, $widget_type) {
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

    // Disable all text formats besides the plain text fallback format.
    $this->drupalLogin($this->admin_user);
    foreach (filter_formats() as $format) {
      if ($format->format != filter_fallback_format()) {
        $this->drupalPost('admin/config/content/formats/' . $format->format . '/disable', array(), t('Disable'));
      }
    }
    $this->drupalLogin($this->web_user);

    // Display the creation form. Since the user only has access to one format,
    // no format selector will be displayed.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", '', 'Widget is displayed');
    $this->assertNoFieldByName("{$this->field_name}[$langcode][0][format]", '', 'Format selector is not displayed');

    // Submit with data that should be filtered.
    $value = '<em>' . $this->randomName() . '</em>';
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
    $this->assertNoRaw($value, 'HTML tags are not displayed.');
    $this->assertRaw(check_plain($value), 'Escaped HTML is displayed correctly.');

    // Create a new text format that does not escape HTML, and grant the user
    // access to it.
    $this->drupalLogin($this->admin_user);
    $edit = array(
      'format' => drupal_strtolower($this->randomName()),
      'name' => $this->randomName(),
    );
    $this->drupalPost('admin/config/content/formats/add', $edit, t('Save configuration'));
    filter_formats_reset();
    $this->checkPermissions(array(), TRUE);
    $format = filter_format_load($edit['format']);
    $format_id = $format->format;
    $permission = filter_permission_name($format);
    $rid = max(array_keys($this->web_user->roles));
    user_role_grant_permissions($rid, array($permission));
    $this->drupalLogin($this->web_user);

    // Display edition form.
    // We should now have a 'text format' selector.
    $this->drupalGet('test-entity/manage/' . $id . '/edit');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", NULL, 'Widget is displayed');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][format]", NULL, 'Format selector is displayed');

    // Edit and change the text format to the new one that was created.
    $edit = array(
      "{$this->field_name}[$langcode][0][format]" => $format_id,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t('test_entity @id has been updated.', array('@id' => $id)), 'Entity was updated');

    // Display the entity.
    $entity = field_test_entity_test_load($id);
    $entity->content = field_attach_view($entity_type, $entity, 'full');
    $this->content = drupal_render($entity->content);
    $this->assertRaw($value, 'Value is displayed unfiltered');
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
