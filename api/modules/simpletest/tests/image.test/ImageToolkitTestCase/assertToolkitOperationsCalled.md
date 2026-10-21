# ImageToolkitTestCase::assertToolkitOperationsCalled()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 51–72 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L51-L72)
- **Class:** [ImageToolkitTestCase](../ImageToolkitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertToolkitOperationsCalled(array $expected)
```

## Documentation

```text
Assert that all of the specified image toolkit operations were called
exactly once once, other values result in failure.

@param $expected
  Array with string containing with the operation name, e.g. 'load',
  'save', 'crop', etc.
```

## Code

```php
  function assertToolkitOperationsCalled(array $expected) {
    // Determine which operations were called.
    $actual = array_keys(array_filter(image_test_get_all_calls()));

    // Determine if there were any expected that were not called.
    $uncalled = array_diff($expected, $actual);
    if (count($uncalled)) {
      $this->assertTrue(FALSE, format_string('Expected operations %expected to be called but %uncalled was not called.', array('%expected' => implode(', ', $expected), '%uncalled' => implode(', ', $uncalled))));
    }
    else {
      $this->assertTrue(TRUE, format_string('All the expected operations were called: %expected', array('%expected' => implode(', ', $expected))));
    }

    // Determine if there were any unexpected calls.
    $unexpected = array_diff($actual, $expected);
    if (count($unexpected)) {
      $this->assertTrue(FALSE, format_string('Unexpected operations were called: %unexpected.', array('%unexpected' => implode(', ', $unexpected))));
    }
    else {
      $this->assertTrue(TRUE, 'No unexpected operations were called.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
