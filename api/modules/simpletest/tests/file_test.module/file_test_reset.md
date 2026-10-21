# file_test_reset()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 152–172 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L152-L172)
- **Module/theme:** batch_test

## Signature

```php
function file_test_reset()
```

## Documentation

```text
Reset/initialize the history of calls to the file_* hooks.

@see file_test_get_calls()
@see file_test_reset()
```

## Code

```php
function file_test_reset() {
  // Keep track of calls to these hooks
  $results = array(
    'load' => array(),
    'validate' => array(),
    'download' => array(),
    'insert' => array(),
    'update' => array(),
    'copy' => array(),
    'move' => array(),
    'delete' => array(),
  );
  variable_set('file_test_results', $results);

  // These hooks will return these values, see file_test_set_return().
  $return = array(
    'validate' => array(),
    'download' => NULL,
  );
  variable_set('file_test_return', $return);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
