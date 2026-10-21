# UrlAlterFunctionalTest::assertUrlInboundAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 240–244 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L240-L244)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertUrlInboundAlter($original, $final)
```

## Documentation

```text
Assert that a inbound path is altered to an expected value.

@param $original
  A string with the aliased or un-normal path that is run through
  drupal_get_normal_path().
@param $final
  A string with the expected result after url().
@return
  TRUE if $original was correctly altered to $final, FALSE otherwise.
```

## Code

```php
  protected function assertUrlInboundAlter($original, $final) {
    // Test inbound altering.
    $result = drupal_get_normal_path($original);
    $this->assertIdentical($result, $final, format_string('Altered inbound URL %original, expected %final, and got %result.', array('%original' => $original, '%final' => $final, '%result' => $result)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
