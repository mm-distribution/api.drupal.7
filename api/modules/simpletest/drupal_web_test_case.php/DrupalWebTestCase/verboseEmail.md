# DrupalWebTestCase::verboseEmail()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 4041–4047 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L4041-L4047)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function verboseEmail($count = 1)
```

## Documentation

```text
Outputs to verbose the most recent $count emails sent.

@param $count
  Optional number of emails to output.
```

## Code

```php
  protected function verboseEmail($count = 1) {
    $mails = $this->drupalGetMails();
    for ($i = sizeof($mails) -1; $i >= sizeof($mails) - $count && $i >= 0; $i--) {
      $mail = $mails[$i];
      $this->verbose(t('Email:') . '<pre>' . print_r($mail, TRUE) . '</pre>');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
