# TranslationTestCase::resetCaches()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 263–265 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L263-L265)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function resetCaches()
```

## Documentation

```text
Resets static caches to make the test code match the client-side behavior.
```

## Code

```php
  function resetCaches() {
    drupal_static_reset('locale_url_outbound_alter');
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
