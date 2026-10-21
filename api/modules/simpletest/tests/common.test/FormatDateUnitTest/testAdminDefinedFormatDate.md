# FormatDateUnitTest::testAdminDefinedFormatDate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2948–2985 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2948-L2985)
- **Class:** [FormatDateUnitTest](../FormatDateUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testAdminDefinedFormatDate()
```

## Documentation

```text
Test admin-defined formats in format_date().
```

## Code

```php
  function testAdminDefinedFormatDate() {
    // Create an admin user.
    $this->admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($this->admin_user);

    // Add new date format.
    $admin_date_format = 'j M y';
    $edit = array('date_format' => $admin_date_format);
    $this->drupalPost('admin/config/regional/date-time/formats/add', $edit, 'Add format');

    // Add a new date format which just differs in the case.
    $admin_date_format_uppercase = 'j M Y';
    $edit = array('date_format' => $admin_date_format_uppercase);
    $this->drupalPost('admin/config/regional/date-time/formats/add', $edit, t('Add format'));
    $this->assertText(t('Custom date format added.'));

    // Add new date type.
    $edit = array(
      'date_type' => 'Example Style',
      'machine_name' => 'example_style',
      'date_format' => $admin_date_format,
    );
    $this->drupalPost('admin/config/regional/date-time/types/add', $edit, 'Add date type');

   // Add a second date format with a different case than the first.
    $edit = array(
      'machine_name' => 'example_style_uppercase',
      'date_type' => 'Example Style Uppercase',
      'date_format' => $admin_date_format_uppercase,
    );
    $this->drupalPost('admin/config/regional/date-time/types/add', $edit, t('Add date type'));
    $this->assertText(t('New date type added successfully.'));

    $timestamp = strtotime('2007-03-10T00:00:00+00:00');
    $this->assertIdentical(format_date($timestamp, 'example_style', '', 'America/Los_Angeles'), '9 Mar 07', 'Test format_date() using an admin-defined date type.');
    $this->assertIdentical(format_date($timestamp, 'example_style_uppercase', '', 'America/Los_Angeles'), '9 Mar 2007', 'Test format_date() using an admin-defined date type with different case.');
    $this->assertIdentical(format_date($timestamp, 'undefined_style'), format_date($timestamp, 'medium'), 'Test format_date() defaulting to medium when $type not found.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
