# LocaleUrlRewritingTest

- **Type:** Class
- **File:** [`modules/locale/locale.test`](_file.md), lines 2632–2780 · [local source](../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2632-L2780)
- **Module/theme:** locale

## Signature

```php
class LocaleUrlRewritingTest extends DrupalWebTestCase
```

## Documentation

```text
Test that URL rewriting works as expected.
```

## Properties

### $web_user

```php
protected $web_user;
```

## Methods (derived index)

- [getInfo()](LocaleUrlRewritingTest/getInfo.md)
- [setUp()](LocaleUrlRewritingTest/setUp.md)
- [testUrlRewritingEdgeCases()](LocaleUrlRewritingTest/testUrlRewritingEdgeCases.md) — Check that disabled or non-installed languages are not considered.
- [checkUrl()](LocaleUrlRewritingTest/checkUrl.md) — Check URL rewriting for the given language.
- [testDomainNameNegotiationPort()](LocaleUrlRewritingTest/testDomainNameNegotiationPort.md) — Check URL rewriting when using a domain name and a non-standard port.

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
