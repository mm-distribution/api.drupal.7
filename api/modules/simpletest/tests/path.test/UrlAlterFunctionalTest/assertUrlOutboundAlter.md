# UrlAlterFunctionalTest::assertUrlOutboundAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 221–227 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L221-L227)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertUrlOutboundAlter($original, $final)
```

## Documentation

```text
Assert that an outbound path is altered to an expected value.

@param $original
  A string with the original path that is run through url().
@param $final
  A string with the expected result after url().
@return
  TRUE if $original was correctly altered to $final, FALSE otherwise.
```

## Code

```php
  protected function assertUrlOutboundAlter($original, $final) {
    // Test outbound altering.
    $result = url($original);
    $base_path = base_path() . (variable_get('clean_url', '0') ? '' : '?q=');
    $result = substr($result, strlen($base_path));
    $this->assertIdentical($result, $final, format_string('Altered outbound URL %original, expected %final, and got %result.', array('%original' => $original, '%final' => $final, '%result' => $result)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
