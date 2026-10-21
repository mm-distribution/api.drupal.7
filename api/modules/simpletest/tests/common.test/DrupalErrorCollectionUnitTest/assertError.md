# DrupalErrorCollectionUnitTest::assertError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2820–2827 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2820-L2827)
- **Class:** [DrupalErrorCollectionUnitTest](../DrupalErrorCollectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function assertError($error, $group, $function, $file, $message = NULL)
```

## Documentation

```text
Assert that a collected error matches what we are expecting.
```

## Code

```php
  function assertError($error, $group, $function, $file, $message = NULL) {
    $this->assertEqual($error['group'], $group, format_string("Group was %group", array('%group' => $group)));
    $this->assertEqual($error['caller']['function'], $function, format_string("Function was %function", array('%function' => $function)));
    $this->assertEqual(drupal_basename($error['caller']['file']), $file, format_string("File was %file", array('%file' => $file)));
    if (isset($message)) {
      $this->assertEqual($error['message'], $message, format_string("Message was %message", array('%message' => $message)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
