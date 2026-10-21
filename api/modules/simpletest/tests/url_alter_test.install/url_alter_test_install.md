# url_alter_test_install()

- **Type:** Function
- **File:** [`modules/simpletest/tests/url_alter_test.install`](_file.md), lines 6–12 · [local source](../../../../../source/modules/simpletest/tests/url_alter_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.install#L6-L12)
- **Module/theme:** batch_test

## Signature

```php
function url_alter_test_install()
```

## Documentation

```text
Impelement hook_install().
```

## Code

```php
function url_alter_test_install() {
  // Set the weight of this module to one higher than forum.module.
  db_update('system')
    ->fields(array('weight' => 2))
    ->condition('name', 'url_alter_test')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/url_alter_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
