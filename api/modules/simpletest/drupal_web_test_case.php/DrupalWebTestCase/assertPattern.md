# DrupalWebTestCase::assertPattern()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3474–3479 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3474-L3479)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertPattern($pattern, $message = '', $group = 'Other')
```

## Documentation

```text
Will trigger a pass if the Perl regex pattern is found in the raw content.

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
  protected function assertPattern($pattern, $message = '', $group = 'Other') {
    if (!$message) {
      $message = t('Pattern "@pattern" found', array('@pattern' => $pattern));
    }
    return $this->assert((bool) preg_match($pattern, $this->drupalGetContent()), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
