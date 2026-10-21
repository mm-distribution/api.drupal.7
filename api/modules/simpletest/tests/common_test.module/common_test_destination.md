# common_test_destination()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 116–119 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L116-L119)
- **Module/theme:** batch_test

## Signature

```php
function common_test_destination()
```

## Documentation

```text
Print destination query parameter.
```

## Code

```php
function common_test_destination() {
  $destination = drupal_get_destination();
  print "The destination: " . check_plain($destination['destination']);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
