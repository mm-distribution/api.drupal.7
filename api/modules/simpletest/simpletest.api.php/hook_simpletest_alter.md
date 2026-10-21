# hook_simpletest_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/simpletest/simpletest.api.php`](_file.md), lines 21–26 · [local source](../../../../source/modules/simpletest/simpletest.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.api.php#L21-L26)
- **Module/theme:** simpletest
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_simpletest_alter(&$groups)
```

## Documentation

```text
Alter the list of tests.

@param $groups
  A two dimension array, the first key is the test group (as defined in
  getInfo) the second is the name of the class and the value is the return
  value of the getInfo method.
```

## Code

```php
function hook_simpletest_alter(&$groups) {
  // An alternative session handler module would not want to run the original
  // Session HTTPS handling test because it checks the sessions table in the
  // database.
  unset($groups['Session']['testHttpsSession']);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_simpletest_alter()".

_None found._

---
_Drupal 7.103 · [modules/simpletest/simpletest.api.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
