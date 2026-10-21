# DateFormatTestCase::testDefaultDateFormats()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1553–1581 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1553-L1581)
- **Class:** [DateFormatTestCase](../DateFormatTestCase.md)
- **Module/theme:** system

## Signature

```php
function testDefaultDateFormats()
```

## Documentation

```text
Test the default date type formats are consistent.
```

## Code

```php
  function testDefaultDateFormats() {
    // These are the default format values from format_date().
    $default_formats = array(
      'short' => 'm/d/Y - H:i',
      'medium' => 'D, m/d/Y - H:i',
      'long' => 'l, F j, Y - H:i',
    );

    // Clear the date format variables.
    variable_del('date_format_short');
    variable_del('date_format_medium');
    variable_del('date_format_long');

    $this->drupalGet('admin/config/regional/date-time');

    foreach ($default_formats as $format_name => $format_value) {
      $id = 'edit-date-format-' . $format_name;
      // Check that the configuration fields match the default format.
      $this->assertOptionSelected(
        $id,
        $format_value,
        format_string('The @type format type matches the expected format @format.',
        array(
          '@type' => $format_name,
          '@format' => $format_value,
        )
      ));
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
