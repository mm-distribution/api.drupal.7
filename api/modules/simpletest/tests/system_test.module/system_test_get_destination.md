# system_test_get_destination()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 524–531 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L524-L531)
- **Module/theme:** batch_test

## Signature

```php
function system_test_get_destination()
```

## Documentation

```text
Page callback to print out $_GET['destination'] for testing.
```

## Code

```php
function system_test_get_destination() {
  if (isset($_GET['destination'])) {
    print $_GET['destination'];
  }
  // No need to render the whole page, we are just interested in this bit of
  // information.
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
