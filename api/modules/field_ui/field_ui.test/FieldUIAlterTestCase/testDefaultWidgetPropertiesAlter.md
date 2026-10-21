# FieldUIAlterTestCase::testDefaultWidgetPropertiesAlter()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 715–769 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L715-L769)
- **Class:** [FieldUIAlterTestCase](../FieldUIAlterTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testDefaultWidgetPropertiesAlter()
```

## Documentation

```text
Tests hook_field_widget_properties_alter() on the default field widget.

@see field_test_field_widget_properties_alter()
@see field_test_field_widget_properties_user_alter()
@see field_test_field_widget_form_alter()
```

## Code

```php
  function testDefaultWidgetPropertiesAlter() {
    // Create the alter_test_text field and an instance on article nodes.
    field_create_field(array(
      'field_name' => 'alter_test_text',
      'type' => 'text',
    ));
    field_create_instance(array(
      'field_name' => 'alter_test_text',
      'entity_type' => 'node',
      'bundle' => 'article',
      'widget' => array(
        'type' => 'text_textfield',
        'size' => 60,
      ),
    ));

    // Test that field_test_field_widget_properties_alter() sets the size to
    // 42 and that field_test_field_widget_form_alter() reports the correct
    // size when the form is displayed.
    $this->drupalGet('admin/structure/types/manage/article/fields/alter_test_text');
    $this->assertText('Field size: 42', 'Altered field size is found in hook_field_widget_form_alter().');

    // Create the alter_test_options field.
    field_create_field(array(
      'field_name' => 'alter_test_options',
      'type' => 'list_text'
    ));
    // Create instances on users and page nodes.
    field_create_instance(array(
      'field_name' => 'alter_test_options',
      'entity_type' => 'user',
      'bundle' => 'user',
      'widget' => array(
        'type' => 'options_select',
      )
    ));
    field_create_instance(array(
      'field_name' => 'alter_test_options',
      'entity_type' => 'node',
      'bundle' => 'page',
      'widget' => array(
        'type' => 'options_select',
      )
    ));

    // Test that field_test_field_widget_properties_user_alter() replaces
    // the widget and that field_test_field_widget_form_alter() reports the
    // correct widget name when the form is displayed.
    $this->drupalGet('admin/config/people/accounts/fields/alter_test_options');
    $this->assertText('Widget type: options_buttons', 'Widget type is altered for users in hook_field_widget_form_alter().');

    // Test that the widget is not altered on page nodes.
    $this->drupalGet('admin/structure/types/manage/page/fields/alter_test_options');
    $this->assertText('Widget type: options_select', 'Widget type is not altered for pages in hook_field_widget_form_alter().');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
