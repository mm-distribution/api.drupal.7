# FileHookTestCase::assertFileHooksCalled()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 255–276 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L255-L276)
- **Class:** [FileHookTestCase](../FileHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertFileHooksCalled($expected)
```

## Documentation

```text
Assert that all of the specified hook_file_* hooks were called once, other
values result in failure.

@param $expected
  Array with string containing with the hook name, e.g. 'load', 'save',
  'insert', etc.
```

## Code

```php
  function assertFileHooksCalled($expected) {
    // Determine which hooks were called.
    $actual = array_keys(array_filter(file_test_get_all_calls()));

    // Determine if there were any expected that were not called.
    $uncalled = array_diff($expected, $actual);
    if (count($uncalled)) {
      $this->assertTrue(FALSE, format_string('Expected hooks %expected to be called but %uncalled was not called.', array('%expected' => implode(', ', $expected), '%uncalled' => implode(', ', $uncalled))));
    }
    else {
      $this->assertTrue(TRUE, format_string('All the expected hooks were called: %expected', array('%expected' => empty($expected) ? t('(none)') : implode(', ', $expected))));
    }

    // Determine if there were any unexpected calls.
    $unexpected = array_diff($actual, $expected);
    if (count($unexpected)) {
      $this->assertTrue(FALSE, format_string('Unexpected hooks were called: %unexpected.', array('%unexpected' => empty($unexpected) ? t('(none)') : implode(', ', $unexpected))));
    }
    else {
      $this->assertTrue(TRUE, 'No unexpected hooks were called.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
