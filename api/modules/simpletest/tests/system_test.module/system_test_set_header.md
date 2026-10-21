# system_test_set_header()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 224–227 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L224-L227)
- **Module/theme:** batch_test

## Signature

```php
function system_test_set_header()
```

## Documentation

_No docblock in source._

## Code

```php
function system_test_set_header() {
  drupal_add_http_header($_GET['name'], $_GET['value']);
  return t('The following header was set: %name: %value', array('%name' => $_GET['name'], '%value' => $_GET['value']));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
