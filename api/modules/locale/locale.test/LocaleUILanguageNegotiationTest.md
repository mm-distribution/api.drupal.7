# LocaleUILanguageNegotiationTest

- **Type:** Class
- **File:** [`modules/locale/locale.test`](_file.md), lines 2351–2627 · [local source](../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2351-L2627)
- **Module/theme:** locale

## Signature

```php
class LocaleUILanguageNegotiationTest extends DrupalWebTestCase
```

## Documentation

```text
Test UI language negotiation
1. URL (PATH) > DEFAULT
   UI Language base on URL prefix, browser language preference has no
   influence:
     admin/config
       UI in site default language
     zh-hans/admin/config
       UI in Chinese
     blah-blah/admin/config
       404
2. URL (PATH) > BROWSER > DEFAULT
       admin/config
         UI in user's browser language preference if the site has that
         language enabled, if not, the default language
       zh-hans/admin/config
         UI in Chinese
       blah-blah/admin/config
         404
3. URL (DOMAIN) > DEFAULT
       http://example.com/admin/config
         UI language in site default
       http://example.cn/admin/config
         UI language in Chinese
```

## Methods (derived index)

- [getInfo()](LocaleUILanguageNegotiationTest/getInfo.md)
- [setUp()](LocaleUILanguageNegotiationTest/setUp.md)
- [testUILanguageNegotiation()](LocaleUILanguageNegotiationTest/testUILanguageNegotiation.md) — Tests for language switching by URL path.
- [runTest()](LocaleUILanguageNegotiationTest/runTest.md)
- [testUrlLanguageFallback()](LocaleUILanguageNegotiationTest/testUrlLanguageFallback.md) — Test URL language detection when the requested URL has no language.
- [testLanguageDomain()](LocaleUILanguageNegotiationTest/testLanguageDomain.md) — Tests url() when separate domains are used for multiple languages.

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
