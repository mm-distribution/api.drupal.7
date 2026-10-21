# locale_test_store_language_negotiation()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 121–127 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L121-L127)
- **Module/theme:** locale_test

## Signature

```php
function locale_test_store_language_negotiation()
```

## Documentation

```text
Store the last negotiated languages.
```

## Code

```php
function locale_test_store_language_negotiation() {
  $last = array();
  foreach (language_types() as $type) {
    $last[$type] = $GLOBALS[$type]->language;
  }
  variable_set('locale_test_language_negotiation_last', $last);
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
