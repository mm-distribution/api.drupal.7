# DrupalTestCase::assertNull()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 354–356 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L354-L356)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNull($value, $message = '', $group = 'Other')
```

## Documentation

```text
Check to see if a value is NULL.

@param $value
  The value on which the assertion is to be done.
@param $message
  The message to display along with the assertion.
@param $group
  The type of assertion - examples are "Browser", "PHP".
@return
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertNull($value, $message = '', $group = 'Other') {
    return $this->assert(!isset($value), $message ? $message : t('Value @value is NULL.', array('@value' => var_export($value, TRUE))), $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
