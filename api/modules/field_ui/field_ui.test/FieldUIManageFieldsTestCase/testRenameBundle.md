# FieldUIManageFieldsTestCase::testRenameBundle()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 424–434 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L424-L434)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testRenameBundle()
```

## Documentation

```text
Tests renaming a bundle.
```

## Code

```php
  function testRenameBundle() {
    $type2 = strtolower($this->randomName(8)) . '_' .'test';
    $hyphen_type2 = str_replace('_', '-', $type2);

    $options = array(
      'type' => $type2,
    );
    $this->drupalPost('admin/structure/types/manage/' . $this->hyphen_type, $options, t('Save content type'));

    $this->drupalGet('admin/structure/types/manage/' . $hyphen_type2 . '/fields');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
