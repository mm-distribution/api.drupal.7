# CommonSizeTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 603–624 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L603-L624)
- **Class:** [CommonSizeTestCase](../CommonSizeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    $kb = DRUPAL_KILOBYTE;
    $this->exact_test_cases = array(
      '1 byte' => 1,
      '1 KB'   => $kb,
      '1 MB'   => $kb * $kb,
      '1 GB'   => $kb * $kb * $kb,
      '1 TB'   => $kb * $kb * $kb * $kb,
      '1 PB'   => $kb * $kb * $kb * $kb * $kb,
      '1 EB'   => $kb * $kb * $kb * $kb * $kb * $kb,
      '1 ZB'   => $kb * $kb * $kb * $kb * $kb * $kb * $kb,
      '1 YB'   => $kb * $kb * $kb * $kb * $kb * $kb * $kb * $kb,
    );
    $this->rounded_test_cases = array(
      '2 bytes' => 2,
      '1 MB' => ($kb * $kb) - 1, // rounded to 1 MB (not 1000 or 1024 kilobyte!)
      round(3623651 / ($this->exact_test_cases['1 MB']), 2) . ' MB' => 3623651, // megabytes
      round(67234178751368124 / ($this->exact_test_cases['1 PB']), 2) . ' PB' => 67234178751368124, // petabytes
      round(235346823821125814962843827 / ($this->exact_test_cases['1 YB']), 2) . ' YB' => 235346823821125814962843827, // yottabytes
    );
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
