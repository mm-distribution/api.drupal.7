# FilterCRUDTestCase::testTextFormatCRUD()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 27–82 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L27-L82)
- **Class:** [FilterCRUDTestCase](../FilterCRUDTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testTextFormatCRUD()
```

## Documentation

```text
Tests CRUD operations for text formats and filters.
```

## Code

```php
  function testTextFormatCRUD() {
    // Add a text format with minimum data only.
    $format = new stdClass();
    $format->format = 'empty_format';
    $format->name = 'Empty format';
    filter_format_save($format);
    $this->verifyTextFormat($format);
    $this->verifyFilters($format);

    // Add another text format specifying all possible properties.
    $format = new stdClass();
    $format->format = 'custom_format';
    $format->name = 'Custom format';
    $format->filters = array(
      'filter_url' => array(
        'status' => 1,
        'settings' => array(
          'filter_url_length' => 30,
        ),
      ),
    );
    filter_format_save($format);
    $this->verifyTextFormat($format);
    $this->verifyFilters($format);

    // Alter some text format properties and save again.
    $format->name = 'Altered format';
    $format->filters['filter_url']['status'] = 0;
    $format->filters['filter_autop']['status'] = 1;
    filter_format_save($format);
    $this->verifyTextFormat($format);
    $this->verifyFilters($format);

    // Add a uncacheable filter and save again.
    $format->filters['filter_test_uncacheable']['status'] = 1;
    filter_format_save($format);
    $this->verifyTextFormat($format);
    $this->verifyFilters($format);

    // Disable the text format.
    filter_format_disable($format);

    $db_format = db_query("SELECT * FROM {filter_format} WHERE format = :format", array(':format' => $format->format))->fetchObject();
    $this->assertFalse($db_format->status, 'Database: Disabled text format is marked as disabled.');
    $formats = filter_formats();
    $this->assertTrue(!isset($formats[$format->format]), 'filter_formats: Disabled text format no longer exists.');

    // Add a new format to check for Xss in format name.
    $format = new stdClass();
    $format->format = 'xss_format';
    $format->name = '<script>alert(123)</script>';
    filter_format_save($format);
    user_role_change_permissions(DRUPAL_ANONYMOUS_RID, array(filter_permission_name($format) => 1));
    $this->drupalGet('filter/tips');
    $this->assertNoRaw($format->name, 'Text format name contains no xss.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
