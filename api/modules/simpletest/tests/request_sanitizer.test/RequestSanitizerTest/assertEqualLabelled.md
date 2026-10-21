# RequestSanitizerTest::assertEqualLabelled()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 263–270 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L263-L270)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertEqualLabelled($first, $second, $message = '', $group = 'Other', $label = '')
```

## Documentation

```text
Asserts two values are equal, includes a label.

@param mixed $first
  The first value to check.
@param mixed $second
  The second value to check.
@param string $message
  The message to display along with the assertion.
@param string $group
  The type of assertion - examples are "Browser", "PHP".
@param string $label
  The label to include with the message.

@return bool
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertEqualLabelled($first, $second, $message = '', $group = 'Other', $label = '') {
    $label = (empty($label)) ? '' : $label . ': ';
    $message = $message ? $message : t('Value @first is equal to value @second.', array(
      '@first' => var_export($first, TRUE),
      '@second' => var_export($second, TRUE),
    ));
    return $this->assert($first == $second, $label . $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
