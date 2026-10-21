# requirements1_test_requirements()

- **Type:** Function
- **File:** [`modules/simpletest/tests/requirements1_test.install`](_file.md), lines 6–21 · [local source](../../../../../source/modules/simpletest/tests/requirements1_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/requirements1_test.install#L6-L21)
- **Module/theme:** batch_test
- **Implements:** [hook_requirements()](../../../system/system.api.php/hook_requirements.md)

## Signature

```php
function requirements1_test_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function requirements1_test_requirements($phase) {
  $requirements = array();
  // Ensure translations don't break during installation.
  $t = get_t();

  // Always fails requirements.
  if ('install' == $phase) {
    $requirements['requirements1_test'] = array(
      'title' => $t('Requirements 1 Test'),
      'severity' => REQUIREMENT_ERROR,
      'description' => $t('Requirements 1 Test failed requirements.'),
    );
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/requirements1_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/requirements1_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
