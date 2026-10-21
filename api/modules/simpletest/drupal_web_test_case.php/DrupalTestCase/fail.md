# DrupalTestCase::fail()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 470–472 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L470-L472)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function fail($message = NULL, $group = 'Other')
```

## Documentation

```text
Fire an assertion that is always negative.

@param $message
  The message to display along with the assertion.
@param $group
  The type of assertion - examples are "Browser", "PHP".
@return
  FALSE.
```

## Code

```php
  protected function fail($message = NULL, $group = 'Other') {
    return $this->assert(FALSE, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
