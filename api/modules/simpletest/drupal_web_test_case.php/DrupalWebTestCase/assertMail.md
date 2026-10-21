# DrupalWebTestCase::assertMail()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3981–3985 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3981-L3985)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertMail($name, $value = '', $message = '')
```

## Documentation

```text
Asserts that the most recently sent e-mail message has the given value.

The field in $name must have the content described in $value.

@param $name
  Name of field or message property to assert. Examples: subject, body, id, ...
@param $value
  Value of the field to assert.
@param $message
  Message to display.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertMail($name, $value = '', $message = '') {
    $captured_emails = variable_get('drupal_test_email_collector', array());
    $email = end($captured_emails);
    return $this->assertTrue($email && isset($email[$name]) && $email[$name] == $value, $message, t('E-mail'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
