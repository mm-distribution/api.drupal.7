# system_test_multiple_redirects()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 215–222 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L215-L222)
- **Module/theme:** batch_test

## Signature

```php
function system_test_multiple_redirects($count)
```

## Documentation

```text
Menu callback; sends a redirect header to itself until $count argument is 0.

Emulates the variable number of redirects (given by initial $count argument)
to the final destination URL by continuous sending of 301 HTTP redirect
headers to itself together with decrementing the $count parameter until the
$count parameter reaches 0. After that it returns an empty string to render
the final destination page.

@param $count
  The count of redirects left until the final destination page.

@returns
  The location redirect if the $count > 0, otherwise an empty string.
```

## Code

```php
function system_test_multiple_redirects($count) {
  $count = (int) $count;
  if ($count > 0) {
    header("location: " . url('system-test/multiple-redirects/' . --$count, array('absolute' => TRUE)), TRUE, 301);
    exit;
  }
  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
