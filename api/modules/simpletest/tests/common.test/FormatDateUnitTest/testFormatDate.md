# FormatDateUnitTest::testFormatDate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2990–3043 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2990-L3043)
- **Class:** [FormatDateUnitTest](../FormatDateUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFormatDate()
```

## Documentation

```text
Tests for the format_date() function.
```

## Code

```php
  function testFormatDate() {
    global $user, $language;

    $timestamp = strtotime('2007-03-26T00:00:00+00:00');
    $this->assertIdentical(format_date($timestamp, 'custom', 'l, d-M-y H:i:s T', 'America/Los_Angeles', 'en'), 'Sunday, 25-Mar-07 17:00:00 PDT', 'Test all parameters.');
    $this->assertIdentical(format_date($timestamp, 'custom', 'l, d-M-y H:i:s T', 'America/Los_Angeles', self::LANGCODE), 'domingo, 25-Mar-07 17:00:00 PDT', 'Test translated format.');
    $this->assertIdentical(format_date($timestamp, 'custom', '\\l, d-M-y H:i:s T', 'America/Los_Angeles', self::LANGCODE), 'l, 25-Mar-07 17:00:00 PDT', 'Test an escaped format string.');
    $this->assertIdentical(format_date($timestamp, 'custom', '\\\\l, d-M-y H:i:s T', 'America/Los_Angeles', self::LANGCODE), '\\domingo, 25-Mar-07 17:00:00 PDT', 'Test format containing backslash character.');
    $this->assertIdentical(format_date($timestamp, 'custom', '\\\\\\l, d-M-y H:i:s T', 'America/Los_Angeles', self::LANGCODE), '\\l, 25-Mar-07 17:00:00 PDT', 'Test format containing backslash followed by escaped format string.');
    $this->assertIdentical(format_date($timestamp, 'custom', 'l, d-M-y H:i:s T', 'Europe/London', 'en'), 'Monday, 26-Mar-07 01:00:00 BST', 'Test a different time zone.');

    // Create an admin user and add Spanish language.
    $admin_user = $this->drupalCreateUser(array('administer languages'));
    $this->drupalLogin($admin_user);
    $edit = array(
      'langcode' => self::LANGCODE,
      'name' => self::LANGCODE,
      'native' => self::LANGCODE,
      'direction' => LANGUAGE_LTR,
      'prefix' => self::LANGCODE,
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add custom language'));

    // Create a test user to carry out the tests.
    $test_user = $this->drupalCreateUser();
    $this->drupalLogin($test_user);
    $edit = array('language' => self::LANGCODE, 'mail' => $test_user->mail, 'timezone' => 'America/Los_Angeles');
    $this->drupalPost('user/' . $test_user->uid . '/edit', $edit, t('Save'));

    // Disable session saving as we are about to modify the global $user.
    drupal_save_session(FALSE);
    // Save the original user and language and then replace it with the test user and language.
    $real_user = $user;
    $user = user_load($test_user->uid, TRUE);
    $real_language = $language->language;
    $language->language = $user->language;
    // Simulate a Drupal bootstrap with the logged-in user.
    date_default_timezone_set(drupal_get_user_timezone());

    $this->assertIdentical(format_date($timestamp, 'custom', 'l, d-M-y H:i:s T', 'America/Los_Angeles', 'en'), 'Sunday, 25-Mar-07 17:00:00 PDT', 'Test a different language.');
    $this->assertIdentical(format_date($timestamp, 'custom', 'l, d-M-y H:i:s T', 'Europe/London'), 'Monday, 26-Mar-07 01:00:00 BST', 'Test a different time zone.');
    $this->assertIdentical(format_date($timestamp, 'custom', 'l, d-M-y H:i:s T'), 'domingo, 25-Mar-07 17:00:00 PDT', 'Test custom date format.');
    $this->assertIdentical(format_date($timestamp, 'long'), 'domingo, 25. marzo 2007 - 17:00', 'Test long date format.');
    $this->assertIdentical(format_date($timestamp, 'medium'), '25. marzo 2007 - 17:00', 'Test medium date format.');
    $this->assertIdentical(format_date($timestamp, 'short'), '2007 Mar 25 - 5:00pm', 'Test short date format.');
    $this->assertIdentical(format_date($timestamp), '25. marzo 2007 - 17:00', 'Test default date format.');

    // Restore the original user and language, and enable session saving.
    $user = $real_user;
    $language->language = $real_language;
    // Restore default time zone.
    date_default_timezone_set(drupal_get_user_timezone());
    drupal_save_session(TRUE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
