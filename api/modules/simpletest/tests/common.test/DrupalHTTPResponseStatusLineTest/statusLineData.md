# DrupalHTTPResponseStatusLineTest::statusLineData()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1362–1391 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1362-L1391)
- **Class:** [DrupalHTTPResponseStatusLineTest](../DrupalHTTPResponseStatusLineTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function statusLineData()
```

## Documentation

```text
Data provider for testStatusLine().

@return array
  Test data.
```

## Code

```php
  protected function statusLineData() {
    return array(
      array(
        'HTTP/1.1 200 OK',
        array(
          'http_version' => 'HTTP/1.1',
          'response_code' => '200',
          'reason_phrase' => 'OK',
        ),
      ),
      // Data set with no reason phrase.
      array(
        'HTTP/1.1 200',
        array(
          'http_version' => 'HTTP/1.1',
          'response_code' => '200',
          'reason_phrase' => '',
        ),
      ),
      // Arbitrary strings.
      array(
        'version code multi word explanation',
        array(
          'http_version' => 'version',
          'response_code' => 'code',
          'reason_phrase' => 'multi word explanation',
        ),
      ),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
