# hook_test_finished()

- **Type:** Hook (documentation function)
- **File:** [`modules/simpletest/simpletest.api.php`](_file.md), lines 54–55 · [local source](../../../../source/modules/simpletest/simpletest.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.api.php#L54-L55)
- **Module/theme:** simpletest
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_test_finished($results)
```

## Documentation

```text
An individual test has finished.

This hook is called when an individual test has finished.

@param
  $results The results of the test as gathered by DrupalWebTestCase.

@see DrupalWebTestCase->results
```

## Code

```php
function hook_test_finished($results) {
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_test_finished()".

_None found._

---
_Drupal 7.103 · [modules/simpletest/simpletest.api.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
