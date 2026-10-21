# FieldUIManageFieldsTestCase::testDuplicateFieldName()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 439–453 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L439-L453)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testDuplicateFieldName()
```

## Documentation

```text
Tests that a duplicate field name is caught by validation.
```

## Code

```php
  function testDuplicateFieldName() {
    // field_tags already exists, so we're expecting an error when trying to
    // create a new field with the same name.
    $edit = array(
      'fields[_add_new_field][field_name]' => 'tags',
      'fields[_add_new_field][label]' => $this->randomName(),
      'fields[_add_new_field][type]' => 'taxonomy_term_reference',
      'fields[_add_new_field][widget_type]' => 'options_select',
    );
    $url = 'admin/structure/types/manage/' . $this->hyphen_type . '/fields';
    $this->drupalPost($url, $edit, t('Save'));

    $this->assertText(t('The machine-readable name is already in use. It must be unique.'));
    $this->assertUrl($url, array(), 'Stayed on the same page.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
