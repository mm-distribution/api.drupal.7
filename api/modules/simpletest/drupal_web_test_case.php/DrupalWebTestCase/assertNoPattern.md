# DrupalWebTestCase::assertNoPattern()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3493–3498 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3493-L3498)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoPattern($pattern, $message = '', $group = 'Other')
```

## Documentation

```text
Will trigger a pass if the perl regex pattern is not present in raw content.

@param $pattern
  Perl regex to look for including the regex delimiters.
@param $message
  Message to display.
@param $group
  The group this message belongs to.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertNoPattern($pattern, $message = '', $group = 'Other') {
    if (!$message) {
      $message = t('Pattern "@pattern" not found', array('@pattern' => $pattern));
    }
    return $this->assert(!preg_match($pattern, $this->drupalGetContent()), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
