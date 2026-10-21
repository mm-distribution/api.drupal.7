# DrupalWebTestCase::assertMailPattern()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 4028–4033 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L4028-L4033)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertMailPattern($field_name, $regex, $message)
```

## Documentation

```text
Asserts that the most recently sent e-mail message has the pattern in it.

@param $field_name
  Name of field or message property to assert: subject, body, id, ...
@param $regex
  Pattern to search for.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertMailPattern($field_name, $regex, $message) {
    $mails = $this->drupalGetMails();
    $mail = end($mails);
    $regex_found = preg_match("/$regex/", $mail[$field_name]);
    return $this->assertTrue($regex_found, t('Expected text found in @field of email message: "@expected".', array('@field' => $field_name, '@expected' => $regex)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
