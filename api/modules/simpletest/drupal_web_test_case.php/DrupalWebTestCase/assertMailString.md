# DrupalWebTestCase::assertMailString()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 4000–4015 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L4000-L4015)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertMailString($field_name, $string, $email_depth)
```

## Documentation

```text
Asserts that the most recently sent e-mail message has the string in it.

@param $field_name
  Name of field or message property to assert: subject, body, id, ...
@param $string
  String to search for.
@param $email_depth
  Number of emails to search for string, starting with most recent.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertMailString($field_name, $string, $email_depth) {
    $mails = $this->drupalGetMails();
    $string_found = FALSE;
    for ($i = sizeof($mails) -1; $i >= sizeof($mails) - $email_depth && $i >= 0; $i--) {
      $mail = $mails[$i];
      // Normalize whitespace, as we don't know what the mail system might have
      // done. Any run of whitespace becomes a single space.
      $normalized_mail = preg_replace('/\s+/', ' ', $mail[$field_name]);
      $normalized_string = preg_replace('/\s+/', ' ', $string);
      $string_found = (FALSE !== strpos($normalized_mail, $normalized_string));
      if ($string_found) {
        break;
      }
    }
    return $this->assertTrue($string_found, t('Expected text found in @field of email message: "@expected".', array('@field' => $field_name, '@expected' => $string)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
