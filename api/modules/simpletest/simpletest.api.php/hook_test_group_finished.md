# hook_test_group_finished()

- **Type:** Hook (documentation function)
- **File:** [`modules/simpletest/simpletest.api.php`](_file.md), lines 41–42 · [local source](../../../../source/modules/simpletest/simpletest.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.api.php#L41-L42)
- **Module/theme:** simpletest
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_test_group_finished()
```

## Documentation

```text
A test group has finished.

This hook is called just once at the end of a test group.
```

## Code

```php
function hook_test_group_finished() {
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_test_group_finished()".

_None found._

---
_Drupal 7.103 · [modules/simpletest/simpletest.api.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
