# DrupalTestCase::assertNotIdentical()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 442–444 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L442-L444)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNotIdentical($first, $second, $message = '', $group = 'Other')
```

## Documentation

```text
Check to see if two values are not identical.

@param $first
  The first value to check.
@param $second
  The second value to check.
@param $message
  The message to display along with the assertion.
@param $group
  The type of assertion - examples are "Browser", "PHP".
@return
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertNotIdentical($first, $second, $message = '', $group = 'Other') {
    return $this->assert($first !== $second, $message ? $message : t('Value @first is not identical to value @second.', array('@first' => var_export($first, TRUE), '@second' => var_export($second, TRUE))), $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
