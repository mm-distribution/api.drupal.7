# DrupalUnitTestCase::__construct()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 760–763 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L760-L763)
- **Class:** [DrupalUnitTestCase](../DrupalUnitTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function __construct($test_id = NULL)
```

## Documentation

```text
Constructor for DrupalUnitTestCase.
```

## Code

```php
  function __construct($test_id = NULL) {
    parent::__construct($test_id);
    $this->skipClasses[__CLASS__] = TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
