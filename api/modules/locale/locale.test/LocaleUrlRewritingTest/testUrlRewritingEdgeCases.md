# LocaleUrlRewritingTest::testUrlRewritingEdgeCases()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2677–2687 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2677-L2687)
- **Class:** [LocaleUrlRewritingTest](../LocaleUrlRewritingTest.md)
- **Module/theme:** locale

## Signature

```php
function testUrlRewritingEdgeCases()
```

## Documentation

```text
Check that disabled or non-installed languages are not considered.
```

## Code

```php
  function testUrlRewritingEdgeCases() {
    // Check URL rewriting with a disabled language.
    $languages = language_list();
    $this->checkUrl($languages['it'], 'Path language is ignored if language is disabled.', 'URL language negotiation does not work with disabled languages');

    // Check URL rewriting with a non-installed language.
    $non_existing = language_default();
    $non_existing->language = $this->randomName();
    $non_existing->prefix = $this->randomName();
    $this->checkUrl($non_existing, 'Path language is ignored if language is not installed.', 'URL language negotiation does not work with non-installed languages');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
