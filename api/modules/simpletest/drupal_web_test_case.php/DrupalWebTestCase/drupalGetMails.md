# DrupalWebTestCase::drupalGetMails()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3220–3234 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3220-L3234)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalGetMails($filter = array())
```

## Documentation

```text
Gets an array containing all e-mails sent during this test case.

@param $filter
  An array containing key/value pairs used to filter the e-mails that are returned.
@return
  An array containing e-mail messages captured during the current test.
```

## Code

```php
  protected function drupalGetMails($filter = array()) {
    $captured_emails = variable_get('drupal_test_email_collector', array());
    $filtered_emails = array();

    foreach ($captured_emails as $message) {
      foreach ($filter as $key => $value) {
        if (!isset($message[$key]) || $message[$key] != $value) {
          continue 2;
        }
      }
      $filtered_emails[] = $message;
    }

    return $filtered_emails;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
