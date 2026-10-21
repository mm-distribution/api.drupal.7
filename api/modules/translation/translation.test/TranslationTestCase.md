# TranslationTestCase

- **Type:** Class
- **File:** [`modules/translation/translation.test`](_file.md), lines 11–494 · [local source](../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L11-L494)
- **Module/theme:** translation

## Signature

```php
class TranslationTestCase extends DrupalWebTestCase
```

## Documentation

```text
Functional tests for the Translation module.
```

## Properties

### $book

```php
protected $book;
```

### $admin_user

```php
protected $admin_user;
```

### $translator

```php
protected $translator;
```

## Methods (derived index)

- [getInfo()](TranslationTestCase/getInfo.md)
- [setUp()](TranslationTestCase/setUp.md)
- [testContentTranslation()](TranslationTestCase/testContentTranslation.md) — Creates, modifies, and updates a basic page with a translation.
- [testLanguageSwitchLinks()](TranslationTestCase/testLanguageSwitchLinks.md) — Checks that the language switch links behave properly.
- [testLanguageSwitcherBlockIntegration()](TranslationTestCase/testLanguageSwitcherBlockIntegration.md) — Tests that the language switcher block alterations work as intended.
- [resetCaches()](TranslationTestCase/resetCaches.md) — Resets static caches to make the test code match the client-side behavior.
- [emptyNode()](TranslationTestCase/emptyNode.md) — Returns an empty node data structure.
- [addLanguage()](TranslationTestCase/addLanguage.md) — Installs the specified language, or enables it if it is already installed.
- [createPage()](TranslationTestCase/createPage.md) — Creates a "Basic page" in the specified language.
- [createTranslation()](TranslationTestCase/createTranslation.md) — Creates a translation for a basic page in the specified language.
- [assertContentByXPath()](TranslationTestCase/assertContentByXPath.md) — Asserts an element identified by the given XPath has the given content.
- [assertLanguageSwitchLinks()](TranslationTestCase/assertLanguageSwitchLinks.md) — Tests whether the specified language switch links are found.
- [findContentByXPath()](TranslationTestCase/findContentByXPath.md) — Searches for elements matching the given xpath and value.

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
