# FilterAdminTestCase::testUrlFilterAdmin()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 424–431 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L424-L431)
- **Class:** [FilterAdminTestCase](../FilterAdminTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testUrlFilterAdmin()
```

## Documentation

```text
Tests the URL filter settings form is properly validated.
```

## Code

```php
  function testUrlFilterAdmin() {
    // The form does not save with an invalid filter URL length.
    $edit = array(
      'filters[filter_url][settings][filter_url_length]' => $this->randomName(4),
    );
    $this->drupalPost('admin/config/content/formats/filtered_html', $edit, t('Save configuration'));
    $this->assertNoRaw(t('The text format %format has been updated.', array('%format' => 'Filtered HTML')));
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
