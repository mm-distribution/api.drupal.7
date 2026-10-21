# FieldUIManageFieldsTestCase::testExternalDestinations()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 458–466 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L458-L466)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testExternalDestinations()
```

## Documentation

```text
Tests that external URLs in the 'destinations' query parameter are blocked.
```

## Code

```php
  function testExternalDestinations() {
    $path = 'admin/structure/types/manage/article/fields/field_tags/field-settings';
    $options = array(
      'query' => array('destinations' => array('http://example.com')),
    );
    $this->drupalPost($path, NULL, t('Save field settings'), $options);

    $this->assertUrl('admin/structure/types/manage/article/fields', array(), 'Stayed on the same site.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
