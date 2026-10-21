# hook_drupal_goto_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3902–3905 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3902-L3905)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_drupal_goto_alter(&$path, &$options, &$http_response_code)
```

## Documentation

```text
Change the page the user is sent to by drupal_goto().

@param $path
  A Drupal path or a full URL.
@param $options
  An associative array of additional URL options to pass to url().
@param $http_response_code
  The HTTP status code to use for the redirection. See drupal_goto() for more
  information.
```

## Code

```php
function hook_drupal_goto_alter(&$path, &$options, &$http_response_code) {
  // A good addition to misery module.
  $http_response_code = 500;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_drupal_goto_alter()".

- [common_test_drupal_goto_alter()](../../simpletest/tests/common_test.module/common_test_drupal_goto_alter.md) — `modules/simpletest/tests/common_test.module`
- [session_test_drupal_goto_alter()](../../simpletest/tests/session_test.module/session_test_drupal_goto_alter.md) — `modules/simpletest/tests/session_test.module`
- [overlay_drupal_goto_alter()](../../overlay/overlay.module/overlay_drupal_goto_alter.md) — `modules/overlay/overlay.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
