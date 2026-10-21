# url_alter_test_foo()

- **Type:** Function
- **File:** [`modules/simpletest/tests/url_alter_test.module`](_file.md), lines 24–27 · [local source](../../../../../source/modules/simpletest/tests/url_alter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module#L24-L27)
- **Module/theme:** batch_test

## Signature

```php
function url_alter_test_foo()
```

## Documentation

```text
Menu callback.
```

## Code

```php
function url_alter_test_foo() {
  print 'current_path=' . current_path() . ' request_path=' . request_path();
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/url_alter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
