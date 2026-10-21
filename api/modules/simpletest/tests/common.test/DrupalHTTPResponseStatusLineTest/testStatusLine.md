# DrupalHTTPResponseStatusLineTest::testStatusLine()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1341–1354 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1341-L1354)
- **Class:** [DrupalHTTPResponseStatusLineTest](../DrupalHTTPResponseStatusLineTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testStatusLine()
```

## Documentation

```text
Tests parsing HTTP response status line.
```

## Code

```php
  public function testStatusLine() {
    // Grab the big array of test data from statusLineData().
    $data = $this->statusLineData();
    foreach($data as $test_case) {
      $test_data = array_shift($test_case);
      $expected = array_shift($test_case);

      $outcome = _drupal_parse_response_status($test_data);

      foreach(array_keys($expected) as $key) {
        $this->assertIdentical($outcome[$key], $expected[$key]);
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
