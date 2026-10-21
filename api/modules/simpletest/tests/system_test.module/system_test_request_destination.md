# system_test_request_destination()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 536–543 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L536-L543)
- **Module/theme:** batch_test

## Signature

```php
function system_test_request_destination()
```

## Documentation

```text
Page callback to print out $_REQUEST['destination'] for testing.
```

## Code

```php
function system_test_request_destination() {
  if (isset($_REQUEST['destination'])) {
    print $_REQUEST['destination'];
  }
  // No need to render the whole page, we are just interested in this bit of
  // information.
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
