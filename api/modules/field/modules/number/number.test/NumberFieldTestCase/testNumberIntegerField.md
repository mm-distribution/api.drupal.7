# NumberFieldTestCase::testNumberIntegerField()

- **Type:** Method
- **File:** [`modules/field/modules/number/number.test`](../_file.md), lines 122–154 · [local source](../../../../../../../source/modules/field/modules/number/number.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test#L122-L154)
- **Class:** [NumberFieldTestCase](../NumberFieldTestCase.md)
- **Module/theme:** number

## Signature

```php
function testNumberIntegerField()
```

## Documentation

```text
Test number_integer field.
```

## Code

```php
  function testNumberIntegerField() {
    // Display the "Add content type" form.
    $this->drupalGet('admin/structure/types/add');

    // Add a content type.
    $name = $this->randomName();
    $type = drupal_strtolower($name);
    $edit = array('name' => $name, 'type' => $type);
    $this->drupalPost(NULL, $edit, t('Save and add fields'));

    // Add an integer field to the newly-created type.
    $label = $this->randomName();
    $field_name = drupal_strtolower($label);
    $edit = array(
      'fields[_add_new_field][label]'=> $label,
      'fields[_add_new_field][field_name]' => $field_name,
      'fields[_add_new_field][type]' => 'number_integer',
      'fields[_add_new_field][widget_type]' => 'number',
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    // Set the formatter to "number_integer" and to "unformatted", and just
    // check that the settings summary does not generate warnings.
    $this->drupalGet("admin/structure/types/manage/$type/display");
    $edit = array(
      "fields[field_$field_name][type]" => 'number_integer',
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $edit = array(
      "fields[field_$field_name][type]" => 'number_unformatted',
    );
    $this->drupalPost(NULL, $edit, t('Save'));
  }
```

---
_Drupal 7.103 · [modules/field/modules/number/number.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test) · Licensed GPL-2.0-or-later (see LICENSE)._
