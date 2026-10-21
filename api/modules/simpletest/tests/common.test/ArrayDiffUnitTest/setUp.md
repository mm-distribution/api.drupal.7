# ArrayDiffUnitTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3318–3342 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3318-L3342)
- **Class:** [ArrayDiffUnitTest](../ArrayDiffUnitTest.md)
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
    parent::setUp();

    $this->array1 = array(
      'same' => 'yes',
      'different' => 'no',
      'array_empty_diff' => array(),
      'null' => NULL,
      'int_diff' => 1,
      'array_diff' => array('same' => 'same', 'array' => array('same' => 'same')),
      'array_compared_to_string' => array('value'),
      'string_compared_to_array' => 'value',
      'new' => 'new',
    );
    $this->array2 = array(
      'same' => 'yes',
      'different' => 'yes',
      'array_empty_diff' => array(),
      'null' => NULL,
      'int_diff' => '1',
      'array_diff' => array('same' => 'different', 'array' => array('same' => 'same')),
      'array_compared_to_string' => 'value',
      'string_compared_to_array' => array('value'),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
