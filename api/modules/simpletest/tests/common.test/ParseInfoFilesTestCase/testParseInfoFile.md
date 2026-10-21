# ParseInfoFilesTestCase::testParseInfoFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2845–2850 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2845-L2850)
- **Class:** [ParseInfoFilesTestCase](../ParseInfoFilesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testParseInfoFile()
```

## Documentation

```text
Parse an example .info file an verify the results.
```

## Code

```php
  function testParseInfoFile() {
    $info_values = drupal_parse_info_file(drupal_get_path('module', 'simpletest') . '/tests/common_test_info.txt');
    $this->assertEqual($info_values['simple_string'], 'A simple string', 'Simple string value was parsed correctly.', 'System');
    $this->assertEqual($info_values['simple_constant'], WATCHDOG_INFO, 'Constant value was parsed correctly.', 'System');
    $this->assertEqual($info_values['double_colon'], 'dummyClassName::', 'Value containing double-colon was parsed correctly.', 'System');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
